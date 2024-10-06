
from amis.AmisComponent import AmisComponent

class Log(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "log")
    
    def height(self, height):
        # 展示区域高度 可选项: number
        return self.set("height", height)

        
    def className(self, className):
        # 外层 CSS 类名 可选项: string
        return self.set("className", className)

        
    def autoScroll(self, autoScroll):
        # 是否自动滚动 可选项: boolean
        return self.set("autoScroll", autoScroll)

        
    def disableColor(self, disableColor):
        # 是否禁用 ansi 颜色支持 可选项: boolean
        return self.set("disableColor", disableColor)

        
    def placeholder(self, placeholder):
        # 加载中的文字 可选项: string
        return self.set("placeholder", placeholder)

        
    def encoding(self, encoding):
        # 返回内容的字符编码 可选项: string
        return self.set("encoding", encoding)

        
    def source(self, source):
        # 接口 可选项: string
        return self.set("source", source)

        
    def credentials(self, credentials):
        # fetch 的 credentials 设置 可选项: string
        return self.set("credentials", credentials)

        
    def rowHeight(self, rowHeight):
        # 设置每行高度，将会开启虚拟渲染 可选项: number
        return self.set("rowHeight", rowHeight)

        
    def maxLength(self, maxLength):
        # 最大显示行数 可选项: number
        return self.set("maxLength", maxLength)

        
    def operation(self, operation):
        # 可选日志操作：['stop','restart',clear','showLineNumber','filter'] 可选项: Array
        return self.set("operation", operation)

        