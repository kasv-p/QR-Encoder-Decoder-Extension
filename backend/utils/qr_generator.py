from io import BytesIO
from enums.qr_types import QrType
import qrcode

def generate_qr_code(qr_gen_request) -> BytesIO:
    data=""
    print(qr_gen_request)
    if qr_gen_request.type==QrType.bank_account:
        data="upi://pay?pa="+qr_gen_request.account_no+"@"+qr_gen_request.ifsc_code+".ifsc.npci"+"&pn="+qr_gen_request.payee_name+"&am="
    elif qr_gen_request.type==QrType.upi_id:
        data="upi://pay?pa="+qr_gen_request.payee_vpa+"&pn="+qr_gen_request.payee_name
    else:
        data = qr_gen_request.text
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return img_io