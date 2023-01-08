import cv2

faceCascade = cv2.CascadeClassifier(r"D:\code_2023\opencv\haarcascade_frontalface_default.xml")
img = cv2.imread(r'D:\code_2023\opencv\lena.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(imggray,1.1,4)
#create bounding box
for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+h,y+h),(255,0,0),2)


cv2.imshow('result',img)
cv2.waitKey(0)