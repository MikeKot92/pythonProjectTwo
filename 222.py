
import cv2

img = cv2.imread('123.jpg')
imgR=cv2.resize(img,dsize=(img.shape[1]//8, img.shape[0]//8))
img0=cv2.cvtColor(imgR, cv2.COLOR_BGR2RGB)
img1=cv2.cvtColor(imgR, cv2.COLOR_BGR2HSV)
img2=cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(imgR, cv2.COLOR_BGR2HLS)
cv2.imshow('window0', img0)
cv2.imshow('window1', img1)
cv2.imshow('window2', img2)
cv2.imshow('window3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('new.jpg', img3)












