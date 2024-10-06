
from amis.AmisComponent import AmisComponent

class ObjectListBodyField(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "object-list-body-field")
        
    