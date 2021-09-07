import numpy as np
import cv2
from skimage.color import gray2rgb

# name path
Class_path = '/home/pi/Rubbish_Recycle_Robot_CV/Xml/8.29_Generation_Three/cascade8.29.xml'

# name classifier
Bottle = cv2.CascadeClassifier(Class_path)

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
    # print("img", img.shape)

    final_img = np.zeros(img.shape, dtype='uint8')
    process_img = np.zeros(img.shape, dtype='uint8')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower=np.array([35,43,46])
    upper=np.array([77,255,255])
 
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    
    image_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    bottle = Bottle.detectMultiScale(
        image_gray,
        scaleFactor = 1.2,
        minNeighbors = 20,
        minSize = (20, 20),
        maxSize = (160,160)
    )

    # identify the object with frame
    for (x, y, w, h) in bottle:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display the camera window with title
    # cv2.imshow('I am so tired!!', hueMask)
    cv2.imshow("test", img)
    # print("image_gray", image_gray.shape)

    # close the window
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
