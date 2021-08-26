import numpy as np
import cv2

path = "/home/pi/BackUp/Database/negative/"
for i in range(1, 2401):
    print(path + str(i) + '.jpg')
    img = cv2.imread(path+str(i)+'.jpg', cv2.IMREAD_GRAYSCALE)
    img5050 = cv2.resize(img, dsize=(25, 25))
    #cv2.imshow("img", img5050)
    cv2.waitKey(1)
    cv2.imwrite('/home/pi/Opencv/Database/neg/'+str(i)+'.jpg', img5050)
