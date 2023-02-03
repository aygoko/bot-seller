async def api_create_invoice(price: float, data: str) -> str:
    """
    Create payment url for user
    :param price: payment amount
    :param data: payment label
    :return: payment url
    """
    url = f'https://yoomoney.ru/quickpay/confirm.xml?receiver=&quickpay-form=shop&targets' \
          f'=Оплата%20подписки%20&paymentType=SB&sum={price}&label={data}'
    return url
