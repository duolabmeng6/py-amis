
from amis.AmisComponent import AmisComponent

class Tooltip(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tooltip")
        
    