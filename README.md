# c-python-img-processing
Project that automaticly takes a picture from your webcam and count the number of black objects in it. The capture and processing parts are done in python, but the trigger for the photo is in the C code, as well as the final result!


RUNME:

1. Open two command prompts, in one of them compile and run 'server.c', and in the other run 'img_processing.py'.
2. Position your webcam in front of the black objects
3. In the C code, type 1 and press enter
4. Wait about 5 seconds
5. The result will be available for use in both C and Python codes


Libs used:

- Python-OpenCV
- Numpy
