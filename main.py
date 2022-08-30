import cv2
# cap =cv2.VideoCapture('BP.mp4')
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")
# while True:
#     ret, frame=cap.read()
#     frame =cv2.resize(frame, None, fx=1, fy=1, interpolation =cv2.INTER_AREA)
#     cv2.imshow('Input', frame)
#     c=cv2.waitKey(1)
#     if c==27:
#         break
# cap.release()
# cv2.destroyAllWindows()

# cap=cv2.VideoCapture('bp.mp4')
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     cv2.waitKey(10)

cap=cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.waitKey(100)