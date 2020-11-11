import cv2 as cv
import numpy as np

img = cv.imread('cat-pics/cat-1.jpg')
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)
# cv.imshow("cat", img)

# paint image in certain color
blank[:] = 255, 0, 0
# cv.imshow("green", blank)
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('rect', blank)
# draw circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
# cv.imshow("circle", blank)
cv.line(blank, (0, 0),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow("line", blank)
cv.putText(blank, "I am text", (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 155), thickness=2)
cv.imshow("text", blank)
cv.waitKey(0)
