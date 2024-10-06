
from amis.AmisComponent import AmisComponent

class AutoFillHeightObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "auto-fill-height-object")
        
    
    def height(self, height):
        
        
        return self.set("height", height)

        
    def maxHeight(self, maxHeight):
        
        
        return self.set("maxHeight", maxHeight)

        