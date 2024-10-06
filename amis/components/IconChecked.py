
from amis.AmisComponent import AmisComponent

class IconChecked(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "icon-checked")
        
    
    def id(self, id):
        
        
        return self.set("id", id)

        
    def name(self, name):
        
        
        return self.set("name", name)

        
    def svg(self, svg):
        
        
        return self.set("svg", svg)

        