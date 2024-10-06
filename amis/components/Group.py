
from amis.AmisComponent import AmisComponent

class Group(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "group")
    
    def className(self, className):
        # CSS 类名 可选项: string
        return self.set("className", className)

        
    def label(self, label):
        # group 的标签 可选项: string
        return self.set("label", label)

        
    def body(self, body):
        # 表单项集合 可选项: Array<[表单项](./formitem)>
        return self.set("body", body)

        
    def mode(self, mode):
        # 展示默认，同 [Form](./index#%E8%A1%A8%E5%8D%95%E5%B1%95%E7%A4%BA) 中的模式 可选项: string
        return self.set("mode", mode)

        
    def gap(self, gap):
        # 表单项之间的间距，可选：`xs`、`sm`、`normal` 可选项: string
        return self.set("gap", gap)

        
    def direction(self, direction):
        # 可以配置水平展示还是垂直展示。对应的配置项分别是：`vertical`、`horizontal` 可选项: string
        return self.set("direction", direction)

        