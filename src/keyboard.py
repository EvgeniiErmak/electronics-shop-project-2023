# Класс-миксин для хранения и изменения раскладки клавиатуры
class KeyboardLayoutMixin:
    def __init__(self):
        self.layout = "EN"  # Изначально устанавливаем раскладку на английскую

    def change_layout(self, new_layout):
        if new_layout in ["EN", "RU"]:
            self.layout = new_layout
            print(f"Раскладка клавиатуры изменена на {new_layout}")
        else:
            print("Неподдерживаемая раскладка. Доступны только 'EN' и 'RU'.")


# Основной класс Keyboard для товара "клавиатура"
class Keyboard(KeyboardLayoutMixin):
    def __init__(self, name, model, price, language="EN"):
        super().__init__()  # Вызываем конструктор миксина
        self.name = name
        self.model = model
        self.price = price
        self.language = language

    def change_lang(self, new_language):
        if new_language in ["EN", "RU"]:
            self.language = new_language
            print(f"Язык клавиатуры изменен на {new_language}")
        else:
            print("Неподдерживаемый язык. Доступны только 'EN' и 'RU'.")

    def __str__(self):
        return f"{self.name} {self.model}"


# Пример использования
if __name__ == "__main__":
    kb = Keyboard("Dark Project", "KD87A", 50, "EN")
    print(f"Товар: {kb}, Цена: {kb.price}, Язык: {kb.language}, Раскладка: {kb.layout}")

    kb.change_lang("RU")
    kb.change_layout("RU")

    print(f"Товар: {kb}, Цена: {kb.price}, Язык: {kb.language}, Раскладка: {kb.layout}")
