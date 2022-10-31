import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer\\trainningData.yml")
id = 0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (203, 23, 252)

def getProfile(id):
    conn = sqlite3.connect('D:\\1\\Data.db')
    cmd = "SELECT * FROM People WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


while (True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        profile = getProfile(id)
        if conf <48 :

            if (profile != None):
                cv2.putText(frame, "Name: " + str(profile[1]), (x, y + h + 30), fontface, fontscale, fontcolor, 2)
                cv2.putText(frame, "Age: " + str(profile[2]), (x, y + h + 60), fontface, fontscale, fontcolor, 2)
                cv2.putText(frame, "Gender: " + str(profile[3]), (x, y + h + 90), fontface, fontscale, fontcolor, 2)
        else:
            cv2.putText(frame, "Unknow " , (x + 10 , y + h + 30), fontface, fontscale, fontcolor, 2)


    cv2.imshow('Face', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
