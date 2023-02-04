from aiogram_dialog import DialogManager

from infrastructure.database.repositories.user import UserReader
from tgbot.pay_api.create_invoice import api_create_invoice


async def get_payment_link(dialog_manager: DialogManager, user_reader: UserReader, **kwargs):
    promo_value = dialog_manager.current_context().dialog_data.get('promo_value', None)
    link = await api_create_invoice(100, 'test')
    return {
        'pay_link': link,
        'amount': promo_value
    }
