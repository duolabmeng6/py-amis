
from amis.AmisComponent import AmisComponent

class QuickEdit(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "quick-edit")
        
    