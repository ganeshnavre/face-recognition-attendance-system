import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(eye, landmarks):
    v1 = abs(landmarks[eye[1]].y - landmarks[eye[5]].y)
    v2 = abs(landmarks[eye[2]].y - landmarks[eye[4]].y)
    h = abs(landmarks[eye[0]].x - landmarks[eye[3]].x)
    return (v1 + v2) / (2.0 * h)

def spoof_check(timeout=5):
    cap = cv2.VideoCapture(0)
    start_time = time.time()

    print("Please blink your eyes...")

    while time.time() - start_time < timeout:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark

            left_ear = eye_aspect_ratio(LEFT_EYE, landmarks)
            right_ear = eye_aspect_ratio(RIGHT_EYE, landmarks)
            ear = (left_ear + right_ear) / 2

            # 🔑 EAR threshold (relaxed for real use)
            if ear < 0.25:
                print("Blink detected")
                cap.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow("Spoof Check", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False
