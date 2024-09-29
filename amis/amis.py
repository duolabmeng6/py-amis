from amis.component.button import button
from amis.component.page import page


class Amis:
    @staticmethod
    def button() -> button:
        return button()

    @staticmethod
    def page() -> page:
        return page()

def amis() -> Amis:
    return Amis()

