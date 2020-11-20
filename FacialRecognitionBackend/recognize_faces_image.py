import face_recognition
import argparse
import pickle
import cv2

from FacialRecognitionBackend.encode_faces import calculate_encodings_for_image
from FacialRecognitionBackend.models import FaceEncoding


def recognize_face(image_path, detection_mode, data=None):
    if data is None:
        data = {"encodings": []}
        face_encodings = FaceEncoding.objects.all()
        for face_encoding in face_encodings:
            face_enc = face_encoding.face_encode.replace("[", "").replace("]", "").replace("\n", "")
            data["encodings"].append(
                [float(number) for number in face_enc.split(" ") if number != ""])
    encodings = calculate_encodings_for_image(image_path, detection_mode)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"
        if True in matches:
            matches_indexes = [index for (index, boolean) in enumerate(matches) if boolean]
            counts = {}
            for i in matches_indexes:
                name = FaceEncoding.objects.all()[i].person.name
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        names.append(name)
    return names

