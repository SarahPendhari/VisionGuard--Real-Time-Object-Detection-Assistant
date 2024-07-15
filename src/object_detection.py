import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        self.net = cv2.dnn.readNet("models/yolov3.weights", "config/yolov3.cfg")
        self.classes = []
        with open("config/coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def detect(self, frame):
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.net.getUnconnectedOutLayersNames())

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        detections = []
        for i in indices:
            if isinstance(i, (list, np.ndarray)):
                i = i[0]
            box = boxes[i]
            detections.append((class_ids[i], confidences[i], box))
        return detections

    def get_color(self, class_id):
        return tuple(map(int, self.colors[class_id]))

    def get_class_name(self, class_id):
        return self.classes[class_id]