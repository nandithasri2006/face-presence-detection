import cv2
import json
from datetime import datetime

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

# Safety check
if not cap.isOpened():
    print("❌ Camera not opening")
    exit()

last_seen_time = datetime.now()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    now = datetime.now()

    # FIX: better preprocessing (IMPORTANT)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # FIX: stronger detection settings
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(40, 40)
    )

    # DEBUG (VERY IMPORTANT)
    print("Faces detected:", len(faces))

    face_present = False

    # If face found
    if len(faces) > 0:
        face_present = True
        last_seen_time = now

    # absence time
    if face_present:
        duration_absent = 0
    else:
        duration_absent = (now - last_seen_time).total_seconds()

    alert = duration_absent > 3

    # JSON output
    data = {
        "face_present": face_present,
        "duration_absent_sec": round(duration_absent, 2),
        "alert": alert
    }

    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # UI text
    cv2.putText(frame,
                f"Face: {face_present}",
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

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()