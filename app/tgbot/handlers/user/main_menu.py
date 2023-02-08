import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Url, Select, Group
from aiogram_dialog.widgets.text import Format, Const

from tgbot.handlers.dialogs.user.getters.products import get_products
from tgbot.handlers.dialogs.user.on_clicks.select_product import choose_product
from tgbot.states.user.menu import UserMenu

main_menu_dialog = Dialog(
    Window(
        Format('Привет!'),
        Const('Выберите товар'),
        Url(
            Const('Доступ в приват на месяц'),
            Const('https://t.me/donate')
        ),
        Group(
            Select(
                Format('{item.product_name} за {item.product_price} рублей'),
                id='product',
                item_id_getter=operator.attrgetter('product_id'),
                items='products',
                on_click=choose_product
            ),
            width=1
        ),

        state=UserMenu.main_menu,
        getter=get_products
    ),
)
