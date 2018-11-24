import numpy as np
import math
from scipy import ndimage
from scipy import misc
import cv2


def getDist(v1, v2):
	ans = 0
	for i in range(3):
		ans += abs(v1[i] - v2[i])

	return ans

def isRed(v1):
	return getDist(v1, [133, 55, 50]) < 100

def process():
	img = misc.imread('test.png')
	n, m = img.shape[0], img.shape[1]

	ans = 0
	vis = n*[m*[0]]

	def valid(x, y):
		return x >= 0 and x < n and y >= 0 and y < m and isRed(img[x][y]) and vis[x][y] == 0

	def dfs(x, y):
		vis[x][y] = 1 
		tam = 1
		for i in range(-10, 10):
			for j in range(-10, 10):
				nx, ny = x + i, y + j
				if valid(nx, ny):
					tam += dfs(nx, ny)

		return tam

	for i in range(n):
		for j in range(m):
			if isRed(img[i][j]):
				if vis[i][j] == 0:
					sz = dfs(i, j)
					if sz >= 15:
						ans += 1

	result = open('number_dots.bin', 'wb')
	ret = bytearray([ans])
	result.write(ret)
	result.close()

def captureImg():
	cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
	if cap.isOpened() == False:
		cap.open()

	ret, frame = cap.read()
	if ret == True:
		cv2.imwrite('test.png', frame)

if __name__ == '__main__':
	while True:
		checker = open('flag.bin', 'rb')
		value = np.fromfile(checker, dtype = np.uint32)
		checker.close()
		if value == 1:
			captureImg()
			process()

