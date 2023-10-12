import pytest
from src.keyboard import KeyboardLayoutMixin, Keyboard

def test_keyboard_layout_mixin_default_layout():
    """
    Проверка раскладки клавиатуры по умолчанию.
    """
    mixin = KeyboardLayoutMixin()
    assert mixin.layout == "EN"

def test_keyboard_layout_mixin_change_layout_valid_option():
    """
    Проверка изменения раскладки клавиатуры на допустимую опцию.
    """
    mixin = KeyboardLayoutMixin()
    mixin.change_layout("RU")
    assert mixin.layout == "RU"

def test_keyboard_layout_mixin_change_layout_invalid_option():
    """
    Проверка изменения раскладки клавиатуры на недопустимую опцию.
    """
    mixin = KeyboardLayoutMixin()
    mixin.change_layout("CH")
    assert mixin.layout == "EN"

def test_keyboard_default_language():
    """
    Проверка языка клавиатуры по умолчанию.
    """
    keyboard = Keyboard("Название", "Модель", 50)
    assert keyboard.language == "EN"

def test_keyboard_valid_language_option():
    """
    Проверка изменения языка клавиатуры на допустимую опцию.
    """
    keyboard = Keyboard("Название", "Модель", 50)
    keyboard.change_lang("RU")
    assert keyboard.language == "RU"

def test_keyboard_invalid_language_option():
    """
    Проверка изменения языка клавиатуры на недопустимую опцию.
    """
    keyboard = Keyboard("Название", "Модель", 50)
    keyboard.change_lang("CH")
    assert keyboard.language == "EN"

def test_keyboard_string_representation():
    """
    Проверка строкового представления клавиатуры.
    """
    keyboard = Keyboard("Название", "Модель", 50)
    assert str(keyboard) == "Название Модель"

if __name__ == '__main__':
    pytest.main()
