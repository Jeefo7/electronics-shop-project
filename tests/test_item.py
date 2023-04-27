"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


test1 = Item("ТестСмартфон", 5000, 10)
test2 = Item("ТестНоутбук", 10000, 3)
def test_calculate_total_price():
    assert test1.calculate_total_price() == 50000
    assert test2.calculate_total_price() == 30000


def test_apply_discount():
    assert test1.apply_discount() == None