import cv2
import json
from datetime import datetime

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Open webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Webcam started successfully")

while True:

    # Read frame
    success, frame = cap.read()

    if not success:
        print("Failed to read frame")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    face_present = False

    # If face detected
    if len(faces) > 0:

        face_present = True

        for (x, y, w, h) in faces:

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    # Save JSON output
    data = {
        "face_present": face_present,
        "timestamp": str(datetime.now())
    }

    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)

    # Display text
    cv2.putText(
        frame,
        f"Face Present: {face_present}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam
    cv2.imshow("Face Presence Detection", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()