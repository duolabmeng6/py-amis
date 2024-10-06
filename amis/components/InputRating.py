
from amis.AmisComponent import AmisComponent

class InputRating(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-rating")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def value(self, value):
        # 当前值 可选项: number
        return self.set("value", value)

        
    def half(self, half):
        # 是否使用半星选择 可选项: boolean
        return self.set("half", half)

        
    def count(self, count):
        # 总星数 可选项: number
        return self.set("count", count)

        
    def readOnly(self, readOnly):
        # 只读 可选项: boolean
        return self.set("readOnly", readOnly)

        
    def allowClear(self, allowClear):
        # 是否允许再次点击后清除 可选项: boolean
        return self.set("allowClear", allowClear)

        
    def colors(self, colors):
        # 星星被选中的颜色。 若传入字符串，则只有一种颜色。若传入对象，可自定义分段，键名为分段的界限值，键值为对应的类名 可选项: string/object
        return self.set("colors", colors)

        
    def inactiveColor(self, inactiveColor):
        # 未被选中的星星的颜色 可选项: string
        return self.set("inactiveColor", inactiveColor)

        
    def texts(self, texts):
        # 星星被选中时的提示文字。可自定义分段，键名为分段的界限值，键值为对应的类名 可选项: object
        return self.set("texts", texts)

        
    def textPosition(self, textPosition):
        # 文字的位置 可选项: right/left
        return self.set("textPosition", textPosition)

        
    def char(self, char):
        # 自定义字符 可选项: string
        return self.set("char", char)

        
    def className(self, className):
        # 自定义样式类名 可选项: string
        return self.set("className", className)

        
    def charClassName(self, charClassName):
        # 自定义字符类名 可选项: string
        return self.set("charClassName", charClassName)

        
    def textClassName(self, textClassName):
        # 自定义文字类名 可选项: string
        return self.set("textClassName", textClassName)

        