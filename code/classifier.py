import numpy as np
import cv2


ip = cv2.imread('1.jpg')
gray_ip = cv2.cvtColor(ip,cv2.COLOR_BGR2GRAY)

stop_cascade = cv2.CascadeClassifier('data/cascade.xml')

stop = stop_cascade.detectMultiScale(gray_ip, scaleFactor=1.3, minNeighbors =10, minSize=(75,75))
# add this
for (x,y,w,h) in stop:
  cv2.rectangle(ip,(x,y),(x+w,y+h),(255,255,0),2)
  cv2.imshow('img',ip)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break

cv2.destroyAllWindows()
