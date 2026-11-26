import json, sys, numpy as np
def iou(a,b):
    x1,y1=max(a[0],b[0]),max(a[1],b[1]); x2,y2=min(a[2],b[2]),min(a[3],b[3])
    i=max(0,x2-x1)*max(0,y2-y1); u=(a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-i
    return i/u if u>0 else 0
def ok(b):
    w,h=b[2]-b[0],b[3]-b[1]
    return b[4]>=0.15 and h<=330 and w<=700 and w>=20
def build(frames, ext=8, gap=14, minlen=8):
    tracks=[]
    for fi,boxes in enumerate(frames):
        for b in sorted([b for b in boxes if ok(b)], key=lambda b:-b[4]):
            best=None;bs=0
            for t in tracks:
                lf,lb=t["f"][-1],t["b"][-1]
                if fi-lf>gap or lf==fi: continue
                cx=( (b[0]+b[2])-(lb[0]+lb[2]) )/2; cy=((b[1]+b[3])-(lb[1]+lb[3]))/2
                d=np.hypot(cx,cy)/max(40,(lb[2]-lb[0]))
                s=iou(b,lb)+ (1-min(d,1))*0.6
                if s>bs and (iou(b,lb)>0.05 or d<0.9): best,bs=t,s
            if best: best["f"].append(fi); best["b"].append(b[:4]); best["c"].append(b[4])
            else: tracks.append({"f":[fi],"b":[b[:4]],"c":[b[4]]})
    out=[]
    n=len(frames)
    for t in tracks:
        if len(t["f"])<minlen or max(t["c"])<0.4: continue
        f=np.array(t["f"]); B=np.array(t["b"],float)
        full=np.arange(f[0],f[-1]+1)
        I=np.stack([np.interp(full,f,B[:,k]) for k in range(4)],1)
        # gaussian smooth (sigma 2.5 frames), edge-padded
        k=np.exp(-0.5*(np.arange(-8,9)/2.5)**2); k/=k.sum()
        P=np.pad(I,((8,8),(0,0)),mode="edge")
        Sm=np.stack([np.convolve(P[:,j],k,mode="valid") for j in range(4)],1)
        # extend ends by `ext` frames using last velocity (damped)
        v0=Sm[min(3,len(Sm)-1)]-Sm[0]; v0/=max(1,min(3,len(Sm)-1))
        v1=Sm[-1]-Sm[max(0,len(Sm)-4)]; v1/=max(1,min(3,len(Sm)-1))
        pre=[Sm[0]-v0*(i+1) for i in range(ext)][::-1]; post=[Sm[-1]+v1*(i+1) for i in range(ext)]
        start=full[0]-ext; allb=np.vstack([pre,Sm,post]) if len(pre) else Sm
        fr=np.arange(start,start+len(allb)); keep=(fr>=0)&(fr<n)
        out.append({"start":int(fr[keep][0]),"boxes":allb[keep].round(1).tolist(),"n":len(t["f"])})
    return out
d=json.load(open(sys.argv[1])); tr=build(d["frames"])
json.dump({"fps":d["fps"],"tracks":tr},open(sys.argv[2],"w"))
for t in tr: print(sys.argv[1], "frames %d-%d (%.2f-%.2fs) dets=%d"%(t["start"],t["start"]+len(t["boxes"])-1,t["start"]/60,(t["start"]+len(t["boxes"])-1)/60,t["n"]))
