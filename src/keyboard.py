from accessify import private
from src.item import Item


class LangMixin:
    """Класс для работы с языком клавиатуры."""

    def __init__(self):
        """Установка языка по умолчанию - EN."""
        self.__language = "EN"

    @property
    def language(self):
        """Возвращает текущий язык клавиатуры."""
        return self.__language

    @language.setter
    def language(self, lang):
        """Устанавливает язык клавиатуры."""
        if lang in ("EN", "RU"):
            self.__language = lang

    def change_lang(self, lang):
        """Меняет язык клавиатуры."""
        self.language = lang


class Keyboard(Item, LangMixin):
    """Класс для представления клавиатуры."""

    def __init__(self, name: str, model: str, price: float, language="EN"):
        """Инициализирует атрибуты клавиатуры."""
        super().__init__(name, price, 1)
        LangMixin.__init__(self)
        self.model = model
        self.language = language

    def __str__(self):
        """Возвращает информацию о клавиатуре."""
        return f"{self.name} {self.model}"

    @property
    def language(self):
        """Возвращает язык клавиатуры."""
        return LangMixin.language

    @language.setter
    def language(self, lang):
        """Устанавливает язык клавиатуры."""
        LangMixin.language = lang

    def change_lang(self, lang):
        """Меняет язык клавиатуры."""
        LangMixin.change_lang(self, lang)