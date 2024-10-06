
from amis.AmisComponent import AmisComponent

class Amis(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "amis")
    
    def type(self, type):
        # 指定为 amis 渲染器 可选项: string
        return self.set("type", type)

        
    def name(self, name):
        # 绑定上下文变量名 可选项: string
        return self.set("name", name)

        
    def props(self, props):
        # 向下传递的 props 可选项: object
        return self.set("props", props)

        