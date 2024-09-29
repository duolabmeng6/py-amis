from amis.component.AmisButton import AmisButton
from amis.component.AmisPage import AmisPage


class Amis:
    @staticmethod
    def button() -> AmisButton:
        return AmisButton()

    @staticmethod
    def page() -> AmisPage:
        return AmisPage()

def amis() -> Amis:
    return Amis()

