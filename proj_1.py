import cv2
import numpy as np

#orange=5,107,0  max-19,255,255
cap=cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height
cap.set(10,150)#brightness

mycolors=[[5,107,0,19,255,255],#orange
          [133,56,0,159,156,255],#purple
          [57,76,0,100,255,255]]#green
mycolorValues=[[255,153,51],
               [255,0,255],
               [0,255,0]]


mypoints=  [] #[x,y,colorID]
def findcolor(img,mycolors,mycolorValues):
       imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
       count=0
       newPoints=[]
       for color in mycolors:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(color[0]),mask)
        x,y=getContours(mask)
        cv2.circle(imageresult,(x,y),10,mycolorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
       return  newPoints
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imageresult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y
def drawoncanvas(mypoints,mycolorValues):
    for point in mypoints:
        cv2.circle(imageresult, (point[0],point[1]), 10, mycolorValues[point[2]], cv2.FILLED)

while True:
    success,img=cap.read()
    imageresult=img.copy()
    newPoints= findcolor(img,mycolors,mycolorValues)
    if len(newPoints)!=0:
        for newp in newPoints:
            mypoints.append(newp)
    if len(mypoints)!=0:
        drawoncanvas(mypoints,mycolorValues)

    cv2.imshow("Video:",imageresult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break