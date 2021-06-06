import os
from imutils import paths
from .encode_faces import calculate_encodings_for_image
from .models import FaceEncoding, Person


def register_face(image_folder):
    print("[INFO] quantifying faces")
    imagepaths = list(paths.list_images(image_folder))

    for (i, imagePath) in enumerate(imagepaths):
        print("[INFO] Processing image {}/{}".format(i + 1, len(imagepaths)))
        name = imagePath.split(os.path.sep)[-2]
        calculated_encodings = calculate_encodings_for_image(imagePath, 'hog', False)

        for encoding in calculated_encodings:
            person = Person.objects.filter(name=name).first()
            if person is None:
                person = Person(name=name, identification_photo=imagePath)
                person.save()

            face_encoding = FaceEncoding(person=person, face_encode=encoding)
            face_encoding.save()

    return True
