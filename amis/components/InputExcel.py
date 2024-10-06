
from amis.AmisComponent import AmisComponent

class InputExcel(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-excel")
    
    def allSheets(self, allSheets):
        # 是否解析所有 sheet 可选项: boolean
        return self.set("allSheets", allSheets)

        
    def parseMode(self, parseMode):
        # 解析模式 可选项: array或object
        return self.set("parseMode", parseMode)

        
    def includeEmpty(self, includeEmpty):
        # 是否包含空值 可选项: boolean
        return self.set("includeEmpty", includeEmpty)

        
    def plainText(self, plainText):
        # 是否解析为纯文本 可选项: boolean
        return self.set("plainText", plainText)

        