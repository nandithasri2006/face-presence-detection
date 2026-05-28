from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Face Monitoring API Running"}

@app.get("/status")
def status():
    try:
        with open("output.json", "r") as f:
            data = json.load(f)
        return data
    except:
        return {
            "face_present": False,
            "duration_absent_sec": -1
        }