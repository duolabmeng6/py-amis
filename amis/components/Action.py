
from amis.AmisComponent import AmisComponent

class Action(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "action")
        
    