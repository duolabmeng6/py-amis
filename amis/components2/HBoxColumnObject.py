
from amis.AmisComponent import AmisComponent

class HBoxColumnObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "h-box-column-object")
        
    
    def columnClassName(self, columnClassName):
        # 列上 CSS 类名
        
        return self.set("columnClassName", columnClassName)

        
    def valign(self, valign):
        # 垂直对齐方式# 可选项: ['top', 'middle', 'bottom', 'between']
        
        return self.set("valign", valign)

        
    def width(self, width):
        # 宽度
        
        return self.set("width", width)

        
    def height(self, height):
        # 高度
        
        return self.set("height", height)

        
    def style(self, style):
        # 其他样式
        
        return self.set("style", style)

        
    def mode(self, mode):
        # 配置子表单项默认的展示方式。# 可选项: ['normal', 'inline', 'horizontal']
        
        return self.set("mode", mode)

        
    def horizontal(self, horizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("horizontal", horizontal)

        
    def body(self, body):
        # 内容区
        
        return self.set("body", body)

        
    def visible(self, visible):
        # 是否显示
        
        return self.set("visible", visible)

        
    def visibleOn(self, visibleOn):
        # 是否显示表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("visibleOn", visibleOn)

        