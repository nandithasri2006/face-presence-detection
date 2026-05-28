from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Face Presence Detection API Running"}

@app.get("/status")
def status():
    try:
        with open("output.json", "r") as f:
            return json.load(f)
    except:
        return {
            "face_present": False,
            "duration_absent_sec": -1,
            "alert": False
        }