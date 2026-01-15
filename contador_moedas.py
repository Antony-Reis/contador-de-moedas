import cv2
from ultralytics import YOLO

model = YOLO(r"contador-de-moedas\yolo_runs\moedas2\weights\best.pt")

cap = cv2.VideoCapture(0)



while True:
    valor = 0.0
    rec, frame = cap.read()
    if not rec:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    arestas = cv2.Canny(blur, 50, 150, apertureSize=3)

    h, w = frame.shape[:2]

    results = model.predict(frame, conf=0.2, verbose=False)
    if results[0] is not None:
        for box in results[0].boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])


            label = model.names[cls]

            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.putText(frame,f'{label} Conf: {conf:.2f}',(x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)


            dc = {'1 real':1, '25 cents':0.25, '50 cents':0.5}
            valor += dc[label]

    cv2.rectangle(frame,(w-160,20),(w-40,45),(255,0,0),-1)
    cv2.putText(frame, f'R${valor:.2f}', (w - 150, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)



    cv2.imshow('frame',frame)
    cv2.imshow('arestas',arestas)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
