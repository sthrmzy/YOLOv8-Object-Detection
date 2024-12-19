from ultralytics import YOLO
import cv2

modelo = YOLO('yolov8x.pt')

ESC_KEY = 27

cap = cv2.VideoCapture(0)

cv2.namedWindow('trackbarWindow')

frame_nmr = -1
while True:
        frame_nmr += 1
        success, frame = cap.read()
        if not True:
                print("Falha ao capturar quadro")
                break

        detecoes = modelo(frame, verbose=False)[0]
        cv2.imshow('Detecções', detecoes.plot())

        if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == ESC_KEY:
                break

cap.release()
cv2.destroyAllWindows()
