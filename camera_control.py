import cv2
import os
import threading
import timer
import sys

def shot_img():
    global num
    success, frame = cameraCapture.read()
    path = "D:\jupyter\美的校企赛\camera_buffer\\"
    directory = path
    
    if num == 0:
        os.chdir(directory)
    
    cv2.imwrite( f'{num}' + '.jpg', frame)
    print(num)
    num += 1
    if num==10:
        cameraCapture.release()
        cv2.destroyAllWindows()
        sys.exit()
    timer = threading.Timer(1, shot_img)
    timer.start()

if __name__ == '__main__':
    num=0
    cameraCapture = cv2.VideoCapture(0)
    timer = threading.Timer(1,shot_img)
    timer.start()