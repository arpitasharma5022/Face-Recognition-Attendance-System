# 🎓 Face Recognition Attendance System

An **AI-based Attendance System** built using **Python**, **OpenCV**, and **Face Recognition**.  
It automatically detects and recognizes faces from a live webcam feed and marks attendance in a CSV file with timestamps.

---

## 🚀 Features

- 🔍 Real-time face detection using OpenCV  
- 🤖 Face recognition using `face_recognition` library (based on dlib)  
- 🧠 Machine learning-based encoding for registered users  
- 🗂️ Automatic attendance marking in `attendance.csv`  
- 🕒 Records timestamp for each entry  
- 📸 Easy to add new users by simply placing their images in the `Images/` folder  

---

## 🧰 Technologies Used

- **Python 3.8+**
- **OpenCV** – for real-time image capturing and processing  
- **face_recognition** – for facial encoding and matching  
- **NumPy & Pandas** – for data handling and storage  
- **dlib** (installed with face_recognition) – for deep learning-based face encoding  

---

## 🗂️ Project Structure

Face_Recognition_Attendance/
│
├── Images/ # Folder containing images of known persons
│ ├── Arpita.jpg
│ ├── Rahul.jpg
│ └── etc...
│
├── encode_faces.py # Script to encode faces from Images folder
├── face_recognition_attendance.py # Main attendance system
├── attendance.csv # Output file for attendance records
├── encodings.pkl # Saved face encodings (auto-generated)
├── requirements.txt # Required dependencies
└── README.md # Project documentation



---

## ⚙️ Installation & Setup

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/yourusername/Face_Recognition_Attendance.git
   cd Face_Recognition_Attendance
pip install -r requirements.txt

Add known faces:

Place clear front-facing images in the Images/ folder.

Example: Images/Arpita.jpg, Images/Rahul.jpg

Encode faces (run once):

python encode_faces.py


Run the attendance system:

python face_recognition_attendance.py


Press q to quit webcam window.

🧾 Output

Attendance is saved automatically in a file named attendance.csv:

Name	Time
ARPITA	2025-11-13 11:25:34
RAHUL	2025-11-13 11:27:12
