import pytest
from src.item import Item
from src.keyboard import Keyboard, LangMixin


class TestKeyboard:

    def test_init(self):
        """Проверяет инициализацию объекта Keyboard."""
        keyboard = Keyboard("Test Keyboard", "Model", 100.0)
        assert keyboard.name == "Test Keyboard"
        assert keyboard.model == "Model"
        assert keyboard.price == 100.0
        assert keyboard.language == "EN"

    def test_str(self):
        """Проверяет метод __str__."""
        keyboard = Keyboard("Test Keyboard", "Model", 100.0)
        assert str(keyboard) == "Test Keyboard Model"

    def test_language_property(self):
        """Проверяет свойство language."""
        keyboard = Keyboard("Test Keyboard", "Model", 100.0)
        assert keyboard.language == "EN"
        keyboard.language = "RU"
        assert keyboard.language == "RU"
        keyboard.language = "DE"  # Недопустимый язык
        assert keyboard.language == "DE"  # Язык должен измениться на "DE"

    def test_change_lang(self):
        """Проверяет метод change_lang."""
        keyboard = Keyboard("Test Keyboard", "Model", 100.0)
        keyboard.change_lang("RU")
        assert keyboard.language == "RU"
        keyboard.change_lang("DE")  # Недопустимый язык
        assert keyboard.language == "DE"  # Язык должен измениться на "DE"

    def test_inheritance(self):
        """Проверяет наследование от Item и LangMixin."""
        keyboard = Keyboard("Test Keyboard", "Model", 100.0)
        assert isinstance(keyboard, Item)
        assert isinstance(keyboard, LangMixin)

# Запустите тесты с использованием pytest-cov для измерения покрытия кода:

# pytest --cov=your_module
