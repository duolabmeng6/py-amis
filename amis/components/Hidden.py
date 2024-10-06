
from amis.AmisComponent import AmisComponent

class Hidden(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "hidden")
    