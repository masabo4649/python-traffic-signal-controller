from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import controller
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

class SignalStatus(BaseModel):
    green: Optional[int] = None
    yellow: Optional[int] = None
    red: Optional[int] = None

@app.get("/status")
def getStatus():
    return json.dumps(controller.getStatus())

@app.post("/status")
def setStatus(status: SignalStatus):
    controller.setStatus(status.dict())
    print(json.dumps(status.dict()))
    return json.dumps(controller.getStatus())
