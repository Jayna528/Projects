import cv2

video = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = video.read()
    cv2.imwrite('picture.jpg', frame)
    result = False

video.release()
cv2.destroyAllWindows()
    