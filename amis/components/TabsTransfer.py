
from amis.AmisComponent import AmisComponent

class TabsTransfer(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tabs-transfer")
    