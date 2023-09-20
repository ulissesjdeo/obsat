from imageai.Detection import ObjectDetection
from os import getcwd, remove
from os.path import join
from glob import glob


def analyze(file, timestamp):
    amount = 0
    runenv = getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(join(runenv, 'yolov3.pt'))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(
        input_image=join(runenv, file),
        output_image_path=join(runenv, f'photos/{timestamp}.{file.split(".")[-1]}'),
        minimum_percentage_probability=30
    )

    for obj in detections:
        if obj['name'] == 'person' or obj['name'] == 'umbrella':
            amount += 1  # amount.append(f"{obj['name']} with {obj['percentage_probability']}")
    return amount
