
from amis.AmisComponent import AmisComponent

class Unkown(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "unkown")
        
    