# Generated by Django 3.1.3 on 2020-11-20 20:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('identification_photo', models.ImageField(upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='FaceEncoding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_encode', models.CharField(max_length=10000000, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FacialRecognitionBackend.person')),
            ],
        ),
    ]
