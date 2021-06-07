import json
import os

import cv2
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from FacialRecognitionBackend.add_face_to_database import register_face
from FacialRecognitionBackend.helper_functions import convert_base64_to_cv2_image
from FacialRecognitionBackend.models import Person
from FacialRecognitionBackend.recognize_faces_image import recognize_face
from FacialRecognitionBackend.serializers import PersonSerializer


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
    image = str(image).replace("data:image/jpeg;base64,", "")
    print(image)
    names = recognize_face(convert_base64_to_cv2_image(image), "hog")
    print(names)
    return JsonResponse({"name": names[0] if len(names) > 0 else "Unknown"}, safe=True, status=200)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
