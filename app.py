import cv2
from ultralytics import YOLO

# Load model YOLO
model = YOLO('model/yolo11s.pt')

# Realize image prediction / Save and show results (save = True)
results = model(
    "video/laboratorio_trombetta.mp4", 
    show=True, 
    save=True,
    imgsz=640  # <-- Define larg size of the image
)
