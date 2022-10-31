import cv2
import  numpy
import sqlite3
import os

def insertOrUpDate(id,name,age,gender) :
    conn = sqlite3.connect('D:\\1\\Data.db')

    query = "Select * from  People Where  ID= " +str(id)

    cursor = conn.execute(query)

    isRecordExist = 0

    for row in cursor :
        isRecordExist = 1

    if(isRecordExist == 0):
        query = "Insert into People(ID,Name,Age,Gender) values(" +str(id)+",'"+str(name)+"','"+str(age)+"','"+str(gender)+"')"
    else:
        query = "Update People set Name = '"+str(name)+"',Age = '"+str(age)+"',Gender = '"+str(gender)+"' Where ID = "+ str(id)
    conn.execute(query)
    conn.commit()
    conn.close()

id = input("Enter your ID : ")
name = input("Enter your Name : ")
age = input("Enter your Age : ")
gender = input("Enter your Gender : ")
insertOrUpDate(id ,name ,age , gender)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
sampleNum = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y) ,(x+w , y+h) ,(0,255,0) ,2)
        sampleNum += 1
        cv2.imwrite('dataSet/User.' + str(id) + '.' + str(sampleNum) + '.jpg', gray[y:y+h, x:x+w])
        cv2.imshow('Frame', frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>200:
        break
cap.release()
cv2.destroyAllWindows()