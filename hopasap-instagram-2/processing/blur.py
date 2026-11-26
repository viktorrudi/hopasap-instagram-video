import json, sys, subprocess, cv2, numpy as np
import os
FF=os.environ.get("FFMPEG","ffmpeg")
def load(tracks_path):
    if not tracks_path: return []
    return json.load(open(tracks_path))["tracks"]
def active(tracks, fi):
    out=[]
    for t in tracks:
        k=fi-t["start"]; L=len(t["boxes"])
        if 0<=k<L:
            # soft ramp alpha over first/last 4 frames of the (already extended) track
            a=min(1.0,1.0 if t["start"]==0 else (k+1)/4,(L-k)/4)
            out.append((t["boxes"][k],a))
    return out
def blur_frame(fr, boxes):
    H,W=fr.shape[:2]
    for (x1,y1,x2,y2),a in boxes:
        w,h=x2-x1,y2-y1
        if w<6 or h<4: continue
        px,py=0.22*w+10,0.40*h+10
        X1,Y1,X2,Y2=x1-px,y1-py,x2+px,y2+py
        m=int(max(X2-X1,Y2-Y1)*0.35)+20
        cx1,cy1=int(max(0,X1-m)),int(max(0,Y1-m)); cx2,cy2=int(min(W,X2+m)),int(min(H,Y2+m))
        if cx2-cx1<4 or cy2-cy1<4: continue
        crop=fr[cy1:cy2,cx1:cx2].astype(np.float32)
        sig=max(9.0,0.30*h+0.06*w)
        # pixel-average then gaussian: unreadable but soft
        small=cv2.resize(crop,(max(1,int(crop.shape[1]/(sig*0.6))),max(1,int(crop.shape[0]/(sig*0.6)))),interpolation=cv2.INTER_AREA)
        bl=cv2.resize(small,(crop.shape[1],crop.shape[0]),interpolation=cv2.INTER_LINEAR)
        bl=cv2.GaussianBlur(bl,(0,0),sig*0.8)
        mask=np.zeros(crop.shape[:2],np.float32)
        r=max(0,int(min(X2-X1,Y2-Y1)*0.35))
        rx1,ry1,rx2,ry2=int(X1-cx1),int(Y1-cy1),int(X2-cx1),int(Y2-cy1)
        cv2.rectangle(mask,(rx1+r,ry1),(rx2-r,ry2),1,-1); cv2.rectangle(mask,(rx1,ry1+r),(rx2,ry2-r),1,-1)
        for cx,cy in [(rx1+r,ry1+r),(rx2-r,ry1+r),(rx1+r,ry2-r),(rx2-r,ry2-r)]: cv2.circle(mask,(cx,cy),r,1,-1)
        fe=max(3.0,0.12*min(X2-X1,Y2-Y1))
        mask=cv2.GaussianBlur(mask,(0,0),fe)*a
        mask=mask[...,None]
        fr[cy1:cy2,cx1:cx2]=(crop*(1-mask)+bl*mask).clip(0,255).astype(np.uint8)
    return fr
if __name__=="__main__":
    mode=sys.argv[1]; src=sys.argv[2]; tracks=load(sys.argv[3] if sys.argv[3]!="-" else None)
    cap=cv2.VideoCapture(src); W=int(cap.get(3)); H=int(cap.get(4))
    if mode=="crops":
        out=sys.argv[4]; ts=[float(x) for x in sys.argv[5].split(",")]; tiles=[]; fi=0
        want={int(round(t*60)):t for t in ts}
        while True:
            ok,fr=cap.read()
            if not ok: break
            if fi in want:
                fr=blur_frame(fr,active(tracks,fi)); cv2.putText(fr,f"{want[fi]:.2f}",(10,60),0,2,(0,255,255),4); tiles.append(cv2.resize(fr,(540,960)))
            fi+=1
        cv2.imwrite(out,np.hstack(tiles)); print(out,len(tiles)); sys.exit()
    if mode=="sheet":
        out=sys.argv[4]; t0,t1,step=map(float,sys.argv[5:8]); tiles=[]
        fi=0
        while True:
            ok,fr=cap.read()
            if not ok: break
            t=fi/60
            if t0<=t<=t1 and abs((t-t0)/step-round((t-t0)/step))<1/120:
                b=active(tracks,fi); fr=blur_frame(fr,b)
                th=cv2.resize(fr,(270,480)); cv2.putText(th,f"{t:.2f}",(5,20),0,0.6,(0,255,255),2); tiles.append(th)
            fi+=1
        cols=8; rows=[np.hstack(tiles[i:i+cols]+[np.zeros_like(tiles[0])]*(cols-len(tiles[i:i+cols]))) for i in range(0,len(tiles),cols)]
        cv2.imwrite(out,np.vstack(rows)); print(out,len(tiles))
    else:
        wav=sys.argv[4]; out=sys.argv[5]
        p=subprocess.Popen([FF,"-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r","60","-i","-","-i",wav,
            "-map","0:v","-map","1:a","-c:v","libx264","-preset","slow","-crf","16","-profile:v","high","-pix_fmt","yuv420p",
            "-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709","-g","30",
            "-c:a","aac","-b:a","256k","-movflags","+faststart",out],stdin=subprocess.PIPE)
        fi=0
        while True:
            ok,fr=cap.read()
            if not ok: break
            p.stdin.write(blur_frame(fr,active(tracks,fi)).tobytes()); fi+=1
        p.stdin.close(); p.wait(); print(out,fi,"frames")
