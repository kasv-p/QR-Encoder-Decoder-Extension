from fastapi import HTTPException
import cv2
from PIL import Image

async def decode_qr(image):
    if not image.content_type.startswith("image"):
        raise HTTPException(status_code=400, detail="Only images are allowed")
    file_name = "uploaded_image.png"
    with open(file_name, "wb") as buffer:
        buffer.write(await image.read())
    img=cv2.imread(file_name)
    detector = cv2.QRCodeDetector()
    val,_,_ = detector.detectAndDecode(img)
    return val
    