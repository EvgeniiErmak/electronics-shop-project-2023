class Item:
    # Атрибут класса для хранения уровня цен с учетом скидки
    pay_rate = 1.0

    # Атрибут класса для хранения созданных экземпляров класса
    all_items = []


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all_items.append(self)


    def calculate_total_price(self):
        # Метод для вычисления общей стоимости товара с учетом количества
        return self.price * self.quantity


    def apply_discount(self):
        # Метод для применения скидки к товару
        self.price *= self.pay_rate

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # Устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # Применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all_items)  # [<__main__.Item object at 0x000001EC6250C690>]
                           # [<__main__.Item object at 0x000001EC6250C6D0>]
