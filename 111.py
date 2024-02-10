
import cv2
img=cv2.imread('123.jpg') #загружает картинку в виде матрицы
print(img)
cv2.imshow('window',img)#показывает картинку
#cv2.waitKey(2000) #ждать 2 сек
cv2.waitKey(0)#ждет нажатия на кнопку
cv2.destroyAllWindows()

#менять размер

print(img.dtype)
print(img.size)
print(img.shape)
print(img.data)
print(img.ndim)

imgResize=cv2.resize(img,dsize=(img.shape[1]//8, img.shape[0]//8)) #менять размер
cv2.imshow('window',imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()

#разворот картинки
imgv=cv2.flip(imgResize,1)
imgh=cv2.flip(imgResize,0)
imgvh=cv2.flip(imgResize,-1)
cv2.imshow('window0',imgv)
cv2.imshow('window1',imgh)
cv2.imshow('window2',imgvh)
cv2.waitKey(0)#ждет нажатия на кнопку
cv2.destroyAllWindows()
