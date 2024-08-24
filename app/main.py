from fastapi import FastAPI, UploadFile
from model.model import cropSignature
import io
from PIL import Image
from fastapi.responses import FileResponse

app = FastAPI()
    
@app.get("/")
def home():
#    return {"health_check": "OK", "model_version": model_version}
    return {"health_check": "OK"}

@app.post("/predict")
def predict(image:UploadFile):
    input_image = image.file.read()
    input_image = Image.open(io.BytesIO(input_image))
    cropped_signature = cropSignature(image=input_image, save_dir="./", confidance=0.2)
    # |-- cropSignature == {"signature_image":signature, "signature_path":signature_path}
    return FileResponse(cropped_signature["signature_path"])
    #return cropped_signature