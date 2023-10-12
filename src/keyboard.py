class KeyboardLayoutMixin:
    def __init__(self):
        self.layout = "EN"

    def change_layout(self, new_layout):
        layout_options = ["EN", "RU"]
        if new_layout in layout_options:
            self.layout = new_layout

class Keyboard(KeyboardLayoutMixin):
    def __init__(self, name, model, price, language="EN"):
        super().__init__()
        self.name = name
        self.model = model
        self.price = price
        self.language = language if language in ["EN", "RU"] else "EN"

    def change_lang(self, new_language):
        language_options = ["EN", "RU"]
        if new_language in language_options:
            self.language = new_language

    def __str__(self):
        return f"{self.name} {self.model}"
