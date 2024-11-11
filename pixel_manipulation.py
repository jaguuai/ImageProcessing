import cv2 as cv
import numpy as np

img=cv.imread("ForExpImg/apple.jpg")

#görüntü boyutunu değiştirme
height,width=img.shape[:2]
print("Width and height: ",width,height)

#beyaz kare
square_size=50

start_x=(width//2)-25
start_y=(height//2)-25

#kare olustur
for y in range (start_y,start_y+square_size):
    for x in range(start_x,start_x+square_size):
        img[y,x]=[255,255,255]