from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Start, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from tgbot.handlers.dialogs.admin.getters.stats import get_mail_stats
from tgbot.handlers.dialogs.admin.on_clicks.mailing import start_mailing
from tgbot.states.admin.menu import AdminMenu
from tgbot.states.admin.promosg import PromoSG

admin_menu_dialog = Dialog(
    Window(
        Const('<b>Админ Меню</b>'),
        Start(Const('Промокоды'), id='promo_codes_dialog', state=PromoSG.stats),
        SwitchTo(Const('Рассылка сообщений'), id='broadcast', state=AdminMenu.enter_message),
        state=AdminMenu.admin_menu
    ),
    Window(
        Const('Введите сообщение для рассылки'),
        SwitchTo(Const('Назад'), id='back_to_admin_menu', state=AdminMenu.admin_menu),
        MessageInput(start_mailing),
        state=AdminMenu.enter_message
    ),
    Window(
        Format('Сообщение успешно отправлено. Количество получателей: {mail_count}'),
        SwitchTo(Const('Назад'), id='back_to_admin_menu', state=AdminMenu.admin_menu),
        state=AdminMenu.mail_result,
        getter=get_mail_stats
    ),

)
