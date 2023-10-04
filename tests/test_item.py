import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item('Товар', 100, 10)


def test_init(item):
    assert item.name == 'Товар'
    assert item.price == 100
    assert item.quantity == 10
    assert len(Item.all) == 1


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 1000


def test_apply_discount(item):
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 90