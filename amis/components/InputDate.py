
from amis.AmisComponent import AmisComponent

class InputDate(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-date")
    
    def value(self, value):
        # [默认值](./date#%E9%BB%98%E8%AE%A4%E5%80%BC) 可选项: string
        return self.set("value", value)

        
    def closeOnSelect(self, closeOnSelect):
        # 点选日期后，是否马上关闭选择框 可选项: boolean
        return self.set("closeOnSelect", closeOnSelect)

        
    def placeholder(self, placeholder):
        # 占位文本 可选项: string
        return self.set("placeholder", placeholder)

        
    def minDate(self, minDate):
        # 限制最小日期 可选项: string
        return self.set("minDate", minDate)

        
    def maxDate(self, maxDate):
        # 限制最大日期 可选项: string
        return self.set("maxDate", maxDate)

        
    def utc(self, utc):
        # 保存 utc 值 可选项: boolean
        return self.set("utc", utc)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def embed(self, embed):
        # 是否内联模式 可选项: boolean
        return self.set("embed", embed)

        
    def disabledDate(self, disabledDate):
        # 用字符函数来控制哪些天不可以被点选 可选项: string
        return self.set("disabledDate", disabledDate)

        