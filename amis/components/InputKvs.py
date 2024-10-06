
from amis.AmisComponent import AmisComponent

class InputKvs(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-kvs")
    