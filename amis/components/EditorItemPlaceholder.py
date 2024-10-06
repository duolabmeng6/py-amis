
from amis.AmisComponent import AmisComponent

class EditorItemPlaceholder(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "editor-item-placeholder")
        
    
    def key(self, key):
        
        
        return self.set("key", key)

        
    def title(self, title):
        
        
        return self.set("title", title)

        
    def description(self, description):
        
        
        return self.set("description", description)

        
    def default(self, default):
        
        
        return self.set("default", default)

        
    def empty(self, empty):
        
        
        return self.set("empty", empty)

        