
from amis.AmisComponent import AmisComponent

class Textarea(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "textarea")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def minRows(self, minRows):
        # 最小行数 可选项: number
        return self.set("minRows", minRows)

        
    def maxRows(self, maxRows):
        # 最大行数 可选项: number
        return self.set("maxRows", maxRows)

        
    def trimContents(self, trimContents):
        # 是否去除首尾空白文本 可选项: boolean
        return self.set("trimContents", trimContents)

        
    def readOnly(self, readOnly):
        # 是否只读 可选项: boolean
        return self.set("readOnly", readOnly)

        
    def showCounter(self, showCounter):
        # 是否显示计数器 可选项: boolean
        return self.set("showCounter", showCounter)

        
    def maxLength(self, maxLength):
        # 限制最大字数 可选项: number
        return self.set("maxLength", maxLength)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def resetValue(self, resetValue):
        # 清除后设置此配置项给定的值。 可选项: string
        return self.set("resetValue", resetValue)

        