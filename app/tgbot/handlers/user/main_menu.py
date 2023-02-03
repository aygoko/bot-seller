from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Url, Button
from aiogram_dialog.widgets.text import Format, Const

from tgbot.states.main_menu import MainMenu

main_menu_dialog = Dialog(
    Window(
        Format('Привет!'),
        Url(
            Const("Доступ в приват на месяц"),
            Const("https://t.me/donate")
        ),
        Button(
            Const("Купить методичку"),

            # ссылка на функцию
        ),
        Button(
            Const("Доступ в приват навсегда"),
            # ссылка на функцию
        ),
        state=MainMenu.main_menu
    )

)
