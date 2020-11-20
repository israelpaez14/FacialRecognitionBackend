
from django.contrib import admin
from django.urls import path

from FacialRecognitionBackend.api import register_person_from_image_array, recognize_person_from_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_person/', register_person_from_image_array),
    path('recognize_person/', recognize_person_from_image),

]
