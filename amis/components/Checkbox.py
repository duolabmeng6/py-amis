
from amis.AmisComponent import AmisComponent

class Checkbox(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "checkbox")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def option(self, option):
        # 选项说明 可选项: string
        return self.set("option", option)

        
    def trueValue(self, trueValue):
        # 标识真值 可选项: string｜number｜boolean
        return self.set("trueValue", trueValue)

        
    def falseValue(self, falseValue):
        # 标识假值 可选项: string｜number｜boolean
        return self.set("falseValue", falseValue)

        
    def optionType(self, optionType):
        # 设置 option 类型 可选项: default｜button
        return self.set("optionType", optionType)

        