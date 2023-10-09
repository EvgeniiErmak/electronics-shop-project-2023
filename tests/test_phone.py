import pytest
from src.item import Item
from src.phone import Phone

# Создаем фикстуру для инициализации объекта Phone перед каждым тестом
@pytest.fixture
def phone():
    return Phone("Phone A", 500.0, 10, 2)

# Тестируем конструктор
def test_phone_constructor(phone):
    assert phone.name == "Phone A"
    assert phone.price == 500.0
    assert phone.quantity == 10
    assert phone.sim_cards == 2

# Тестируем метод __add__
def test_phone_add(phone):
    item = Item("Item A", 100.0, 5)
    new_phone = phone + item
    assert isinstance(new_phone, Phone)
    assert new_phone.name == "Phone A"
    assert new_phone.price == 500.0
    assert new_phone.quantity == 15  # 10 + 5
    assert new_phone.sim_cards == 2

# Тестируем метод __repr__
def test_phone_repr(phone):
    expected_repr = "Phone('Phone A', 500.0, 10, 2)"
    assert repr(phone) == expected_repr

# Тестируем исключение при сложении с объектом другого класса
def test_phone_add_with_wrong_class(phone):
    with pytest.raises(ValueError):
        phone + "InvalidItem"
