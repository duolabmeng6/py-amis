
from amis.AmisComponent import AmisComponent

class PopOverObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "pop-over-object")
        
    
    def className(self, className):
        # 类名
        
        return self.set("className", className)

        
    def popOverClassName(self, popOverClassName):
        # 弹框外层类名
        
        return self.set("popOverClassName", popOverClassName)

        
    def popOverEnableOn(self, popOverEnableOn):
        # 配置当前行是否启动，要用表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("popOverEnableOn", popOverEnableOn)

        
    def mode(self, mode):
        # 弹出模式# 可选项: ['dialog', 'drawer', 'popOver']
        
        return self.set("mode", mode)

        
    def size(self, size):
        # 是弹窗形式的时候有用。# 可选项: ['sm', 'md', 'lg', 'xl']
        
        return self.set("size", size)

        
    def position(self, position):
        # 弹出位置# 可选项: ['center', 'left-top', 'left-top-left-top', 'left-top-left-center', 'left-top-left-bottom', 'left-top-center-top', 'left-top-center-center', 'left-top-center-bottom', 'left-top-right-top', 'left-top-right-center', 'left-top-right-bottom', 'right-top', 'right-top-left-top', 'right-top-left-center', 'right-top-left-bottom', 'right-top-center-top', 'right-top-center-center', 'right-top-center-bottom', 'right-top-right-top', 'right-top-right-center', 'right-top-right-bottom', 'left-bottom', 'left-bottom-left-top', 'left-bottom-left-center', 'left-bottom-left-bottom', 'left-bottom-center-top', 'left-bottom-center-center', 'left-bottom-center-bottom', 'left-bottom-right-top', 'left-bottom-right-center', 'left-bottom-right-bottom', 'right-bottom', 'right-bottom-left-top', 'right-bottom-left-center', 'right-bottom-left-bottom', 'right-bottom-center-top', 'right-bottom-center-center', 'right-bottom-center-bottom', 'right-bottom-right-top', 'right-bottom-right-center', 'right-bottom-right-bottom', 'fixed-center', 'fixed-left-top', 'fixed-right-top', 'fixed-left-bottom', 'fixed-right-bottom']
        
        return self.set("position", position)

        
    def trigger(self, trigger):
        # 触发条件，默认是 click# 可选项: ['click', 'hover']
        
        return self.set("trigger", trigger)

        
    def showIcon(self, showIcon):
        # 是否显示查看更多的 icon，通常是放大图标。
        
        return self.set("showIcon", showIcon)

        
    def offset(self, offset):
        # 偏移量
        
        return self.set("offset", offset)

        
    def title(self, title):
        # 标题
        
        return self.set("title", title)

        
    def body(self, body):
        
        
        return self.set("body", body)

        