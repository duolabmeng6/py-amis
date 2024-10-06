
from amis.AmisComponent import AmisComponent

class Name(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "name")
        
    