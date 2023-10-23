import cv2
img=cv2.imread('p1.jpg',1)
cv2.line(img,(0,0),(630,400),(128,128,0),4)
cv2.rectangle(img,(15,15),(265,170),(0,128,128),6)
cv2.circle(img,(20,20),15,(0,128,0),-1)
cv2.circle(img,(255,163),15,(0,128,0),-1)
cv2.circle(img,(257,15),15,(0,128,0),-1)
cv2.circle(img,(15,165),15,(0,128,0),-1)
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'Hoooolaaa',(30,150),font,fontScale=1,color=(0,0,255))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
