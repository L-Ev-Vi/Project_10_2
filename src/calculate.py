def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    new_list = []
    for price in prices:
        if price <= 0:
            raise ValueError ('Неверная цена')
    if tax_rate <= 0 or tax_rate >= 100:
            raise ValueError('Неверный налоговый процент')
    else:
        for price in prices:
            new_price = price + (price * tax_rate) / 100
            new_list.append(new_price)
        return new_list
