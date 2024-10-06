
from amis.AmisComponent import AmisComponent

class GridNav(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "grid-nav")
    
    def type(self, type):
        #  可选项: string
        return self.set("type", type)

        
    def className(self, className):
        # 外层 CSS 类名 可选项: string
        return self.set("className", className)

        
    def itemClassName(self, itemClassName):
        # 列表项 css 类名 可选项: string
        return self.set("itemClassName", itemClassName)

        
    def contentClassName(self, contentClassName):
        # 列表项内容 css 类名 可选项: string
        return self.set("contentClassName", contentClassName)

        
    def value(self, value):
        # 图片数组 可选项: Array<object>
        return self.set("value", value)

        
    def source(self, source):
        # 数据源 可选项: string
        return self.set("source", source)

        
    def square(self, square):
        # 是否将列表项固定为正方形 可选项: boolean
        return self.set("square", square)

        
    def center(self, center):
        # 是否将列表项内容居中显示 可选项: boolean
        return self.set("center", center)

        
    def border(self, border):
        # 是否显示列表项边框 可选项: boolean
        return self.set("border", border)

        
    def gutter(self, gutter):
        # 列表项之间的间距，默认单位为`px` 可选项: number
        return self.set("gutter", gutter)

        
    def reverse(self, reverse):
        # 是否调换图标和文本的位置 可选项: boolean
        return self.set("reverse", reverse)

        
    def iconRatio(self, iconRatio):
        # 图标宽度占比，单位% 可选项: number
        return self.set("iconRatio", iconRatio)

        
    def direction(self, direction):
        # 列表项内容排列的方向，可选值为 `horizontal` 、`vertical` 可选项: string
        return self.set("direction", direction)

        
    def columnNum(self, columnNum):
        # 列数 可选项: number
        return self.set("columnNum", columnNum)

        