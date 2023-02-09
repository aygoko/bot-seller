from datetime import datetime

from domain.dto.base import DTO


class InvoiceDTO(DTO):
    invoice_id: int
    user_id: int
    amount: int
    created_at: datetime
    paid: bool
    payment_id: int | None
    invoice_hash: str
    product_id: int
