def calculate_taxes(prices: list[float], tax_rate: float)-> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    new_list = []
    for price in prices:
        new_price = price + (price * tax_rate) / 100
        new_list.append(new_price)
    return new_list
