import cv2
import numpy as np

im = cv2.imread(r"C:\Users\HP PC\Pictures\Camera Roll\Rutherfordium-L.jpg")

if im is None:
    print('Image not found')
else:

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_inv = cv2.bitwise_not(im_gray)
    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    im_lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB)
    im_xyz = cv2.cvtColor(im, cv2.COLOR_RGB2XYZ)

    cv2.imshow("111",im_gray)
    cv2.imshow("112", im_inv)
    cv2.imshow("113",im_rgb)
    cv2.imshow("1114",im_hsv)
    cv2.imshow("1115",im_lab)
    cv2.imshow("1116",im_xyz)

    #save

    cv2.imwrite('111_bw.jpg',im_gray)
    cv2.imwrit("111.jpg",im_gray)
    cv2.imwrit("112.jpg", im_inv)
    cv2.imwrit("113.jpg",im_rgb)
    cv2.imwrit("1114.jpg",im_hsv)
    cv2.imwrit("1115.jpg",im_lab)
    cv2.imwrit("1116.jpg",im_xyz)


# for image show 
    #print("Image Found")
    #cv2.imshow('cosmere', im)
    #cv2.waitKey(0)          # K is capital


