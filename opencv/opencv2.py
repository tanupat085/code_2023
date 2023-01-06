import cv2
import numpy as np

img = cv2.imread(r"D:\code_2023\opencv\card.jpg")

width , height = 250,350 #แล้วแต่จะตั้งเลย
pt1 = np.float32([[225,91],[433,139],[162,387],[369,431]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgout = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("matrix",matrix)
cv2.imshow("imgout",imgout)
cv2.waitKey(0)