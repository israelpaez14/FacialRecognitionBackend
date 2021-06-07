import base64
import cv2
import numpy as np


def convert_base64_to_cv2_image(base64_image):
    base64_image = str(base64_image).replace("data:image/jpeg;base64,", "")
    im_bytes = base64.b64decode(base64_image)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img
