from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const, Format

from tgbot.handlers.dialogs.admin.getters.stats import get_promo_stats
from tgbot.handlers.dialogs.admin.on_clicks.add_promocode import add_promocode
from tgbot.states.admin.promosg import PromoSG

admin_changes_dialog = Dialog(
    Window(
        Const('<b>Статистика использования промокодов</b>'),
        Format('{stats_msg}'),
        SwitchTo(Const('Создать промокод'), id='create_promo', state=PromoSG.enter_name),
        state=PromoSG.stats,
        getter=get_promo_stats
    ),
    Window(
        Const('<b>Создание промокода</b>'),
        TextInput(id='promo_name', on_success=add_promocode),
        state=PromoSG.enter_name
    ),
    Window(
        Const('<b>Промокод успешно создан</b>'),
        Cancel(Const('Вернуться в меню')),
        state=PromoSG.created
    ),
)
