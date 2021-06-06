from imutils import paths
import face_recognition
import pickle
import cv2
import os


def calculate_encodings_for_image(image_path, detection_mode, in_memory=True):
    if in_memory:
        image = image_path
    else:
        image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb_image, model=detection_mode)
    encodings = face_recognition.face_encodings(rgb_image, boxes)
    return encodings


def do_encode(dataset, encodings, detection_mode="cnn", in_memory=False):
    print("[INFO] quantifying faces")
    imagepaths = list(paths.list_images(dataset))
    known_encodings = []
    known_names = []

    for (i, imagePath) in enumerate(imagepaths):
        name = imagePath.split(os.path.sep)[-2]
        calculated_encodings = calculate_encodings_for_image(imagePath, detection_mode, in_memory)
        for encoding in calculated_encodings:
            known_encodings.append(encoding)
            known_names.append(name)
        data = {"encodings": known_encodings, "names": known_names}
        f = open(encodings, 'wb')
        f.write(pickle.dumps(data))
        f.close()
