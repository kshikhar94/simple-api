from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import requests
from PIL import Image
import io

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

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="only png images are allowed")
    
    content = await file.read()

    size = len(content)

    try:
        image = Image.open(io.BytesIO(content))
    except Exception as e:
        raise HTTPException(status_code=400, detail="invalid image file")
    
    width, height = image.size
    format = image.format

    image_info = {
        "image_name": file.filename,
        "image_size": size, 
        "image_format": format,
        "image_dims": {
            "width": width,
            "height": height
        }
    }

    return JSONResponse(content=image_info)
