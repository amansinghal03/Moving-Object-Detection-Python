import cv2
img = cv2.imread("python.png")
grayimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
theres = cv2.threshold(grayimg , 40, 200, cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold6.png",theres)