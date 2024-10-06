
from amis.AmisComponent import AmisComponent

class CRUD(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "crud")
        
    