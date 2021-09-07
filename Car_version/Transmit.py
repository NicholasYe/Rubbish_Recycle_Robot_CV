import numpy as np
import cv2
from skimage.color import gray2rgb

# def detectHSColor(in_image, minHue, maxHue, minSat, maxSat):
#     hsv = cv2.cvtColor(in_image, cv2.COLOR_BGR2HSV)
#     channels = cv2.split(hsv)
#     mask1 = cv2.threshold(channels[0], maxHue, 255, cv2.THRESH_BINARY_INV)
#     mask2 = cv2.threshold(channels[0], minHue, 255, cv2.THRESH_BINARY)
#     if minHue < maxHue :
#         hueMask = mask1 & mask2
#     else :
#         hueMask = mask1 | mask2
#     satMask = cv2.inRange(channels[1], minSat, maxSat)
#     mask = hueMask & satMask
#     return mask

# def detectHSColor(in_image):
#     lower_blue=np.array([35,43,50])
#     upper_blue=np.array([77,255,255])
#     img1=in_image
#     frame=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#     mask_blue=cv2.inRange(frame,lower_blue,upper_blue)
#     res_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
#     res_blue=cv2.cvtColor(res_blue,cv2.COLOR_HSV2BGR)
#     return res_blue

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

    # image disposal
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # image_green = detectHSColor(img, [35,0,0], [77,255,255], [0,43,0], [255,255,255])

    # lower_blue=np.array([35,43,0])
    # upper_blue=np.array([77,255,255])
    # frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # mask_blue=cv2.inRange(frame,lower_blue,upper_blue)
    # res_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
    # res_blue=cv2.cvtColor(res_blue,cv2.COLOR_HSV2BGR)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    channels = cv2.split(hsv)
    retval1, mask1 = cv2.threshold(channels[0], 77, 255, cv2.THRESH_BINARY_INV)
    retval2, mask2 = cv2.threshold(channels[0], 35, 255, cv2.THRESH_BINARY)
    # hueMask = cv2.add(mask1, mask2)
    hueMask = mask1 + mask2
    satMask = cv2.inRange(channels[1], 43, 255)
    # mask = cv2.add(hueMask, satMask)
    mask = hueMask + satMask
    out_img = gray2rgb(mask)

    # image_process = img.copyTo(image_green)
    image_gray = cv2.cvtColor(out_img, cv2.COLOR_BGR2GRAY)

    # special features
    bottle = Bottle.detectMultiScale(
        image_gray,
        scaleFactor = 1.2,
        minNeighbors = 20,
        minSize = (20, 20),
        maxSize = (160,160)
    )

    # identify the object with frame
    for (x, y, w, h) in bottle:
        cv2.rectangle(image_gray, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display the camera window with title
    cv2.imshow('I am so tired!!', image_gray)

    # close the window
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
