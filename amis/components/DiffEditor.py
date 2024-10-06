
from amis.AmisComponent import AmisComponent

class DiffEditor(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "diff-editor")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def language(self, language):
        # 编辑器高亮的语言，可选 [支持的语言](./editor#%E6%94%AF%E6%8C%81%E7%9A%84%E8%AF%AD%E8%A8%80) 可选项: string
        return self.set("language", language)

        
    def diffValue(self, diffValue):
        # 左侧值 可选项: [Tpl](../tpl)
        return self.set("diffValue", diffValue)

        