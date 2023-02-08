from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Url, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Format, Const

from tgbot.handlers.dialogs.common import when_not
from tgbot.handlers.dialogs.user.getters.payments import get_payment_link
from tgbot.handlers.dialogs.user.on_clicks.promo_codes import check_input_promo
from tgbot.states.user.buy_product import BuyProduct

buy_product_dialog = Dialog(
    Window(
        Const('Введите промокод'),
        TextInput(id='promo_code', on_success=check_input_promo),
        SwitchTo(Const('Пропустить'), id='skip_promo', state=BuyProduct.pay_url),
        Cancel(Const('Назад'), id='back_to_products'),
        state=BuyProduct.enter_promo_code
    ),
    Window(
        Format('Применен промокод на {amount} рублей, к оплате {total} рублей', when='promo'),
        Format('К оплате {total} рублей', when=when_not('promo')),
        Url(
            Const('Оплатить'),
            Format('{pay_link}')  # ссылка на оплату yoomoney
        ),
        SwitchTo(Const('Назад'), id='back_to_promo', state=BuyProduct.enter_promo_code),
        state=BuyProduct.pay_url,
        getter=get_payment_link
    )
)
