
from amis.AmisComponent import AmisComponent

class GroupSubControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "group-sub-control")
        
    