
from amis.AmisComponent import AmisComponent

class Expandable(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "expandable")
        
    
    def type(self, type):
        # 对应渲染器类型
        
        return self.set("type", type)

        
    def keyField(self, keyField):
        # 对应数据源的key值
        
        return self.set("keyField", keyField)

        
    def expandableOn(self, expandableOn):
        # 行是否可展开表达式
        
        return self.set("expandableOn", expandableOn)

        
    def expandedRowClassNameExpr(self, expandedRowClassNameExpr):
        # 展开行自定义样式表达式
        
        return self.set("expandedRowClassNameExpr", expandedRowClassNameExpr)

        
    def expandedRowKeys(self, expandedRowKeys):
        # 已展开的key值
        
        return self.set("expandedRowKeys", expandedRowKeys)

        
    def expandedRowKeysExpr(self, expandedRowKeysExpr):
        # 已展开的key值表达式
        
        return self.set("expandedRowKeysExpr", expandedRowKeysExpr)

        