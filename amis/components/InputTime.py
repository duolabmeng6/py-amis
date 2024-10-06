
from amis.AmisComponent import AmisComponent

class InputTime(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-time")
    
    def value(self, value):
        # [默认值](./date#%E9%BB%98%E8%AE%A4%E5%80%BC) 可选项: string
        return self.set("value", value)

        
    def placeholder(self, placeholder):
        # 占位文本 可选项: string
        return self.set("placeholder", placeholder)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def timeConstraints(self, timeConstraints):
        #  可选项: object
        return self.set("timeConstraints", timeConstraints)

        