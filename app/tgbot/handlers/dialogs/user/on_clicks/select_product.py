from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from tgbot.states.user.buy_product import BuyProduct


async def choose_product(c: CallbackQuery, widget: Any, manager: DialogManager, product_id: str):
    manager.current_context().dialog_data['product_id'] = product_id
    await manager.start(BuyProduct.enter_promo_code, data={'product_id': product_id})
