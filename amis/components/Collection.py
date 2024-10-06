
from amis.AmisComponent import AmisComponent

class Collection(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "collection")
        
    