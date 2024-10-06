
from amis.AmisComponent import AmisComponent

class OfficeViewer(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "office-viewer")
    
    def src(self, src):
        # 文档地址 可选项: Api
        return self.set("src", src)

        
    def loading(self, loading):
        # 是否显示 loading 图标 可选项: boolean
        return self.set("loading", loading)

        
    def enableVar(self, enableVar):
        # 是否开启变量替换功能 可选项: boolean
        return self.set("enableVar", enableVar)

        
    def wordOptions(self, wordOptions):
        # Word 渲染配置 可选项: object
        return self.set("wordOptions", wordOptions)

        