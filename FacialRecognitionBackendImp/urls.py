from django.contrib import admin
from django.urls import path

from FacialRecognitionBackend.api import register_person_from_image_array, recognize_person_from_image
from FacialRecognitionBackend.views import login_endpoint, main, logout_endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_person/', register_person_from_image_array),
    path('recognize_person/', recognize_person_from_image),
    path('login/', login_endpoint),
    path('logout/', logout_endpoint),
    path('main/', main),

]
