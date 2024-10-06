
from amis.AmisComponent import AmisComponent

class Number(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "number")
    
    def type(self, type):
        # 如果在 Table、Card 和 List 中，为`"number"`；在 Form 中用作静态展示，为`"static-number"` 或者 `input-number` 配置 static 属性 可选项: string
        return self.set("type", type)

        
    def className(self, className):
        # 外层 CSS 类名 可选项: string
        return self.set("className", className)

        
    def value(self, value):
        # 数值 可选项: string
        return self.set("value", value)

        
    def name(self, name):
        # 在其他组件中，时，用作变量映射 可选项: string
        return self.set("name", name)

        
    def placeholder(self, placeholder):
        # 占位内容 可选项: string
        return self.set("placeholder", placeholder)

        
    def kilobitSeparator(self, kilobitSeparator):
        # 是否千分位展示 可选项: boolean
        return self.set("kilobitSeparator", kilobitSeparator)

        
    def precision(self, precision):
        # 用来控制小数点位数 可选项: number
        return self.set("precision", precision)

        
    def percent(self, percent):
        # 是否用百分比展示，如果是数字，还可以控制百分比小数点位数 可选项: boolean,number
        return self.set("percent", percent)

        
    def prefix(self, prefix):
        # 前缀 可选项: string
        return self.set("prefix", prefix)

        
    def affix(self, affix):
        # 后缀 可选项: string
        return self.set("affix", affix)

        