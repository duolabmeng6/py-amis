
from amis.AmisComponent import AmisComponent

class PlainObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "plain-object")
        
    