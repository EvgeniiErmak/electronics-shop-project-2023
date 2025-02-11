from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название телефона.
        :param price: Цена за единицу телефона.
        :param quantity: Количество телефонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)  # Вызываем конструктор родительского класса Item
        self.number_of_sim = number_of_sim  # Заменяем sim_cards на number_of_sim

    def __add__(self, other):
        """
        Переопределяем оператор сложения для Phone и Item.

        :param other: Другой объект (Phone или Item) для сложения.
        :return: Новый экземпляр класса Phone с обновленным количеством товара.
        """
        if isinstance(other, Phone):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.number_of_sim)  # Заменяем sim_cards на number_of_sim
        elif isinstance(other, Item):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.number_of_sim)  # Заменяем sim_cards на number_of_sim
        else:
            raise ValueError("Нельзя сложить Phone с объектом другого класса")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"  # Заменяем sim_cards на number_of_sim
