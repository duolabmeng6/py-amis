
from amis.AmisComponent import AmisComponent

class Control(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "control")
    