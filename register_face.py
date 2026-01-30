import cv2
import face_recognition
import pickle
import os

os.makedirs("face_db", exist_ok=True)

name = input("Enter your name: ").strip()

cap = cv2.VideoCapture(0)
encodings = []

print("Press 'c' to capture face, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Register Face", frame)
    key = cv2.waitKey(1)

    if key == ord('c'):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)

        if len(faces) == 1:
            encoding = face_recognition.face_encodings(rgb, faces)[0]
            encodings.append(encoding)
            print(f"✅ Face captured ({len(encodings)})")
        else:
            print("⚠️ Ensure exactly ONE face")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 🔒 Safety check
if len(encodings) == 0:
    print("❌ No face captured, file not saved")
    exit()

with open(f"face_db/{name}.pkl", "wb") as f:
    pickle.dump(encodings, f)

print("🎉 Registration complete successfully")
