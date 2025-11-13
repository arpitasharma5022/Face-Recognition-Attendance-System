import cv2
import numpy as np
import face_recognition
import pickle
import pandas as pd
from datetime import datetime

# Load Encoded Data
with open('encodings.pkl', 'rb') as f:
    encodeListKnown, classNames = pickle.load(f)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load or Create attendance file
attendance_file = 'attendance.csv'
try:
    df = pd.read_csv(attendance_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Name', 'Time'])

def markAttendance(name):
    now = datetime.now()
    dtString = now.strftime('%Y-%m-%d %H:%M:%S')
    if name not in list(df['Name']):
        new_row = {'Name': name, 'Time': dtString}
        df.loc[len(df)] = new_row
        df.to_csv(attendance_file, index=False)
        print(f"{name} marked present at {dtString}")

print("Starting camera... Press 'q' to quit")

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            markAttendance(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow('Webcam - Face Recognition Attendance', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
