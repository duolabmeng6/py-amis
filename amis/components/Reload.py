
from amis.AmisComponent import AmisComponent

class Reload(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "reload")
        
    