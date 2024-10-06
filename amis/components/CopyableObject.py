
from amis.AmisComponent import AmisComponent

class CopyableObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "copyable-object")
        
    
    def icon(self, icon):
        # 可以配置图标
        # iconfont 里面的类名。
        return self.set("icon", icon)

        
    def content(self, content):
        # 配置复制时的内容模板。
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("content", content)

        
    def tooltip(self, tooltip):
        # 提示文字内容
        
        return self.set("tooltip", tooltip)

        