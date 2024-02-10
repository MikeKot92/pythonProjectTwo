
import cv2
cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('123.jpg')
imgResize=cv2.resize(img,dsize=(img.shape[1]//8, img.shape[0]//8))
cv2.imshow('window', imgResize)
cv2.waitKey(0)
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
cv2.imshow('window', imgGray)
cv2.waitKey(0)
result=cascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=1)
print(result)
for (x,y,w,h) in result:
    cv2.rectangle(imgResize,(x,y), (x+w,y+h), color=(255,0,0), thickness=2)
cv2.imshow('window', imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()