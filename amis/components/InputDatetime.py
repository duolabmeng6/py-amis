
from amis.AmisComponent import AmisComponent

class InputDatetime(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-datetime")
    
    def value(self, value):
        # [默认值](./datetime#%E9%BB%98%E8%AE%A4%E5%80%BC) 可选项: string
        return self.set("value", value)

        
    def placeholder(self, placeholder):
        # 占位文本 可选项: string
        return self.set("placeholder", placeholder)

        
    def minDate(self, minDate):
        # 限制最小日期时间 可选项: string
        return self.set("minDate", minDate)

        
    def maxDate(self, maxDate):
        # 限制最大日期时间 可选项: string
        return self.set("maxDate", maxDate)

        
    def utc(self, utc):
        # 保存 utc 值 可选项: boolean
        return self.set("utc", utc)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def embed(self, embed):
        # 是否内联 可选项: boolean
        return self.set("embed", embed)

        
    def timeConstraints(self, timeConstraints):
        # 请参考 [input-time](./input-time#控制输入范围) 里的说明 可选项: object
        return self.set("timeConstraints", timeConstraints)

        
    def isEndDate(self, isEndDate):
        # 如果配置为 true，会自动默认为 23:59:59 秒 可选项: boolean
        return self.set("isEndDate", isEndDate)

        
    def disabledDate(self, disabledDate):
        # 用字符函数来控制哪些天不可以被点选 可选项: string
        return self.set("disabledDate", disabledDate)

        