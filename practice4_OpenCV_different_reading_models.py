import cv2 as cv
image_file='ForExpImg/apple.jpg'

img_color=cv.imread(image_file,1)
#img_color=cv.imread(image_file,cv.IMREAD_COLOR)
img_gray=cv.imread(image_file,0)
#img_gray=cv.imread(image_file,cv.IMREAD_GRAYSCALE)

cv.imshow("Color",img_color)
cv.imshow("Gray",img_gray)

cv.waitKey(0)
cv.destroyAllWindows