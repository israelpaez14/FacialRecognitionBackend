# FacialRecognitionBackend
Facial recognition implementation for Django backend, this repo will help you as a base project for your web-based facial recognition app.
## About the dependencies 
  The most of the dependencies should be installed easily, the only one that you could have problems is dlib,
  check how to install it on windows
## How to run the app 
  You can use docker to run the application without messing with dblib in windows, all the docker image configurations is done, all you need to do is :<br>
  docker image build -t bakend .<br>
  docker-compose up -d
 

## About the API

URL | Method | Parameters | Returns
----|------- | -----------|---------
  /register_person|POST|**images**(It's a JSON array with the images in base64 without the prefix), **name**(The name of the person to register) | A json if its ok
  /recognize_person|POST|**image**(Base64 Enconded image to recognize)| A JSON with the name of the person {"name":"Israel"}
  /login|POST|**username**(Django username), **password**(Django password)| A JSON with the login status {"result":"Success"}
  /logout|GET|**NO PARAMETERS**| A JSON with the logout status {"result":"Success"}
  /api/people/|GET|**NO PARAMETERS**| A JSON Array with the registered people

