
from amis.AmisComponent import AmisComponent

class Uuid(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "uuid")
    