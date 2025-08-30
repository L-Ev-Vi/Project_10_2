import pytest

from src.calculate import calculate_taxes


@pytest.mark.parametrize('tax_rate, resul', [(20, [120.0, 240.0]),
                                             (30, [130.0, 260.0]),
                                             (10, [110.0, 220.0])
                                             ])

def test_calculate_taxes(prices1, tax_rate, resul):
    assert calculate_taxes(prices1, tax_rate) == resul
