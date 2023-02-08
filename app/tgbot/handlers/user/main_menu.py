import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Url, Select, SwitchTo
from aiogram_dialog.widgets.text import Format, Const

from tgbot.handlers.dialogs.user.getters.payments import get_payment_link
from tgbot.handlers.dialogs.user.getters.products import get_products
from tgbot.handlers.dialogs.user.on_clicks.promo_codes import check_input_promo
from tgbot.handlers.dialogs.user.on_clicks.select_product import choose_product
from tgbot.states.user.buy_product import BuyProduct

main_menu_dialog = Dialog(
    Window(
        Format('Привет!'),
        Const('Выберите товар'),
        Url(
            Const('Доступ в приват на месяц'),
            Const('https://t.me/donate')
        ),
        Select(
            Format('{item.product_name} за {item.product_price} рублей'),
            id='product',
            item_id_getter=operator.attrgetter('product_id'),
            items='products',
            on_click=choose_product
        ),
        state=BuyProduct.choose_product,
        getter=get_products
    ),
    Window(
        Const('Введите промокод'),
        TextInput(id='promo_code', on_success=check_input_promo),
        SwitchTo(Const('Пропустить'), id='skip_promo', state=BuyProduct.pay_url),
        SwitchTo(Const('Назад'), id='back_to_products', state=BuyProduct.choose_product),
        state=BuyProduct.enter_promo_code
    ),
    Window(
        Format('Применен промокод на {amount} рублей, к оплате {total} рублей'),
        Url(
            Const('Оплатить'),
            Format('{pay_link}')  # ссылка на оплату yoomoney
        ),
        SwitchTo(Const('Назад'), id='back_to_promo', state=BuyProduct.enter_promo_code),
        state=BuyProduct.pay_url,
        getter=get_payment_link
    )
)
