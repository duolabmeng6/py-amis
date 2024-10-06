
from amis.AmisComponent import AmisComponent

class ObjectCardBodyField(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "object-card-body-field")
        
    