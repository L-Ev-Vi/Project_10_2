import pytest

from src.calculate import calculate_taxes


@pytest.mark.parametrize('tax_rate, resul', [(20, [120.00, 240.00]),
                                             (30, [130.00, 260.00]),
                                             (10, [110.00, 220.00])
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
        calculate_taxes(prices1, -1)


def test_calculate_taxes_tax_rate_200(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, 200)


def test_calculate_taxes_tax_rate_minus_50(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, -50)


def test_calculate_taxes_discount(prices1):
    assert calculate_taxes(prices1, 10, discount = 5) == [104.5, 209.0]

def test_calculate_taxes_discount_4_5(prices1):
    assert calculate_taxes(prices1, 10, discount = 4.5) == [105.05, 210.1]


def test_calculate_taxes_prices1e_not_int():
    with pytest.raises(TypeError) as info:
        calculate_taxes("prices1", -50)

def test_calculate_taxes_tax_rate_not_int(prices1):
    with pytest.raises(TypeError) as info:
        calculate_taxes(prices1, "False")

def test_calculate_taxes_tax_rate_not_f(prices1):
        assert calculate_taxes(prices1, False) == [100, 200]

def test_calculate_taxes_tax_rate_not_dis(prices1):
    with pytest.raises(ValueError) as info:
        calculate_taxes(prices1, 0, discount = -20)

def test_calculate_taxes_prices1e_not_i():
    with pytest.raises(TypeError) as info:
        calculate_taxes(["prices1", False], 0)
