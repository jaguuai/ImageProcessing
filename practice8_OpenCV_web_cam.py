import cv2 as cv

#cameradan görüntü al
cap=cv.VideoCapture(0) #0 varsayılan kamera

while True:
    ret,frame=cap.read()

    if not ret:
        break
    cv.imshow("camera",frame)

    cv.waitKey(0)
    
cap.release()
cv.destroyAllWindows()