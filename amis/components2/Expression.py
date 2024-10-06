
from amis.AmisComponent import AmisComponent

class Expression(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "expression")
        
    