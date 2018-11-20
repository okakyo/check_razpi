import socket,cv2
import numpy as np

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.connect("192.168.0.4",12345)

print("ê⁄ë±äÆóπ")

while True:
    data=soc.recv(921600)
    data=np.fromstring(data,dtype=uint8)
    data=np.reshape(480,640,3)
    v2.imshow("",data)
    k=cv2.WaitKey(1)
    if k==13:
        break

cv2.destroyAllWindows()
