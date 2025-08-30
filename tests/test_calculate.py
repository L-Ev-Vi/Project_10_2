import pytest


from src.calculate import calculate_taxes

def test_calculate_taxes():
    assert calculate_taxes([100, 200], 20) == [120, 240]
