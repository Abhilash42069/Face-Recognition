import cv2
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
fe=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml')

while(1):
    r,i=v.read()
    print(i)
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j,1.3,7)
    face1=fe.detectMultiScale(j)
    print('number of ppl are', len(face))
                         
    print(face1)
    for(x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
    for(x,y,w,h) in face1:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('image',i)
    cv2.imshow('image1',j)
    k=cv2.waitKey(500) ###shouldnt be more than 50
    if(k==65):
        cv2.destroyAllWindows()
        v.release()
        break
