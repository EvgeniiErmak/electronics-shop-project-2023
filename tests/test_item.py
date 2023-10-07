import pytest
from src.item import Item


# Тесты для класса Item
class TestItem:

    @pytest.fixture
    def sample_item(self):
        # Фикстура для создания примера товара
        return Item("Sample Item", 10.0, 5)

    def test_init(self, sample_item):
        """
        Проверяем правильность инициализации объекта Item.
        """
        assert sample_item.name == "Sample Item"
        assert sample_item.price == 10.0
        assert sample_item.quantity == 5

    def test_name_property(self, sample_item):
        """
        Проверяем, что свойство name работает правильно.
        """
        sample_item.name = "A very long name for an item"
        assert sample_item.name == "A very lon"

    def test_calculate_total_price(self, sample_item):
        """
        Проверяем правильность расчета общей стоимости товара.
        """
        assert sample_item.calculate_total_price() == 50.0  # 10.0 * 5

    def test_apply_discount(self, sample_item):
        """
        Проверяем применение скидки к товару.
        """
        sample_item.pay_rate = 0.9  # 10% скидка
        sample_item.apply_discount()
        assert sample_item.price == 9.0  # 10.0 * 0.9

    def test_instantiate_from_csv(self, tmp_path):
        """
        Проверяем инициализацию товаров из CSV-файла.
        """
        # Создаем временный CSV-файл
        csv_data = "name,price,quantity\nItem1,5.0,10\nItem2,8.0,20"
        csv_file = tmp_path / "test_item.csv"
        csv_file.write_text(csv_data)

        # Инициализируем товары из CSV
        Item.instantiate_from_csv(str(csv_file))

        assert len(Item.all) == 2
        assert Item.all[0].name == "Item1"
        assert Item.all[0].price == 5.0
        assert Item.all[0].quantity == 10
        assert Item.all[1].name == "Item2"
        assert Item.all[1].price == 8.0
        assert Item.all[1].quantity == 20
