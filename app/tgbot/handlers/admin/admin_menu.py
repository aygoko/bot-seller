from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from tgbot.states.admin.promosg import PromoSG
from tgbot.states.admin.menu import AdminMenu

admin_menu_dialog = Dialog(
    Window(
        Const('<b>Админ Меню</b>'),
        Start(Const('Промокоды'), id='changes', state=PromoSG.stats),
        state=AdminMenu.admin_menu
    )
)