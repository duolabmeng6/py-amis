
from amis.AmisComponent import AmisComponent

class Treeselect(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "treeselect")
    