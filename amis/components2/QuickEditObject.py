
from amis.AmisComponent import AmisComponent

class QuickEditObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "quick-edit-object")
        
    