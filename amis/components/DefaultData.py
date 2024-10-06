
from amis.AmisComponent import AmisComponent

class DefaultData(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "default-data")
        
    