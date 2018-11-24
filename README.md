# C-Python-img-processing
Project that automaticly takes a picture from your webcam and count the number of red dots in it. The coolest part, is that the capture and processing parts are done in python, but the trigger for the photo is in the C code, as well as the final result!


RUNME:

1. Open to command prompts, in one of them compile and run 'server.c', and in the other run 'img_processing.py'.
2. Position your webcam in front of the red dots
3. In the C code, type 1 and press enter
4. Wait about 5 seconds
5. Profit!


Libs used:

- Python-OpenCV
- Scipy
- Numpy
