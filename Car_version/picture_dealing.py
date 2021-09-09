import numpy as np
import cv2

path = "/home/pi/Opencv/Green_Bottle_new/"
for i in range(1,100):
    img= cv2.imread(path + str(i) + '.jpg')
    final_img = np.zeros(img.shape, dtype='uint8')
    process_img = np.zeros(img.shape, dtype='uint8')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([35, 43, 46])
    upper = np.array([77, 255, 255])
    mask = cv2.inRange(hsv, lower,upper)
    res = cv2.bitwise_and(img, img, mask=mask)
    image = cv2.resize(res, dsize=(25, 25))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.waitKey(1)
    print(i,".jpg")
    cv2.imwrite('/home/pi/Opencv/Green_Bottle_old/'+str(i)+'.jpg', image_gray)



