# coding: utf-8
import cv2
# Load a color image 
img = cv2.imread('messi5.jpg')
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
pass