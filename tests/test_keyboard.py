import pytest
from src.keyboard import Keyboard

# Тестирование класса Keyboard

def test_keyboard_init():
    kb = Keyboard("Dark Project", "KD87A", 50, "EN")
    assert kb.name == "Dark Project"
    assert kb.model == "KD87A"
    assert kb.price == 50
    assert kb.language == "EN"
    assert kb.layout == "EN"

def test_keyboard_change_lang():
    kb = Keyboard("Dark Project", "KD87A", 50, "EN")
    kb.change_lang("RU")
    assert kb.language == "RU"

    kb.change_lang("EN")
    assert kb.language == "EN"

def test_keyboard_change_layout():
    kb = Keyboard("Dark Project", "KD87A", 50, "EN")
    kb.change_layout("RU")
    assert kb.layout == "RU"

    kb.change_layout("EN")
    assert kb.layout == "EN"

def test_keyboard_str():
    kb = Keyboard("Dark Project", "KD87A", 50, "EN")
    assert str(kb) == "Dark Project KD87A"

# Запуск тестов
if __name__ == '__main__':
    pytest.main()
