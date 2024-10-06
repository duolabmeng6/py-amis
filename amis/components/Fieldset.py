
from amis.AmisComponent import AmisComponent

class Fieldset(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "fieldset")
    
    def className(self, className):
        # CSS 类名 可选项: string
        return self.set("className", className)

        
    def headingClassName(self, headingClassName):
        # 标题 CSS 类名 可选项: string
        return self.set("headingClassName", headingClassName)

        
    def bodyClassName(self, bodyClassName):
        # 内容区域 CSS 类名 可选项: string
        return self.set("bodyClassName", bodyClassName)

        
    def title(self, title):
        # 标题 可选项: [SchemaNode](../../../docs/types/schemanode)
        return self.set("title", title)

        
    def body(self, body):
        # 表单项集合 可选项: Array<[表单项](./formitem)>
        return self.set("body", body)

        
    def mode(self, mode):
        # 展示默认，同 [Form](./index#%E8%A1%A8%E5%8D%95%E5%B1%95%E7%A4%BA) 中的模式 可选项: string
        return self.set("mode", mode)

        
    def collapsable(self, collapsable):
        # 是否可折叠 可选项: boolean
        return self.set("collapsable", collapsable)

        
    def collapsed(self, collapsed):
        # 默认是否折叠 可选项: booelan
        return self.set("collapsed", collapsed)

        
    def collapseTitle(self, collapseTitle):
        # 收起的标题 可选项: [SchemaNode](../../../docs/types/schemanode)
        return self.set("collapseTitle", collapseTitle)

        
    def size(self, size):
        # 大小，支持 xs、sm、base、md、lg 可选项: string
        return self.set("size", size)

        