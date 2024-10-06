
from amis.AmisComponent import AmisComponent

class Barcode(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "barcode")
    
    def className(self, className):
        # 外层 CSS 类名 可选项: string
        return self.set("className", className)

        
    def value(self, value):
        # 显示的颜色值 可选项: string
        return self.set("value", value)

        
    def name(self, name):
        # 在其他组件中，时，用作变量映射 可选项: string
        return self.set("name", name)

        