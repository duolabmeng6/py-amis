
from amis.AmisComponent import AmisComponent

class ImageToolbarAction(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "image-toolbar-action")
        
    
    def key(self, key):
        # 可选项: ['ROTATE_RIGHT', 'ROTATE_LEFT', 'ZOOM_IN', 'ZOOM_OUT', 'SCALE_ORIGIN']
        
        return self.set("key", key)

        
    def label(self, label):
        
        
        return self.set("label", label)

        
    def icon(self, icon):
        
        
        return self.set("icon", icon)

        
    def iconClassName(self, iconClassName):
        
        
        return self.set("iconClassName", iconClassName)

        
    def disabled(self, disabled):
        
        
        return self.set("disabled", disabled)

        