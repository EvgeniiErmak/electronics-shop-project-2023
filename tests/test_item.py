import pytest
import csv
from src.item import Item


# Подготовительная работа для тестирования
@pytest.fixture
def create_test_items(tmp_path):
    """
    Фикстура для создания тестовых данных и экземпляров класса Item.
    """
    test_data = [
        {'name': 'Test1', 'price': '10', 'quantity': '2'},
        {'name': 'Test2', 'price': '20', 'quantity': '3'},
    ]
    test_file = tmp_path / 'test_items.csv'
    with open(test_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'quantity'])
        writer.writeheader()
        writer.writerows(test_data)

    Item.instantiate_from_csv(str(test_file))
    yield test_file
    Item.all = []

# Тесты для класса Item
def test_instantiate_from_csv(create_test_items):
    """
    Тестирование метода instantiate_from_csv класса Item.
    """
    assert len(Item.all) == 2
    assert Item.all[0].name == 'Test1'
    assert Item.all[1].name == 'Test2'

def test_string_to_number():
    """
    Тестирование метода string_to_number класса Item.
    """
    assert Item.string_to_number('42') == 42

def test_name_property():
    """
    Тестирование свойства name класса Item.
    """
    item = Item('Test', 10, 1)
    assert item.name == 'Test'
    item.name = 'VeryLongNameForTest'
    assert item.name == 'VeryLongNa'  # Изменено на 'VeryLongNa'

def test_calculate_total_price():
    """
    Тестирование метода calculate_total_price класса Item.
    """
    item = Item('Test', 10, 3)
    assert item.calculate_total_price() == 30

def test_apply_discount():
    """
    Тестирование метода apply_discount класса Item.
    """
    item = Item('Test', 10, 1)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0

def test_name_property_setter_short_name():
    """
    Тестирование сеттера свойства name класса Item для короткого имени.
    """
    item = Item('Test', 10, 1)
    item.name = 'Short'
    assert item.name == 'Short'

def test_name_property_setter_long_name():
    """
    Тестирование сеттера свойства name класса Item для длинного имени.
    """
    item = Item('Test', 10, 1)
    item.name = 'VeryLongNameForTest'
    assert item.name == 'VeryLongNa'  # Изменено на 'VeryLongNa'

def test_calculate_total_price_zero_quantity():
    """
    Тестирование метода calculate_total_price класса Item с нулевым количеством товара.
    """
    item = Item('Test', 10, 0)
    assert item.calculate_total_price() == 0

def test_calculate_total_price_negative_price():
    """
    Тестирование метода calculate_total_price класса Item с отрицательной ценой товара.
    """
    item = Item('Test', -10, 3)
    assert item.calculate_total_price() == -30

def test_apply_discount_no_discount():
    """
    Тестирование метода apply_discount класса Item без скидки.
    """
    item = Item('Test', 10, 1)
    item.pay_rate = 1.0
    item.apply_discount()
    assert item.price == 10.0

def test_apply_discount_large_discount():
    """
    Тестирование метода apply_discount класса Item с большой скидкой.
    """
    item = Item('Test', 10, 1)
    item.pay_rate = 0.1
    item.apply_discount()
    assert item.price == 1.0

def test_init_method():
    """
    Тестирование конструктора __init__ класса Item.
    """
    item = Item('Test', 10, 1)
    assert item.name == 'Test'
    assert item.price == 10
    assert item.quantity == 1

def test_str_method():
    """
    Тестирование метода __str__ класса Item.
    """
    item = Item('Test', 10, 1)
    assert str(item) == 'Test'

def test_repr_method():
    """
    Тестирование метода __repr__ класса Item.
    """
    item = Item('Test', 10, 1)
    assert repr(item) == "Item('Test', 10, 1)"

def test_pay_rate():
    """
    Тестирование атрибута класса pay_rate класса Item.
    """
    item = Item('Test', 10, 1)
    assert item.pay_rate == 1.0
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0

def test_instantiate_from_csv_nonexistent_file():
    """
    Тестирование метода instantiate_from_csv класса Item для несуществующего файла.
    """
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("nonexistent.csv")

def test_string_to_number_decimal():
    """
    Тестирование метода string_to_number класса Item для десятичных чисел.
    """
    assert Item.string_to_number('42.5') == 42

def test_string_to_number_negative():
    """
    Тестирование метода string_to_number класса Item для отрицательных чисел.
    """
    assert Item.string_to_number('-42') == -42

def test_add_method_with_invalid_type():
    """
    Тестирование метода __add__ класса Item с неверным типом объекта.
    """
    item = Item('Test', 10, 1)
    with pytest.raises(ValueError):
        item + "InvalidItem"
