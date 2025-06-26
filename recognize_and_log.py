import cv2
import face_recognition
import numpy as np
import os
import csv
from datetime import datetime, timedelta
from utils.encoding_loader import load_all_encodings

LOG_FILE = 'logs/attendance.csv'
RECOGNITION_MODEL = 'hog'
LOG_INTERVAL_MINUTES = 5

# Dictionary lưu thời điểm chấm công gần nhất của từng người
last_logged_times = {}

def ensure_log_file():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            csv.writer(f).writerow(['Name', 'Date', 'Time'])

def should_log(name):
    now = datetime.now()
    last_time = last_logged_times.get(name)

    if last_time is None or now - last_time >= timedelta(minutes=LOG_INTERVAL_MINUTES):
        last_logged_times[name] = now
        return True
    return False

def log_attendance(name):
    now = datetime.now()
    with open(LOG_FILE, 'a', newline='') as f:
        csv.writer(f).writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
    print(f"📝 {name} logged at {now.strftime('%H:%M:%S')}")

def draw_box(frame, box, name):
    top, right, bottom, left = [v * 4 for v in box]
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(frame, name, (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

def process_frame(frame, known_encodings, known_names):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb_small, model=RECOGNITION_MODEL)
    encodings = face_recognition.face_encodings(rgb_small, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            matched_idxs = [i for i, match in enumerate(matches) if match]
            best_match = min(matched_idxs, key=lambda i: face_recognition.face_distance([known_encodings[i]], encoding))
            name = known_names[best_match]

            # ✅ Ghi lại nếu đã qua ≥ 5 phút
            if should_log(name):
                log_attendance(name)

        draw_box(frame, box, name)

def main():
    print("📦 Loading encodings...")
    known_encodings, known_names = load_all_encodings()
    if not known_encodings:
        print("❌ No encodings loaded. Please run encode_faces first.")
        return

    ensure_log_file()
    print("✅ Encodings loaded. Starting camera...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot access camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        process_frame(frame, known_encodings, known_names)
        cv2.imshow("Face Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
