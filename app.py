from fastapi import FastAPI
import json
import os
from datetime import datetime

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Face Presence Detection API Running",
        "status": "success"
    }


@app.get("/status")
def get_status():

    if not os.path.exists("output.json"):

        return {
            "error": "output.json file not found",
            "face_present": False
        }

    try:

        with open("output.json", "r") as file:
            data = json.load(file)

        return {
            "face_present": data.get("face_present", False),
            "timestamp": data.get("timestamp", str(datetime.now()))
        }

    except Exception as e:

        return {
            "error": str(e),
            "face_present": False
        }