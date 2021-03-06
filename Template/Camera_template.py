import numpy as np
import cv2

# name classifier
Bottles = cv2.CascadeClassifier('/home/pi/Opencv/haarcascade_frontalface_default.xml')

# name class
cap = cv2.VideoCapture(0)

# set Width
cap.set(3, 640)
# set Height
cap.set(4, 480)

while True:
    # import camera read into img
    # ret represents TRUE ot FALSE which means whether you get the image
    ret, img = cap.read()

    # image disposal
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # special features
    bottle = Bottles.detectMultiScale(
        img,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    # identify the object with frame
    for (x, y, w, h) in bottle:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display the camera window with title
    cv2.imshow('I am so tired!!', img)

    # close the window
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
