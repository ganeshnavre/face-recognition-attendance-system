# Face Recognition Attendance System with Spoof Detection

This project implements a real-time **Face Authentication Attendance System** using computer vision and machine learning techniques.  
The system marks attendance using a live camera feed while preventing spoofing attempts through **blink-based liveness detection**.

---

## 🚀 Features

- 👤 Face registration using webcam  
- 🧠 Face recognition using pre-trained facial embeddings  
- ⏱️ Real-time attendance marking  
- 🔐 Blink-based spoof (liveness) detection  
- 📝 Punch-In / Punch-Out support  
- 📂 Attendance stored in CSV format  
- 💻 Fully offline, CPU-based solution  

---

## 🛠️ Tech Stack

- Python 3.10  
- OpenCV – camera access & image processing  
- face_recognition (dlib-based) – face encoding & matching  
- MediaPipe – facial landmark detection (blink detection)  
- NumPy  
- CSV – attendance storage  

---

## 📁 Project Structure
# Face Recognition Attendance System with Spoof Detection

This project implements a real-time **Face Authentication Attendance System** using computer vision and machine learning techniques.  
The system marks attendance using a live camera feed while preventing spoofing attempts through **blink-based liveness detection**.

---

## 🚀 Features

- 👤 Face registration using webcam  
- 🧠 Face recognition using pre-trained facial embeddings  
- ⏱️ Real-time attendance marking  
- 🔐 Blink-based spoof (liveness) detection  
- 📝 Punch-In / Punch-Out support  
- 📂 Attendance stored in CSV format  
- 💻 Fully offline, CPU-based solution  

---

## 🛠️ Tech Stack

- Python 3.10  
- OpenCV – camera access & image processing  
- face_recognition (dlib-based) – face encoding & matching  
- MediaPipe – facial landmark detection (blink detection)  
- NumPy  
- CSV – attendance storage  

---

## 📁 Project Structure

# Face Recognition Attendance System with Spoof Detection

This project implements a real-time **Face Authentication Attendance System** using computer vision and machine learning techniques.  
The system marks attendance using a live camera feed while preventing spoofing attempts through **blink-based liveness detection**.

---

## 🚀 Features

- 👤 Face registration using webcam  
- 🧠 Face recognition using pre-trained facial embeddings  
- ⏱️ Real-time attendance marking  
- 🔐 Blink-based spoof (liveness) detection  
- 📝 Punch-In / Punch-Out support  
- 📂 Attendance stored in CSV format  
- 💻 Fully offline, CPU-based solution  

---

## 🛠️ Tech Stack

- Python 3.10  
- OpenCV – camera access & image processing  
- face_recognition (dlib-based) – face encoding & matching  
- MediaPipe – facial landmark detection (blink detection)  
- NumPy  
- CSV – attendance storage  

---

## 📁 Project Structure

face-recognition-attendance-system/
│
├── register_face.py # Register new user's face
├── attendance.py # Face recognition + attendance marking
├── spoof_check.py # Blink-based liveness detection
├── attendance.csv # Attendance records
├── face_db/ # Stored face encodings (.pkl files)
├── README.md # Project documentation
└── .gitignore


---

## ⚙️ How It Works

### 1️⃣ Face Registration
- Run `register_face.py`
- Multiple face samples are captured via webcam
- Face encodings are generated and stored using Pickle

### 2️⃣ Spoof Detection (Liveness Check)
- System asks the user to blink
- Eye Aspect Ratio (EAR) is calculated using MediaPipe
- Attendance is blocked if blink is not detected

### 3️⃣ Attendance Marking
- Live face is matched with stored encodings
- If matched and liveness is confirmed:
  - Name, date, time, and punch type are logged in CSV

---

## ▶️ How to Run

### Step 1: Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate


