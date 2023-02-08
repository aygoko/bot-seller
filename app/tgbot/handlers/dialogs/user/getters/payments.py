import uuid

from aiogram_dialog import DialogManager

from infrastructure.database.repositories.user import UserReader, UserRepo
from tgbot.pay_api.create_invoice import api_create_invoice


async def get_payment_link(dialog_manager: DialogManager,
                           user_reader: UserReader,
                           user_repo: UserRepo, **kwargs) -> dict[str, str]:
    promo_value = dialog_manager.current_context().dialog_data.get('promo_value', None)
    product_id: int = int(dialog_manager.current_context().start_data.get('product_id', None))
    product_price = await user_reader.get_item_price(product_id)
    if promo_value:
        amount_total = product_price - promo_value
    else:
        amount_total = product_price
    invoice_hash = str(uuid.uuid4())
    await user_repo.add_invoice(dialog_manager.event.from_user.id, amount_total, invoice_hash, product_id)
    link = await api_create_invoice(amount_total, invoice_hash)
    promo = True if promo_value else False
    return {
        'total': amount_total,
        'pay_link': link,
        'amount': promo_value,
        'promo': promo,
    }
