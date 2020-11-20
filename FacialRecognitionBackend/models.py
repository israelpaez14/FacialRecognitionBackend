from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    identification_photo = models.ImageField(upload_to="pictures")


class FaceEncoding(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    face_encode = models.CharField(validators=[validate_comma_separated_integer_list], max_length=10000000)


