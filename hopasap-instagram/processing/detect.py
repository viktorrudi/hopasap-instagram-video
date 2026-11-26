import sys, json, cv2
from ultralytics import YOLO
model = YOLO(sys.argv[1]); src = sys.argv[2]; out = sys.argv[3]
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS); res = []; i = 0
while True:
    ok, fr = cap.read()
    if not ok: break
    r = model.predict(fr, imgsz=1280, conf=0.12, device="mps", verbose=False)[0]
    res.append([[*map(float, b.xyxy[0].tolist()), float(b.conf[0])] for b in r.boxes])
    i += 1
json.dump({"fps": fps, "frames": res}, open(out, "w"))
print(src, i, "frames,", sum(1 for f in res if f), "with detections")
