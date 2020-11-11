import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


image = cv.imread('cat-pics/cat-1.jpg')
img = rescaleFrame(image, .09)
# cv.imshow("Cat", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
# how o blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)
canny = cv.Canny(blur, 125, 125)
cv.imshow('canny', canny)
# @dialating the image

dilated = cv.dilate(canny, (3, 3), iterations=5)

cv.imshow('dialated', dilated)

eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

resized = cv.resize(image, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)
cropped = img[50:200, 200:400].git
cv.imshow("cropped", cropped)
cv.waitKey(0)
