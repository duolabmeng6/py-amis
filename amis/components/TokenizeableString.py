
from amis.AmisComponent import AmisComponent

class TokenizeableString(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tokenizeable-string")
        
    