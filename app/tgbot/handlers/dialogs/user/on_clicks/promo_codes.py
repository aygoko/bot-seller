from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import TextInput

from infrastructure.database.repositories.user import UserReader
from tgbot.states.user.buy_product import BuyProduct


async def check_input_promo(m: Message, textinput: TextInput, manager: DialogManager,
                            data: str):
    manager.show_mode = ShowMode.SEND
    repo: UserReader = manager.data.get('user_reader')
    status = await repo.check_promo_status(m.from_user.id, data)
    if not status:
        await m.answer('❕ Промокод не найден или уже использован. Попробуйте еще раз или перейдите к оплате.')
        return
    else:
        value = status
        manager.current_context().dialog_data['promo_value'] = value
        await manager.switch_to(BuyProduct.pay_url)
