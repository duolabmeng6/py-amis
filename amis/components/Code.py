
from amis.AmisComponent import AmisComponent

class Code(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "code")
    
    def className(self, className):
        # 外层 CSS 类名 可选项: string
        return self.set("className", className)

        
    def value(self, value):
        # 显示的颜色值 可选项: string
        return self.set("value", value)

        
    def name(self, name):
        # 在其他组件中，时，用作变量映射 可选项: string
        return self.set("name", name)

        
    def language(self, language):
        # 所使用的高亮语言，默认是 plaintext 可选项: string
        return self.set("language", language)

        
    def tabSize(self, tabSize):
        # 默认 tab 大小 可选项: number
        return self.set("tabSize", tabSize)

        
    def editorTheme(self, editorTheme):
        # 主题，还有 'vs-dark' 可选项: string
        return self.set("editorTheme", editorTheme)

        
    def wordWrap(self, wordWrap):
        # 是否折行 可选项: string
        return self.set("wordWrap", wordWrap)

        
    def maxHeight(self, maxHeight):
        # 最大高度 可选项: string,number
        return self.set("maxHeight", maxHeight)

        