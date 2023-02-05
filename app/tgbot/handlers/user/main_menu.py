import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Url, Select, Start
from aiogram_dialog.widgets.text import Format, Const

from tgbot.handlers.dialogs.user.getters.products import get_products
from tgbot.handlers.dialogs.user.on_clicks import choose_product
from tgbot.states.main_menu import MainMenu

from tgbot.states.user.buy_product import BuyProduct

main_menu_dialog = Dialog(
    Window(
        Format('Привет!'),
        Url(
            Const("Доступ в приват на месяц"),
            Const("https://t.me/donate")
        ),
        Select(
            Const('Выберите товар'),
            Format('{item.product_name} за {item.product_price} рублей'),
            id='product',
            item_id_getter=operator.attrgetter('product_id'),
            on_click=choose_product
        ),
        state=BuyProduct.choose_product,
        getter=get_products
    )

)
