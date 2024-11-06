import cv2 as cv

img_bgr=cv.imread("ForExpImg/apple.jpg")

#orjinal resmi göster ve renk kanallarını ayır
cv.imshow("Red Apple",img_bgr)
b,g,r=cv.split(img_bgr)

#kırmızı ve yesil kanalları birleştir
img_new=cv.merge((b,r,g))

#yesil renkli elmayı göster
cv.imshow("Green Apple",img_new)



#bu uygulamada renk kanallarını degıstırmenın uzerınde duruldu
#Eger sarı renk isteseydik b,r,r yapabilirdik Ton ayarı için b,r-20,r gibi kombınasonlar denenebilir

img_chess=cv.imread("ForExpImg/chess.jpg")
bc,gc,rc=cv.split(img_chess)

blue_chess=cv.merge((rc,gc,bc))
cv.imshow("Blue Chess",blue_chess)
cv.imshow("Blue Chanel",bc)
cv.imshow("Green Chanel",gc)
cv.imshow("Red Chanel",rc)

#Kanal degeri varsa 1 yoksa 0 . 0 oldugunda siyah 1 oldugunda ıse beyaz gosterıcek
cv.imwrite("ForExpImg/blue_chess.jpg",blue_chess)
cv.waitKey(0)




cv.destroyAllWindows