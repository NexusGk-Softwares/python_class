#NexusGK___Softwares
import cv2
url1 = "http://10.10.14.193:8080/video"
cap = cv2.VideoCapture(url1)
while(cap.isOpened()):
    camera, frame = cap.read()
    try:
        cv2.imshow('Imagen',
                   cv2.resize(
                       frame,(600,400)))
        key = cv2.waitKey(1)
        if key== ord('q'):
            break
    except cv2.error:
        print("end")
        break
cv2.destroyAllWindows()