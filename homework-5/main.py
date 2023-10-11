from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project', 'KD87A', 9600, 'EN')
    assert str(kb) == "Dark Project KD87A"

    assert kb.language == "EN"

    kb.change_lang("RU")  # Устанавливаем язык "RU"
    assert kb.language == "RU"

    # Сделали RU -> EN
    kb.change_lang("EN")  # Возвращаем язык на "EN"
    assert kb.language == "EN"

    # Попробовать установить неподдерживаемый язык
    kb.language = 'CH'  # Это должно вызвать ошибку, так как "CH" не поддерживается
