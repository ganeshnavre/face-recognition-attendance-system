import cv2
import face_recognition
import pickle
import os
import csv
import numpy as np
from datetime import datetime
from spoof_check import spoof_check

FACE_DB = "face_db"
ATTENDANCE_FILE = "attendance.csv"

known_faces = []
names = []

for file in os.listdir(FACE_DB):
    if file.endswith(".pkl"):
        with open(os.path.join(FACE_DB, file), "rb") as f:
            enc = pickle.load(f)
            known_faces.append(enc[0])
            names.append(file.replace(".pkl", ""))

if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time", "Type"])

# 🔒 Spoof check before attendance
if not spoof_check():
    print("Attendance blocked due to spoof detection")
    exit()

cap = cv2.VideoCapture(0)
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for enc in encodings:
        matches = face_recognition.compare_faces(known_faces, enc, tolerance=0.5)
        distances = face_recognition.face_distance(known_faces, enc)

        if True in matches:
            idx = np.argmin(distances)
            name = names[idx]

            now = datetime.now()
            with open(ATTENDANCE_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    name,
                    now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S"),
                    "Punch-In"
                ])

            print(f"Attendance marked for {name}")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Face Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
