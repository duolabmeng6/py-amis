
from amis.AmisComponent import AmisComponent

class PopOver(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "pop-over")
        
    