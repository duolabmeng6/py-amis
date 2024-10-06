
from amis.AmisComponent import AmisComponent

class Root(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "root")
        
    