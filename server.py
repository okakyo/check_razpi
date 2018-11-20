import socket,cv2,time
import numpy as np

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind('192.168.0.4',12345)

print('Ú‘±‘Ò‹@’†')
s.listen(1)
soc.addr=s.accept()

print(str(addr)+'‚ÆÚ‘±‚ªŠ®—¹‚µ‚Ü‚µ‚½B')

cam=cv2.VideoCapture(0)

while True:
    flag,img=cam.read()
    img=img.tostring()
    soc.send(img)
    k=cv2.WaitKey(1)
    if k==13:
        break
cam.release()
