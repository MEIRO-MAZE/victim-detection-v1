import os
from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)
assert cap.isOpened(), 'Cannot capture source'  # Memastikan webcam dapat dibuka

model_path = "D:/Kuliah/Robotika/KRSRI Software/KRSRI LOMBA/RISET/YOLO_Object_detection_korban/Lib/runs/detect/train3/weights/best.pt"

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while True:
    ret, frame = cap.read()

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            # Calculate center of bounding box
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            cv2.circle(frame, (int(center_x), int(center_y)), 5, (0, 0, 255), -1)  # Draw center point

    cv2.imshow('YOLOv8 Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Tekan 'q' untuk keluar
        break

cap.release()
cv2.destroyAllWindows()