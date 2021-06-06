import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer

from FacialRecognitionBackend.models import Person


class PersonSerializer(ModelSerializer):
    b64 = serializers.CharField(source="base64", read_only=True)

    class Meta:
        model = Person
        fields = '__all__'

# Custom image field - handles base 64 encoded images
