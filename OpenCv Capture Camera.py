import numpy as np
import cv2
import time
import os

class Camera :
    def __init__(self,cam_id,imgpath):
        print("kamera çalışıyor")
        self.cap=cv2.VideoCapture(0)
        self.path=imgpath

    def __del__(self):
        print("kamera kapalı")
        cv2.destroyAllWindows()

    def is_opened(self):
        return self.cap.isOpened()

    def read_frame(self):
        ret,frame=self.cap.read()
        if ret==False:
            print("Kamera bulunamadı !")
        return frame

    def save_to_file(self,filename):
        print(filename)
        cv2.imwrite(self.path+filename,frame)
                

fotodir=os.path.dirname(os.path.abspath(__file__))
fotodir=fotodir+"/ttss/"
        
cam1=Camera(0,fotodir)

while cam1.is_opened():

    frame=cam1.read_frame()

    timenow=time.time()
    timestr=str(timenow)+".jpg"
    print(timestr)

    cam1.save_to_file(timestr)
    cv2.imshow("Kayıt Ekranı...",frame)
    

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

    
