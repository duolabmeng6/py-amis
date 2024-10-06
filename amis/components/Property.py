
from amis.AmisComponent import AmisComponent

class Property(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "property")
    
    def className(self, className):
        # 外层 dom 的类名 可选项: string
        return self.set("className", className)

        
    def style(self, style):
        # 外层 dom 的样式 可选项: object
        return self.set("style", style)

        
    def labelStyle(self, labelStyle):
        # 属性名的样式 可选项: object
        return self.set("labelStyle", labelStyle)

        
    def contentStyle(self, contentStyle):
        # 属性值的样式 可选项: object
        return self.set("contentStyle", contentStyle)

        
    def column(self, column):
        # 每行几列 可选项: number
        return self.set("column", column)

        
    def mode(self, mode):
        # 显示模式，目前只有 'table' 和 'simple' 可选项: string
        return self.set("mode", mode)

        
    def separator(self, separator):
        # 'simple' 模式下属性名和值之间的分隔符 可选项: string
        return self.set("separator", separator)

        
    def title(self, title):
        # 标题 可选项: string
        return self.set("title", title)

        
    def source(self, source):
        # 数据源 可选项: string
        return self.set("source", source)

        