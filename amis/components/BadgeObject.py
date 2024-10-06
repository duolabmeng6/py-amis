
from amis.AmisComponent import AmisComponent

class BadgeObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "badge-object")
        
    
    def className(self, className):
        
        
        return self.set("className", className)

        
    def text(self, text):
        # 文本内容
        
        return self.set("text", text)

        
    def size(self, size):
        # 大小
        
        return self.set("size", size)

        
    def mode(self, mode):
        # 角标类型# 可选项: ['text', 'dot', 'ribbon']
        
        return self.set("mode", mode)

        
    def offset(self, offset):
        # 角标位置，相对于position的位置进行偏移
        
        return self.set("offset", offset)

        
    def position(self, position):
        # 角标位置# 可选项: ['top-right', 'top-left', 'bottom-right', 'bottom-left']
        
        return self.set("position", position)

        
    def overflowCount(self, overflowCount):
        # 封顶的数字值
        
        return self.set("overflowCount", overflowCount)

        
    def visibleOn(self, visibleOn):
        # 动态控制是否显示
        
        return self.set("visibleOn", visibleOn)

        
    def animation(self, animation):
        # 是否显示动画
        
        return self.set("animation", animation)

        
    def style(self, style):
        # 角标的自定义样式
        
        return self.set("style", style)

        
    def level(self, level):
        # 提示类型
        
        return self.set("level", level)

        