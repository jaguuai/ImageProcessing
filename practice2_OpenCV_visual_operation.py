import cv2 as cv

#gorselı matrix ile okuma
img=cv.imread("ForExpImg/chess.jpg")
print(img)
#gorselin belırlı kısmını matrix ile okuma
print(img[300:400,:])
#matrixten gorsele cevirme
cv.imshow("Chess",img)
cv.waitKey(0)
cv.destroyAllWindows
