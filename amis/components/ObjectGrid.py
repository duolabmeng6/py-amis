
from amis.AmisComponent import AmisComponent

class ObjectGrid(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "object-grid")
        
    