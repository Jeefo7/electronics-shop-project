"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


test1 = Item("ТестСмартфон", 5000, 10)
test2 = Item("ТестНоутбук", 10000, 3)
def test_calculate_total_price():
    assert test1.calculate_total_price() == 50000
    assert test2.calculate_total_price() == 30000

def test_apply_discount():
    assert test1.apply_discount() == None

def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара равна 10 символов
    item.name = '0123456789'
    assert item.name == '0123456789'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name != 'СуперСмартфон'

def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    test1 = Item.all[0]
    assert test1.name == "СуперСмартфон"

def test_name():
    item1 = Item('Смартфон', 1000, 1)

    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'

    item1.name = "Телефон"
    assert item1.name == 'Телефон'
