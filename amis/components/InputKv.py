
from amis.AmisComponent import AmisComponent

class InputKv(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-kv")
    
    def valueType(self, valueType):
        # 值类型 可选项: type
        return self.set("valueType", valueType)

        
    def keyPlaceholder(self, keyPlaceholder):
        # key 的提示信息的 可选项: string
        return self.set("keyPlaceholder", keyPlaceholder)

        
    def valuePlaceholder(self, valuePlaceholder):
        # value 的提示信息的 可选项: string
        return self.set("valuePlaceholder", valuePlaceholder)

        
    def draggable(self, draggable):
        # 是否可拖拽排序 可选项: boolean
        return self.set("draggable", draggable)

        
    def defaultValue(self, defaultValue):
        # 默认值 可选项: 
        return self.set("defaultValue", defaultValue)

        
    def autoParseJSON(self, autoParseJSON):
        # 是否自动转换 json 对象字符串 可选项: boolean
        return self.set("autoParseJSON", autoParseJSON)

        