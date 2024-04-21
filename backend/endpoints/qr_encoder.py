from fastapi import APIRouter
from fastapi.responses import Response
from models.qr_model import QrModel
from utils.qr_generator import generate_qr_code

router = APIRouter()

@router.post("/generate-qr")
async def qr_generator(qr_gen_request: QrModel):
    return Response(generate_qr_code(qr_gen_request).getvalue(), media_type="image/png")
