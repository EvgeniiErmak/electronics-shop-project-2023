from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, sim_cards: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название телефона.
        :param price: Цена за единицу телефона.
        :param quantity: Количество телефонов в магазине.
        :param sim_cards: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)  # Вызываем конструктор родительского класса Item
        self.sim_cards = sim_cards

    def __add__(self, other):
        """
        Переопределяем оператор сложения для Phone и Item.

        :param other: Другой объект (Phone или Item) для сложения.
        :return: Новый экземпляр класса Phone с обновленным количеством товара.
        """
        if isinstance(other, Phone):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.sim_cards)
        elif isinstance(other, Item):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.sim_cards)
        else:
            raise ValueError("Нельзя сложить Phone с объектом другого класса")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_cards})"
