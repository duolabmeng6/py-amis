
from amis.AmisComponent import AmisComponent

class InputArray(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-array")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def type(self, type):
        # 指明为`array`组件 可选项: string
        return self.set("type", type)

        
    def items(self, items):
        # 配置单项表单类型 可选项: [SchemaNode](../../docs/types/schemanode)
        return self.set("items", items)

        
    def addable(self, addable):
        # 是否可新增。 可选项: boolean
        return self.set("addable", addable)

        
    def removable(self, removable):
        # 是否可删除 可选项: boolean
        return self.set("removable", removable)

        
    def draggable(self, draggable):
        # 是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个\$id 字段 可选项: boolean
        return self.set("draggable", draggable)

        
    def draggableTip(self, draggableTip):
        # 可拖拽的提示文字，默认为：`"可通过拖动每行中的【交换】按钮进行顺序调整"` 可选项: string
        return self.set("draggableTip", draggableTip)

        
    def addButtonText(self, addButtonText):
        # 新增按钮文字 可选项: string
        return self.set("addButtonText", addButtonText)

        
    def minLength(self, minLength):
        # 限制最小长度 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 限制最大长度 可选项: number
        return self.set("maxLength", maxLength)

        
    def scaffold(self, scaffold):
        # 新增成员时的默认值，一般根据`items`的数据类型指定需要的默认值 可选项: any
        return self.set("scaffold", scaffold)

        