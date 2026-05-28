# 👁️ Face Presence Detection System

A real-time **Face Presence Monitoring System** built using OpenCV and FastAPI.  
It detects whether a person is present in front of the camera and tracks absence duration for monitoring use cases like online interviews and proctoring.

---

## 🚀 Features

- Real-time face detection using OpenCV (Haar Cascade)
- Tracks presence and absence duration
- Alerts when user is absent beyond threshold
- Outputs structured JSON data
- REST API using FastAPI
- Works with webcam in real time

---

## 🏗️ Project Structure

```
face_presence_detection/
│
├── detector.py        # Webcam face detection logic
├── app.py             # FastAPI backend
├── output.json        # Live detection output
├── requirements.txt   # Dependencies
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- OpenCV
- FastAPI
- Uvicorn

---

## 🧠 How It Works

1. Webcam captures live video
2. OpenCV detects faces using Haar Cascade
3. System tracks:
   - Face presence
   - Absence duration
4. Data is written to `output.json`
5. FastAPI serves this data via API

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nandithasri2006/face-presence-detection.git
cd face-presence-detection
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run face detection (webcam)

```bash
python detector.py
```

Press `q` to stop.

---

### 4. Run API server

```bash
uvicorn app:app --reload
```

---

## 🌐 API Endpoints

### 🔹 Home

```
GET /
```

Response:
```json
{
  "message": "Face Presence Detection Running"
}
```

---

### 🔹 Status

```
GET /status
```

Response:
```json
{
  "face_present": true,
  "duration_absent_sec": 2.5,
  "alert": false
}
```

---

## 📊 Output Format

```json
{
  "face_present": true,
  "duration_absent_sec": 0,
  "alert": false
}
```

---

## ⚙️ Configuration

Inside `detector.py`:

```python
FACE_CONFIRM_FRAMES = 2
ABSENCE_THRESHOLD = 3
```

You can adjust:
- sensitivity of detection
- alert timing

---

## ⚠️ Limitations

- Works only on local system (webcam required)
- Haar Cascade may fail in poor lighting or side faces
- Not suitable for production-grade surveillance without upgrades

---

## 💡 Future Improvements

- YOLO-based face detection (higher accuracy)
- Eye tracking for cheating detection
- Web dashboard UI
- Cloud deployment with video streaming

---

## 👨‍💻 Author

Built as a learning project for:
- Computer Vision basics
- Real-time monitoring systems
- API integration using FastAPI

---

## 📌 Note

Run `detector.py` first before starting API to generate live output.
