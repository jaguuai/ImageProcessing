import cv2 as cv

#gorselı matrix ile okuma
img=cv.imread("ForExpImg/apple.jpg")
#gorsel hakkında bilgi alma(h,w,channel count)
print(img.shape)
height,width=img.shape[:2]
print(height,width)

channels=img.shape[2]
print(f'Kanal sayisi:',channels)
print(f'Yüksekligi:{img.shape[0]}')
print("Veri tipi:",img.dtype)