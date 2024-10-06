
from amis.AmisComponent import AmisComponent

class UrlPath(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "url-path")
        
    