
from amis.AmisComponent import AmisComponent

class InputGroup(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-group")
    