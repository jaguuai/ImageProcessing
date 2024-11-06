import cv2 as cv
import numpy as np

#Giriş ve çıkış video
input_video=r"ForExpImg/25fps.mp4"
output_video=r"ForExpImg/output.mp4"

#video yakalama
cap=cv.VideoCapture(input_video)

#video özelliklerine bak
fourcc=cv.VideoWriter_fourcc(*"mp4v")  #Kodek
#kodek=cap.get(cv.CAP_PROP_FOURCC)
#KODEK encoder-decoderdan olusur. Video çözücüdür.
fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

out=cv.VideoWriter(output_video,fourcc,fps,(width,height)) #videomuzu belirtilen özelliklerde oluştur

while cap.isOpened():
    ret,frame=cap.read()

    if not ret: #okuma basarılı ise
        break
    
    b,g,r=cv.split(frame)
    
    brg_frame=cv.merge((b,r,g))
    cv.imshow("BRG video",brg_frame)

    out.write(brg_frame) #videoya yaz

    if cv.waitKey(1) & 0xFF == ord("q"): #q tusuna basıldıgında
        break

cap.release()
out.release()
cv.destroyAllWindows
