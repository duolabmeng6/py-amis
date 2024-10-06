
from amis.AmisComponent import AmisComponent

class InputYear(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-year")
    