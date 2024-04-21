from pydantic import BaseModel
from typing import Optional
from enums.qr_types import QrType

class QrModel(BaseModel):
    payee_name: Optional[str] = ""
    payee_vpa: Optional[str] = ""
    account_no: Optional[str] = ""
    ifsc_code: Optional[str] = ""
    text: Optional[str] = ""
    type: QrType
