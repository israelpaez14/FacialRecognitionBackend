from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os


def calculate_encodings_for_image(image_path, detection_mode, in_memory=True):
    print()
    if in_memory:
        image = image_path
    else:
        image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb_image, model=detection_mode)
    encodings = face_recognition.face_encodings(rgb_image, boxes)
    return encodings


def do_encode(dataset, encodings, detection_mode="cnn", in_memory=False):
    print("[INFO] quantifying faces")
    imagepaths = list(paths.list_images(dataset))
    known_encodings = []
    known_names = []

    for (i, imagePath) in enumerate(imagepaths):
        print("[INFO] Processing image {}/{}".format(i + 1, len(imagepaths)))
        name = imagePath.split(os.path.sep)[-2]
        calculated_encodings = calculate_encodings_for_image(imagePath, detection_mode, in_memory)
        for encoding in calculated_encodings:
            known_encodings.append(encoding)
            known_names.append(name)
        print("[INFO] Serializing objects")
        data = {"encodings": known_encodings, "names": known_names}
        f = open(encodings, 'wb')
        f.write(pickle.dumps(data))
        f.close()


# if __name__ == '__main__':
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-i", "--dataset", required=True)
#     ap.add_argument("-e", "--encodings", required=True)
#     ap.add_argument("-d", "--detection-mode", type=str, default="cnn")
#     args = vars(ap.parse_args())
#     do_encode(args["dataset"], args["encodings"], False)
