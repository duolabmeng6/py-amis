
from amis.AmisComponent import AmisComponent

class IconItem(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "icon-item")
        
    
    def icon(self, icon):
        
        # iconfont 里面的类名。
        return self.set("icon", icon)

        
    def position(self, position):
        
        
        return self.set("position", position)

        