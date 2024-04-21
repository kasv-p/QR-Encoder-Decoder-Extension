from enum import Enum
class QrType(str, Enum):
    bank_account = "bank_account"
    upi_id = "upi_id"
    text_or_url = "text_or_url"