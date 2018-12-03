import cv2 as cv
import numpy as np

def process(frame):
	if frame is None:
		return -1

	cv.imwrite('before.png', frame) #just saving the image for debugging purposes
	frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #transforming to HSV format
	ft = cv.inRange(frame_HSV, (0, 0, 0), (180, 255, 10)) #using treshold in image, only pixels in range will appear white

	kernel = np.ones((5,5),np.uint8) #kernel of transformation
	ft = cv.morphologyEx(ft, cv.MORPH_OPEN, kernel) #opennig image, removing background noise
	ft = cv.morphologyEx(ft, cv.MORPH_CLOSE, kernel) #closing image, filling small holes
	
	cv.imwrite('after.png', ft) #just saving transformed image for debugging purposes
	im2, contours, hierarchy = cv.findContours(ft, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #counting number of countours
	return len(contours)


def captureImg():
	cap = cv.VideoCapture(0)

	if cap is None:
		return None

	ret, frame = cap.read()
	if ret is False:
		return None

	return frame


if __name__ == '__main__':
	img = captureImg()
	print(process(img))
