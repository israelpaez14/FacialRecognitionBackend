import base64

from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    identification_photo = models.ImageField(upload_to="pictures")

    @property
    def base64(self):
        base64_data = base64.b64encode(self.identification_photo.read())
        return str(base64_data.decode("utf-8"))


class FaceEncoding(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    face_encode = models.CharField(validators=[validate_comma_separated_integer_list], max_length=10000000)
