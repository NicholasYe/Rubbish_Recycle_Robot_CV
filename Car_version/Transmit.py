import numpy as np
import cv2

def detectHSColor(in_image, minHue, maxHue, minSat, maxSat):
    hsv = cv2.cvtColor(in_image, code = cv2.COLOR_BGR2HSV)
    
    channels = np.array(Zero_array)
    cv2.split(hsv, channels)
    mask1 = cv2.threshold(channels[0], maxHue, 255, type = cv2.THRESH_BINARY_INV)
    mask2 = cv2.threshold(channels[0], minHue, 255 ,typr = cv2.THRESH_BINARY)
    if minHue < maxHue :
        hueMask = mask1 & mask2
    else :
        hueMask = mask1 | mask2
    satMask = cv2.inRange(channels[1], minSat, maxSat)
    mask = hueMask & satMask
    return mask

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
    image_green = detectHSColor(img, 35, 77, 43, 255)
    image_process = img.copyTo(image_green)
    image_gray = cv2.cvtColor(image_process, cv2.COLOR_BAYER_BG2GRAY)

    # special features
    bottle = Bottle.detectMultiScale(
        image_gray,
        scaleFactor=1.2,
        minNeighbors=20,
        minSize=(20, 20),
        maxSize=(160,160)
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
