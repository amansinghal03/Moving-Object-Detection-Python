import cv2
img = cv2.imread("python.png")
grayimg = cv2.cvtColor(img , cv2.COLOR_BayerRG2GRAY)
theres = cv2.threshold(grayimg , 200, 225, cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold.png",theres)
