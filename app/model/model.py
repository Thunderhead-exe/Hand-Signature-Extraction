from ultralytics import YOLO
from pathlib import Path
import io
from PIL import Image

inferance_model = YOLO("./model/yolo_v8n_finetuned_hand_signatures.pt")

# Cropping and Saving the signature
def cropSignature(image, save_dir, model=inferance_model, confidance=0.2):  
    prediction = model.predict(image, conf=confidance)
    prediction[0].save_crop(save_dir=save_dir, file_name=save_dir+"croppedSignature")
    signature_path = save_dir+"signature/"+"croppedSignature.jpg"
    signature = Image.open(io.BytesIO(open(signature_path, "rb").read()))
    return {"signature_image":signature, "signature_path":signature_path}