
from amis.AmisComponent import AmisComponent

class Switch(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "switch")
    
    def option(self, option):
        # 选项说明 可选项: string
        return self.set("option", option)

        
    def trueValue(self, trueValue):
        # 标识真值 可选项: boolean,string,number
        return self.set("trueValue", trueValue)

        
    def falseValue(self, falseValue):
        # 标识假值 可选项: boolean,string,number
        return self.set("falseValue", falseValue)

        
    def size(self, size):
        # 开关大小 可选项: "sm","md"
        return self.set("size", size)

        
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        