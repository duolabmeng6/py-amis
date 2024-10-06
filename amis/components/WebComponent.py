
from amis.AmisComponent import AmisComponent

class WebComponent(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "web-component")
    
    def type(self, type):
        # 指定为 web-component 渲染器 可选项: string
        return self.set("type", type)

        
    def tag(self, tag):
        # 具体使用的 web-component 标签 可选项: string
        return self.set("tag", tag)

        
    def props(self, props):
        # 标签上的属性 可选项: object
        return self.set("props", props)

        
    def body(self, body):
        # 子节点 可选项: [SchemaNode](../../docs/types/schemanode)
        return self.set("body", body)

        