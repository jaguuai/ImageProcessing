import cv2 as cv

#kamera baslat
cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if not ret:
        break
    #gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hsv_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #hls_img=cv.cvtColor(frame,cv.COLOR_BGR2HLS)
    #rgba_img=cv.cvtColor(frame,cv.COLOR_BGR2RGBA)
    #rgb_img=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
    #Görüntüyü yatay-->1 ve dikey->0 cevir ters->-1 cevirme
    flipped_img=cv.flip(frame,0)


    cv.imshow("camera",flipped_img)

    if cv.waitKey(1) & 0xFF==ord("q"):
        break

#kamerayı kapat
cap.release()
cv.destroyAllWindows()