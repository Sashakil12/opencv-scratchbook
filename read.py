import cv2 as cv

# rescale


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# video
capture = cv.VideoCapture("cat-vidz/videoplayback (1).mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.5)

    cv.imshow('video',  frame)
    cv.imshow('video-resized',  frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
