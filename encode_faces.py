import cv2
import face_recognition
import os
import pickle

path = 'Images'
images = []
classNames = []
myList = os.listdir(path)

print("Encoding images...")
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if encodes:
            encodeList.append(encodes[0])
    return encodeList

encodeListKnown = findEncodings(images)
print("Encoding Complete ✅")

with open('encodings.pkl', 'wb') as f:
    pickle.dump((encodeListKnown, classNames), f)

print("Encodings saved successfully.")
