from accessify import private, protected
import csv

class InstantiateCSVError(Exception):
    """
    Класс исключения для ошибок при инициализации из CSV.
    """
    def __init__(self, message):
        super().__init__(message)

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    data = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # Добавляем созданный экземпляр в атрибут класса

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """
        Переопределяем оператор сложения для Item.

        :param other: Другой объект (Item) для сложения.
        :return: Новый экземпляр класса Item с обновленным количеством товара.
        """
        if isinstance(other, Item):
            return Item(self.name, self.price, self.quantity + other.quantity)
        else:
            raise ValueError("Нельзя сложить Item с объектом другого класса")

    @classmethod
    def instantiate_from_csv(cls, filename: str = '../src/items.csv'):
        """
        Инициализируем экземпляры класса из файла item.csv.

        :param filename: Имя файла CSV.
        """
        try:
            with open(filename, 'r', newline='') as file:
                data = csv.DictReader(file)
                items = []
                for data_ in data:
                    try:
                        name = data_['name']
                        price = float(data_['price'])
                        quantity = int(data_['quantity'])
                    except KeyError:
                        raise InstantiateCSVError("Файл item.csv поврежден: отсутствует одна из колонок данных")
                    item = cls(name, price, quantity)
                    items.append(item)

                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(str_number: str):
        """
        Возвращает из строки число в int.
        """
        number = str_number.split('.')
        return int(number[0])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
