
from amis.AmisComponent import AmisComponent

class Markdown(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "markdown")
    
    def name(self, name):
        # 名称 可选项: string
        return self.set("name", name)

        
    def value(self, value):
        # 静态值 可选项: string
        return self.set("value", value)

        
    def className(self, className):
        # 类名 可选项: string
        return self.set("className", className)

        
    def src(self, src):
        # 外部地址 可选项: Api
        return self.set("src", src)

        