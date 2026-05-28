import cv2
import json
from datetime import datetime
import state
import time

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

ABSENCE_THRESHOLD = 2  # seconds (configurable)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    now = datetime.now()

    # FACE DETECTED
    if len(faces) > 0:
        state.face_present = True
        state.last_seen_time = now

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    else:
        state.face_present = False

    # Calculate absence duration
    duration_absent = (now - state.last_seen_time).total_seconds()

    # Output JSON
    data = {
        "face_present": len(faces) > 0,
        "duration_absent_sec": round(duration_absent, 2)
    }

    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

    cv2.putText(frame,
                f"Face: {len(faces)>0}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    cv2.putText(frame,
                f"Absent: {duration_absent:.1f}s",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2)

    cv2.imshow("Face Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()