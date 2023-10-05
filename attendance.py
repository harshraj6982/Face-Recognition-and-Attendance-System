import cv2
import face_recognition
import os
import numpy as np
from gtts import gTTS
from datetime import datetime
import threading

# Define the path to the directory containing user face images
path = 'user_faces'

# Lists to store user images and their corresponding class names (names of users)
images = []
classNames = []
mylist = os.listdir(path)

# Load user images and class names from the 'user_faces' directory
for cl in mylist:
    if cl.endswith(".jpg") or cl.endswith(".png"):
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

# Function to play an audio sound using 'afplay' (macOS specific)
def play_sound(path):
    os.system(f'afplay {path}')  # Play the audio file

# Function to encode faces in user images
def findEncodings(images):
    play_sound("sounds/encoding.mp3")  # Play an encoding sound
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    play_sound("sounds/encoded.mp3")  # Play an encoded sound
    return encodeList

# Encode the faces in user images and store the encodings
encoded_face_train = findEncodings(images)

# Function to mark attendance and play a sound message
import cv2
import face_recognition
import os
import numpy as np
from gtts import gTTS
from datetime import datetime
import threading

# ... (Previous code)

# Function to mark attendance and play a sound message
def markAttendance(name):
    if name != "Unknown":
        # Create a set to store existing names for faster lookup
        existing_names = set()

        with open('Attendance.csv', 'r+') as f:
            for line in f:
                entry = line.split(',')
                existing_names.add(entry[0].strip())

        if name not in existing_names:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            with open('Attendance.csv', 'a') as f:
                f.writelines(f'{name}, {time}, {date}\n')
            
            # Use gTTS to speak the attendance message
            message = f'{name} attendance has been marked'
            tts = gTTS(message)
            tts.save('attendance_message.mp3')

            # Perform the blocking operations in a separate thread
            def speak_marking():
                os.system('afplay attendance_message.mp3')  # Play the audio file
                os.remove('attendance_message.mp3')  # Delete the temporary audio file

            # Start a new thread to perform the marking operations
            marking_thread = threading.Thread(target=speak_marking)
            marking_thread.start()

# Initialize the webcam capture
cap = cv2.VideoCapture(0)
known_face_names = []

# Main loop for capturing frames and processing faces
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
                markAttendance(name)  # Mark attendance only if recognized consistently
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

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
