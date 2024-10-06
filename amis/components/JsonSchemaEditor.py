
from amis.AmisComponent import AmisComponent

class JsonSchemaEditor(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "json-schema-editor")
    
    def rootTypeMutable(self, rootTypeMutable):
        # 顶级类型是否可配置 可选项: boolean
        return self.set("rootTypeMutable", rootTypeMutable)

        
    def showRootInfo(self, showRootInfo):
        # 是否显示顶级类型信息 可选项: boolean
        return self.set("showRootInfo", showRootInfo)

        
    def disabledTypes(self, disabledTypes):
        # 用来禁用默认数据类型，默认类型有：string、number、interger、object、number、array、boolean、null 可选项: Array<string>
        return self.set("disabledTypes", disabledTypes)

        
    def definitions(self, definitions):
        # 用来配置预设类型 可选项: object
        return self.set("definitions", definitions)

        
    def mini(self, mini):
        # 用来开启迷你模式，适应于边栏面板，宽度较低的情况 可选项: boolean
        return self.set("mini", mini)

        