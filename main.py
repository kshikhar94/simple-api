from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my simple API!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/get-ip")
def get_ip():
    response = requests.get("https://api.ipify.org?format=json")
    return response.json()
