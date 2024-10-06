
from amis.AmisComponent import AmisComponent

class RowSelectionOptions(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "row-selection-options")
        
    
    def key(self, key):
        # 选择类型 选择全部
        
        return self.set("key", key)

        
    def text(self, text):
        # 选项显示文本
        
        return self.set("text", text)

        