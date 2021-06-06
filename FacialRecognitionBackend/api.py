import json
import os

import cv2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from FacialRecognitionBackend.add_face_to_database import register_face
from FacialRecognitionBackend.helper_functions import convert_base64_to_cv2_image
from FacialRecognitionBackend.recognize_faces_image import recognize_face


@csrf_exempt
def register_person_from_image_array(request):
    body = json.loads(request.body)
    images = body["images"]
    person_name = body["name"]
    save_path = "dataset/" + str(person_name).replace(" ", "_")
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    for idx, frame in enumerate(images):
        cv2.imwrite(save_path + "/" + person_name + str(idx) + ".jpg", convert_base64_to_cv2_image(frame))

    register_face(save_path)
    return HttpResponse("Done")


@csrf_exempt
def recognize_person_from_image(request):
    body = json.loads(request.body)
    print(body)
    image = body["image"]
    image = image[2:]
    image = image[:-1]
    print(image)
    names = recognize_face(convert_base64_to_cv2_image(image), "hog")
    print(names)
    return HttpResponse(names)
