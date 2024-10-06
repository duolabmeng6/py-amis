
from amis.AmisComponent import AmisComponent

class RowSelection(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "row-selection")
        
    
    def type(self, type):
        # 选择类型 单选/多选
        
        return self.set("type", type)

        
    def keyField(self, keyField):
        # 对应数据源的key值
        
        return self.set("keyField", keyField)

        
    def disableOn(self, disableOn):
        # 行是否禁用表达式
        
        return self.set("disableOn", disableOn)

        
    def selections(self, selections):
        # 自定义选择菜单
        
        return self.set("selections", selections)

        
    def selectedRowKeys(self, selectedRowKeys):
        # 已选择的key值
        
        return self.set("selectedRowKeys", selectedRowKeys)

        
    def selectedRowKeysExpr(self, selectedRowKeysExpr):
        # 已选择的key值表达式
        
        return self.set("selectedRowKeysExpr", selectedRowKeysExpr)

        
    def columnWidth(self, columnWidth):
        # 已选择的key值表达式
        
        return self.set("columnWidth", columnWidth)

        
    def rowClick(self, rowClick):
        # 是否点击行触发选中或取消选中
        
        return self.set("rowClick", rowClick)

        