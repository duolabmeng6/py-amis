
from amis.AmisComponent import AmisComponent

class Copyable(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "copyable")
        
    