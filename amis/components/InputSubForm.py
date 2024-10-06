
from amis.AmisComponent import AmisComponent

class InputSubForm(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-sub-form")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def multiple(self, multiple):
        # 是否为多选模式 可选项: boolean
        return self.set("multiple", multiple)

        
    def labelField(self, labelField):
        # 当值中存在这个字段，则按钮名称将使用此字段的值来展示。 可选项: string
        return self.set("labelField", labelField)

        
    def btnLabel(self, btnLabel):
        # 按钮默认名称 可选项: string
        return self.set("btnLabel", btnLabel)

        
    def minLength(self, minLength):
        # 限制最小个数。 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 限制最大个数。 可选项: number
        return self.set("maxLength", maxLength)

        
    def draggable(self, draggable):
        # 是否可拖拽排序 可选项: boolean
        return self.set("draggable", draggable)

        
    def addable(self, addable):
        # 是否可新增 可选项: boolean
        return self.set("addable", addable)

        
    def removable(self, removable):
        # 是否可删除 可选项: boolean
        return self.set("removable", removable)

        
    def addButtonClassName(self, addButtonClassName):
        # 新增按钮 CSS 类名 可选项: string
        return self.set("addButtonClassName", addButtonClassName)

        
    def itemClassName(self, itemClassName):
        # 值元素 CSS 类名 可选项: string
        return self.set("itemClassName", itemClassName)

        
    def itemsClassName(self, itemsClassName):
        # 值包裹元素 CSS 类名 可选项: string
        return self.set("itemsClassName", itemsClassName)

        
    def form(self, form):
        # 子表单配置，同 [Form](./index) 可选项: [Form](./index)
        return self.set("form", form)

        
    def addButtonText(self, addButtonText):
        # 自定义新增一项的文本 可选项: string
        return self.set("addButtonText", addButtonText)

        
    def showErrorMsg(self, showErrorMsg):
        # 是否在左下角显示报错信息 可选项: boolean
        return self.set("showErrorMsg", showErrorMsg)

        