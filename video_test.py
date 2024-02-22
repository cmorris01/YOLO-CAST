"""
detection.py
~~~~~~~~~~~~

A module to implement the trained YOLOv8 model. Functionalities include individual predictions,
webcam intialization with real time object detection, etc. (as implentation is called for)

"""

#### Libraries
# Standard library
import os
import math
from collections import defaultdict
import typing

# Third party libaries
from ultralytics import YOLO
import cv2
import torch

class VideoTest:
    def __init__(self, video_path:str, model_path:str, threshold:float) -> None:
        self.video_path = video_path
        self.video_path_out = '{}_out.mp4'.format(video_path)
        self.model_path = model_path
        self.threshold = threshold

    def initialize_create_video(self) -> None:
        cap = cv2.VideoCapture(self.video_path)
        ret, frame = cap.read()
        if not ret:
            print("Failed to read video file.")
            cap.release()
            return
        H, W, _ = frame.shape
        out = cv2.VideoWriter(self.video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

        model = YOLO(self.model_path)

        while cap.isOpened():
            success, frame = cap.read()
            if success:
                results = model(frame, conf=self.threshold)
                annotated_frame = results[0].plot()  # Assuming this returns the correct annotated frame
                
                cv2.imshow("YOLOv8 Tracking", annotated_frame)
                out.write(annotated_frame)  # Save the annotated frame
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()  # Ensure to release the VideoWriter object
        cv2.destroyAllWindows()

def main():
    # paths
    video_path = '/Users/coymorris/Desktop/for_research/model_implementation/model_versions/car_test_2.mp4'
    model_path = '/Users/coymorris/Desktop/for_research/model_implementation/model_versions/exp1/exp1n.pt'
    threshold = 0.5

    # initialize object
    video_test = VideoTest(video_path, model_path, threshold)
    video_test.initialize_create_video()

main()




