
from amis.AmisComponent import AmisComponent

class TableView(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "table-view")
    