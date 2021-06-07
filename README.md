# FacialRecognitionBackend
Facial recognition implementation for Django backend, this repo will help you as a base project for your web-based facial recognition app.
## About the dependencies 
  The most of the dependencies should be installed easily, the only one that you could have problems is dlib,
  check how to install it on windows

## About the API

URL | Method | Parameters | Returns
----|------- | -------------
  /register_person|POST|**images**(It's a JSON array with the images in base64 without the prefix), **name**(The name of the person to register) | A json if its ok
  /recognize_person|POST|**image**(Base64 Enconded image to recognize)| A JSON with the name of the person
