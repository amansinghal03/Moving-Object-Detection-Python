import cv2
img = cv2.imread("python.png")
gusianblur = cv2.GaussianBlur(img , (21, 21),0)
cv2.imwrite("pythonblur.png",gusianblur)