
from amis.AmisComponent import AmisComponent

class InputTimeRange(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-time-range")
    
    def placeholder(self, placeholder):
        # 占位文本 可选项: string
        return self.set("placeholder", placeholder)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def embed(self, embed):
        # 是否内联模式 可选项: boolean
        return self.set("embed", embed)

        