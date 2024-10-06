
from amis.AmisComponent import AmisComponent

class ObjectTableColumnWithType(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "object-table-column-with-type")
        
    