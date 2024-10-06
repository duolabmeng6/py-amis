
from amis.AmisComponent import AmisComponent

class ConditionBuilder(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "condition-builder")
    
    def className(self, className):
        # 外层 dom 类名 可选项: string
        return self.set("className", className)

        
    def fieldClassName(self, fieldClassName):
        # 输入字段的类名 可选项: string
        return self.set("fieldClassName", fieldClassName)

        
    def source(self, source):
        # 通过远程拉取配置项 可选项: string
        return self.set("source", source)

        
    def embed(self, embed):
        # 内嵌展示 可选项: boolean
        return self.set("embed", embed)

        
    def title(self, title):
        # 弹窗配置的顶部标题 可选项: string
        return self.set("title", title)

        
    def fields(self, fields):
        # 字段配置 可选项: 
        return self.set("fields", fields)

        
    def showANDOR(self, showANDOR):
        # 用于 simple 模式下显示切换按钮 可选项: boolean
        return self.set("showANDOR", showANDOR)

        
    def showNot(self, showNot):
        # 是否显示「非」按钮 可选项: boolean
        return self.set("showNot", showNot)

        
    def draggable(self, draggable):
        # 是否可拖拽 可选项: boolean
        return self.set("draggable", draggable)

        
    def searchable(self, searchable):
        # 字段是否可搜索 可选项: boolean
        return self.set("searchable", searchable)

        
    def selectMode(self, selectMode):
        # 组合条件左侧选项类型。`'chained'`模式需要`3.2.0及以上版本` 可选项: list,tree,chained
        return self.set("selectMode", selectMode)

        