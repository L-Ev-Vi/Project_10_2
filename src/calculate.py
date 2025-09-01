def calculate_taxes(prices: list[float], tax_rate: float, *, discount: float = 0) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    new_list = []
    for arg in [ tax_rate, discount]:
        if not isinstance(arg, int| float):
            raise TypeError('Неверный тип данных')
    if not isinstance(prices, list):
        raise TypeError('Неверный список цен')
    else:
        for price in prices:
            if not isinstance(price, int or float):
                raise TypeError('Неверная цена')
            elif price <= 0:
                raise ValueError('Неверная цена')
        if tax_rate < 0 or tax_rate >= 100:
                raise ValueError('Неверный налоговый процент')
        if discount < 0:
            raise ValueError('Скидка не может быть с минусом')
        for price in prices:
            new_price = price + (price * tax_rate) / 100
            resul_price = (new_price - (new_price * discount) / 100)
            new_list.append(round(float(resul_price), 2))
        return new_list


