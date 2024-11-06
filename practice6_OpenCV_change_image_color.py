import cv2 as cv

img_bgr=cv.imread("ForExpImg/apple.jpg")

#orjinal resmi göster ve renk kanallarını ayır
cv.imshow("Red Apple",img_bgr)
b,g,r=cv.split(img_bgr)

#kırmızı ve yesil kanalları birleştir
img_new=cv.merge((b,r,g))

#yesil renkli elmayı göster
cv.imshow("Green Apple",img_new)

cv.waitKey(0)
cv.destroyAllWindows

