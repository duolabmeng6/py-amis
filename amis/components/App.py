
from amis.AmisComponent import AmisComponent

class App(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "app")
    