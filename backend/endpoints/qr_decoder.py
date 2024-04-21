from fastapi import APIRouter, File, UploadFile
from utils.qr_decoder import decode_qr

router = APIRouter()
@router.post("/decode-qr")
async def upload_image(image: UploadFile = File(...)):
    return await decode_qr(image)