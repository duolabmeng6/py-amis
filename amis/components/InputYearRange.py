
from amis.AmisComponent import AmisComponent

class InputYearRange(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-year-range")
    
    def placeholder(self, placeholder):
        # 占位文本 可选项: string
        return self.set("placeholder", placeholder)

        
    def minDate(self, minDate):
        # 限制最小日期，用法同 [限制范围](./date#%E9%99%90%E5%88%B6%E8%8C%83%E5%9B%B4) 可选项: string
        return self.set("minDate", minDate)

        
    def maxDate(self, maxDate):
        # 限制最大日期，用法同 [限制范围](./date#%E9%99%90%E5%88%B6%E8%8C%83%E5%9B%B4) 可选项: string
        return self.set("maxDate", maxDate)

        
    def minDuration(self, minDuration):
        # 限制最小跨度，如： 2year 可选项: string
        return self.set("minDuration", minDuration)

        
    def maxDuration(self, maxDuration):
        # 限制最大跨度，如：4year 可选项: string
        return self.set("maxDuration", maxDuration)

        
    def utc(self, utc):
        # [保存 UTC 值](./date#utc) 可选项: boolean
        return self.set("utc", utc)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def embed(self, embed):
        # 是否内联模式 可选项: boolean
        return self.set("embed", embed)

        