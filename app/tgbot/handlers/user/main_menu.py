from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Url, Select
from aiogram_dialog.widgets.text import Format, Const

from tgbot.states.main_menu import MainMenu

main_menu_dialog = Dialog(
    Window(
        Format('Привет!'),
        Url(
            Const("Доступ в приват на месяц"),
            Const("https://t.me/donate")
        ),
        Select(
            # # Const("Купить методичку"),
            # Format("Купить методичку за {item.name} рублей",
            #        id='...',
            #        item_id_getter=,
            #        on_click=
            #        ),
            # # ссылка на функцию
        ),
        Select(
            # # Const("Доступ в приват навсегда"),
            # Format("Доступ в приват навсегда за {item.name} рублей",
            #        id='...',
            #        item_id_getter=,
            #        on_click=
            #        ),
            # # ссылка на функцию
        ),
        state=MainMenu.main_menu,
        # getter=
    )

)
