import pytest

from src.calculate import calculate_taxes


@pytest.mark.parametrize('tax_rate, resul', [(20, [120.0, 240.0]),
                                             (30, [130.0, 260.0]),
                                             (10, [110.0, 220.0])
                                             ])

def test_calculate_taxes(prices1, tax_rate, resul):
    assert calculate_taxes(prices1, tax_rate) == resul

def test_calculate_taxes_prices1_zero():
    with pytest.raises(ValueError) as info:
        calculate_taxes([0], 10)

def test_calculate_taxes_tax_rate_100(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, 100)

def test_calculate_taxes_tax_rate_zero(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, 0)

def test_calculate_taxes_tax_rate_200(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, 200)

def test_calculate_taxes_tax_rate_minus_50(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, -50)
