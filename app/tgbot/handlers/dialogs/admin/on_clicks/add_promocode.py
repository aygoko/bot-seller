import logging

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import TextInput

from infrastructure.database.repositories.admin import AdminRepo
from tgbot.states.admin.promosg import PromoSG

logger = logging.getLogger(__name__)


async def add_promocode(m: Message, textinput: TextInput, manager: DialogManager,
                        promo_name: str):
    manager.show_mode = ShowMode.SEND
    manager.current_context().dialog_data['promocode_name'] = promo_name
    repo: AdminRepo = manager.data.get('admin_repo')
    await repo.add_promocode(promo_name)
    await manager.switch_to(PromoSG.created)
