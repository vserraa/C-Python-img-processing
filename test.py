import cv2 as cv

def valid(x, y):
	return x >= 0 and x < n and y >= 0 and y < m and vis[x][y] == 0 and ft[x][y] > 0


def dfs(x, y):
	vis[x][y] = 1 
	tam = 1
	for i in range(-5, 6):
		for j in range(-5, 6):
			nx, ny = x + i, y + j
			if valid(nx, ny):
				tam += dfs(nx, ny)

	return tam

#cap = cv.VideoCapture(0)

frame = cv.imread('test.png')
n, m = frame.shape[0], frame.shape[1]
frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
ft = cv.inRange(frame_HSV, (0, 0, 0), (180, 255, 5))
cv.imwrite('transform.png', ft)

im2, contours, hierarchy = cv.findContours(ft, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

print('------------------')

vis = n*[m*[0]]
ans, tresh = 0, 20
for i in range(n):
	for j in range(m):
		if not vis[i][j] and ft[i][j] > 0:
			tam = dfs(i, j)
			print('(%d, %d) = %d' %(i, j, tam))
			if tam >= tresh:
				ans += 1

print('ans = %d' %ans)
