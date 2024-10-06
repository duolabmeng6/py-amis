
from amis.AmisComponent import AmisComponent

class Static(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "static")
    