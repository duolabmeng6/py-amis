
from amis.AmisComponent import AmisComponent

class InputQuarter(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-quarter")
    