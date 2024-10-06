
from amis.AmisComponent import AmisComponent

class InputCity(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-city")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def allowCity(self, allowCity):
        # 允许选择城市 可选项: boolean
        return self.set("allowCity", allowCity)

        
    def allowDistrict(self, allowDistrict):
        # 允许选择区域 可选项: boolean
        return self.set("allowDistrict", allowDistrict)

        
    def searchable(self, searchable):
        # 是否出搜索框 可选项: boolean
        return self.set("searchable", searchable)

        
    def extractValue(self, extractValue):
        # 默认 `true` 是否抽取值，如果设置成 `false` 值格式会变成对象，包含 `code`、`province`、`city` 和 `district` 文字信息。 可选项: boolean
        return self.set("extractValue", extractValue)

        