
from amis.AmisComponent import AmisComponent

class Index(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "index")
    