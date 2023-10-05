import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

path = 'user_faces'

images = []
classNames = []
mylist = os.listdir(path)

for cl in mylist:
    if cl.endswith(".jpg") or cl.endswith(".png"):
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList

encoded_face_train = findEncodings(images)

def markAttendance(name):
    if name != "Unknown":
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = [entry.split(',')[0].strip() for entry in myDataList]
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'{name}, {time}, {date}\n')

cap = cv2.VideoCapture(0)
known_face_names = []
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    
    face_names = ["Unknown"] * len(faces_in_frame)  # Initialize all as Unknown

    for i, encode_face in enumerate(encoded_faces):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            face_names[i] = classNames[matchIndex].upper().lower()

    # Check if a face has been recognized consistently over multiple frames
    for i, name in enumerate(face_names):
        if name != "Unknown":
            known_face_names.append(name)

            if known_face_names.count(name) >= 5:
                markAttendance(name)
                known_face_names.clear()

    for (top, right, bottom, left), name in zip(faces_in_frame, face_names):
        y1, x2, y2, x1 = top, right, bottom, left
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
