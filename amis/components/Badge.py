
from amis.AmisComponent import AmisComponent

class Badge(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "badge")
    
    def mode(self, mode):
        # 角标类型，可以是 dot/text/ribbon 可选项: string
        return self.set("mode", mode)

        
    def text(self, text):
        # 角标文案，支持字符串和数字，在 mode='dot'下设置无效 可选项: string,number
        return self.set("text", text)

        
    def size(self, size):
        # 角标大小 可选项: number
        return self.set("size", size)

        
    def level(self, level):
        # 角标级别, 可以是 info/success/warning/danger, 设置之后角标背景颜色不同 可选项: string
        return self.set("level", level)

        
    def overflowCount(self, overflowCount):
        # 设置封顶的数字值 可选项: number
        return self.set("overflowCount", overflowCount)

        
    def position(self, position):
        # 角标位置， 可以是 top-right/top-left/bottom-right/bottom-left 可选项: string
        return self.set("position", position)

        
    def offset(self, offset):
        # 角标位置，offset 相对于 position 位置进行水平、垂直偏移 可选项: number[top,left]
        return self.set("offset", offset)

        
    def className(self, className):
        # 外层 dom 的类名 可选项: string
        return self.set("className", className)

        
    def animation(self, animation):
        # 角标是否显示动画 可选项: boolean
        return self.set("animation", animation)

        
    def style(self, style):
        # 角标的自定义样式 可选项: object
        return self.set("style", style)

        
    def visibleOn(self, visibleOn):
        # 控制角标的显示隐藏 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("visibleOn", visibleOn)

        