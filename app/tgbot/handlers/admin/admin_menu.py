from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Start,  SwitchTo
from aiogram_dialog.widgets.text import Const

from tgbot.handlers.dialogs.admin.on_clicks.message_to_all import sending_messages_to_all_users
from tgbot.states.admin.promosg import PromoSG
from tgbot.states.admin.menu import AdminMenu

admin_menu_dialog = Dialog(
    Window(
        Const('<b>Админ Меню</b>'),
        Start(Const('Промокоды'), id='changes', state=PromoSG.stats),
        SwitchTo(Const('Рассылка сообщений'), id='send_message_to_all', state=AdminMenu.send_message_to_all),
        state=AdminMenu.admin_menu
    ),
    Window(
        Const('Введите сообщение для рассылки'),
        MessageInput(sending_messages_to_all_users),
        state=AdminMenu.enter_message
    )

)