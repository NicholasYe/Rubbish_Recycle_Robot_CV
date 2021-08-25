import numpy as np
import cv2
import sys
import math

if __name__ == "__main__":
    image = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)
    h, w = image.shape
    src = np.array([[0,0], [w-1,0], [0,h-1], [w-1,h-1]], np.float32)
    dst = np.array([[50,50], [w/3,50], [50,h-1], [w-1,h-1]], np.float32)
    p = cv2.getPerspectiveTransform(src,dst)
    r = cv2.warpPerspective(image, p, (w,h), borderValue=125)
    cv2.imshow("image", image)
    cv2.imshow("warpPerspective", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()