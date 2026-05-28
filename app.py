from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Face Presence Detection API Running",
        "status": "success"
    }


@app.get("/status")
def status():

    return {
        "face_present": True
    }