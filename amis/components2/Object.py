
from amis.AmisComponent import AmisComponent

class Object(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "object")
        
    