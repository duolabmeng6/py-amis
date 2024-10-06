
from amis.AmisComponent import AmisComponent

class ComboSubControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "combo-sub-control")
        
    