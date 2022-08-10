import cv2

video = cv2.VideoCapture(0)     # 0 = wbcam,  #1 = for USB Camera 

while video.isOpened():
    status, img = video.read()
    if status:

        cv2.imshow('video', img)

        if cv2.waitKey(1) == 27:
            break
    else:
        
        print('video ended')  
        break   # 27 is esc key

video.release()
cv2.destroyAllWindows