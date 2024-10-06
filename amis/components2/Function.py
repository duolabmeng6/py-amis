
from amis.AmisComponent import AmisComponent

class Function(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "function")
        
    