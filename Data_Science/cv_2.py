import cv2

path = r"C:\Users\HP PC\Pictures\Camera Roll\Rutherfordium-L.jpg"
img  = cv2.imread(path)

# resize image 
h, w, _ = img.shape
small_image = cv2.resize(img, (w//2, h//2)) #half size
cv2.imshow("Original", img)
cv2.imshow("current", small_image)

cv2.waitKey(0)


#Change Brightness
bright_img = cv2.add(small_image, 50)
bright_img = cv2.add(small_image, -50)
cv2.imshow("current", small_image)

cv2.waitKey(0)

# Image Flip
flip_img = cv2.flip(img, 1) #1 for horizontal image 
flip_img2 = cv2.flip(img, 0) #0 for verticle image 

# Stitch image
stitched_h_image = cv2.hconcat([img, flip_img, flip_img2])
stitched_v_image = cv2.vconcat([img, flip_img, flip_img2])


#Show image 
cv2.imshow("Original", stitched_h_image)
cv2.imshow("current", stitched_v_image)
cv2.waitKey(0)