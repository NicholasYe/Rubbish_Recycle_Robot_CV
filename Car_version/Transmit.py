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
    # print("img", img.shape)

    # image disposal
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # image_green = detectHSColor(img, [35,0,0], [77,255,255], [0,43,0], [255,255,255])

    # lower_blue=np.array([35,43,0])
    # upper_blue=np.array([77,255,255])
    # frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # mask_blue=cv2.inRange(frame,lower_blue,upper_blue)
    # res_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
    # res_blue=cv2.cvtColor(res_blue,cv2.COLOR_HSV2BGR)

    # output_img = np.zeros(img.shape, dtype='uint8')
    final_img = np.zeros(img.shape, dtype='uint8')
    process_img = np.zeros(img.shape, dtype='uint8')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print("hsv", hsv.shape)

    channels = cv2.split(hsv)
    # print("channels", channels[0].shape)

    retval1, mask1 = cv2.threshold(channels[0], 77, 255, cv2.THRESH_BINARY_INV)
    retval2, mask2 = cv2.threshold(channels[0], 35, 255, cv2.THRESH_BINARY)
    # print("mask1", mask1.shape)

    # hueMask = cv2.add(mask1, mask2)
    hueMask = mask1 & mask2
    # print("hueMask", hueMask.shape)
    # output_img[:,:,0] = hueMask

    satMask = cv2.inRange(channels[1], 43, 255)
    # print("satMask", satMask.shape)
    # output_img[:,:,1] = satMask
    # print("output_img", output_img.shape)

    # mask = cv2.add(hueMask, satMask)
    # mask = hueMask + satMask
    # print("mask", mask.shape)
    process_img[:,:,0] = (hueMask & satMask)
    # img.copyTo(final_img, process_img)
    

    # out_img = gray2rgb(mask)
    # print("out_img", out_img.shape)

    # image_process = img.copyTo(image_green)
    image_gray = cv2.cvtColor(final_img, cv2.COLOR_BGR2GRAY)
    # print("image_gray", image_gray.shape)

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
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # display the camera window with title
    cv2.imshow('I am so tired!!', hueMask)
    cv2.imshow("test", image_gray)


    # close the window
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
