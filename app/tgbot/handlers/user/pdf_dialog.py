from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Url
from aiogram_dialog.widgets.text import Const, Format

from tgbot.handlers.dialogs.user.getters.payments import get_payment_link
from tgbot.handlers.dialogs.user.on_clicks.promo_codes import check_input_promo
from tgbot.states.user.buy_pdf import BuyPDF

pdf_dialog = Dialog(
    Window(
        Const('Введите промокод, если он у вас есть или нажмите "Пропустить"'),
        TextInput(id='promo_code', on_success=check_input_promo),
        SwitchTo(Const('Пропустить'), id='skip_promo', state=BuyPDF.pay_url),
        state=BuyPDF.enter_promo_code
    ),
    Window(
        Format('Промокод на скидку {amount} рублей активирован.', when='amount'),
        Const('Нажмите кнопку ниже для оплаты'),
        Url(Const('Оплатить'), Format('{pay_link}')),
        getter=get_payment_link,
        state=BuyPDF.pay_url
    )
)
