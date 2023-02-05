from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager


async def choose_product(c: CallbackQuery, widget: Any, d: DialogManager, product_id: str):
    d.current_context().dialog_data['product_id'] = product_id
    await d.dialog().next()
