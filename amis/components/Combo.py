
from amis.AmisComponent import AmisComponent

class Combo(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "combo")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def formClassName(self, formClassName):
        # 单组表单项的类名 可选项: string
        return self.set("formClassName", formClassName)

        
    def items(self, items):
        # 组合展示的表单项 可选项: Array<[表单项](./formitem)>
        return self.set("items", items)

        
    def noBorder(self, noBorder):
        # 单组表单项是否显示边框 可选项: boolean
        return self.set("noBorder", noBorder)

        
    def scaffold(self, scaffold):
        # 单组表单项初始值 可选项: object
        return self.set("scaffold", scaffold)

        
    def multiple(self, multiple):
        # 是否多选 可选项: boolean
        return self.set("multiple", multiple)

        
    def multiLine(self, multiLine):
        # 默认是横着展示一排，设置以后竖着展示 可选项: boolean
        return self.set("multiLine", multiLine)

        
    def minLength(self, minLength):
        # 最少添加的条数，`2.4.1` 版本后支持变量 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 最多添加的条数，`2.4.1` 版本后支持变量 可选项: number
        return self.set("maxLength", maxLength)

        
    def flat(self, flat):
        # 是否将结果扁平化(去掉 name),只有当 items 的 length 为 1 且 multiple 为 true 的时候才有效。 可选项: boolean
        return self.set("flat", flat)

        
    def joinValues(self, joinValues):
        # 默认为 `true` 当扁平化开启的时候，是否用分隔符的形式发送给后端，否则采用 array 的方式。 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def delimiter(self, delimiter):
        # 当扁平化开启并且 joinValues 为 true 时，用什么分隔符。 可选项: string
        return self.set("delimiter", delimiter)

        
    def addable(self, addable):
        # 是否可新增 可选项: boolean
        return self.set("addable", addable)

        
    def addattop(self, addattop):
        # 在顶部添加 可选项: boolean
        return self.set("addattop", addattop)

        
    def removable(self, removable):
        # 是否可删除 可选项: boolean
        return self.set("removable", removable)

        
    def deleteApi(self, deleteApi):
        # 如果配置了，则删除前会发送一个 api，请求成功才完成删除 可选项: [API](../../../docs/types/api)
        return self.set("deleteApi", deleteApi)

        
    def deleteConfirmText(self, deleteConfirmText):
        # 当配置 `deleteApi` 才生效！删除时用来做用户确认 可选项: string
        return self.set("deleteConfirmText", deleteConfirmText)

        
    def draggable(self, draggable):
        # 是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个\$id 字段 可选项: boolean
        return self.set("draggable", draggable)

        
    def draggableTip(self, draggableTip):
        # 可拖拽的提示文字 可选项: string
        return self.set("draggableTip", draggableTip)

        
    def subFormMode(self, subFormMode):
        # 可选`normal`、`horizontal`、`inline` 可选项: string
        return self.set("subFormMode", subFormMode)

        
    def subFormHorizontal(self, subFormHorizontal):
        # 当 subFormMode 为 `horizontal` 时有用，用来控制 label 的展示占比 可选项: Object
        return self.set("subFormHorizontal", subFormHorizontal)

        
    def placeholder(self, placeholder):
        # 没有成员时显示。 可选项: string
        return self.set("placeholder", placeholder)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 指定是否可以自动获取上层的数据并映射到表单项上 可选项: boolean
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def conditions(self, conditions):
        # 数组的形式包含所有条件的渲染类型，单个数组内的`test` 为判断条件，数组内的`items`为符合该条件后渲染的`schema` 可选项: object
        return self.set("conditions", conditions)

        
    def typeSwitchable(self, typeSwitchable):
        # 是否可切换条件，配合`conditions`使用 可选项: boolean
        return self.set("typeSwitchable", typeSwitchable)

        
    def strictMode(self, strictMode):
        # 默认为严格模式，设置为 false 时，当其他表单项更新是，里面的表单项也可以及时获取，否则不会。 可选项: boolean
        return self.set("strictMode", strictMode)

        
    def syncFields(self, syncFields):
        # 配置同步字段。只有 `strictMode` 为 `false` 时有效。如果 Combo 层级比较深，底层的获取外层的数据可能不同步。但是给 combo 配置这个属性就能同步下来。输入格式：`["os"]` 可选项: Array<string>
        return self.set("syncFields", syncFields)

        
    def nullable(self, nullable):
        # 允许为空，如果子表单项里面配置验证器，且又是单条模式。可以允许用户选择清空（不填）。 可选项: boolean
        return self.set("nullable", nullable)

        
    def itemClassName(self, itemClassName):
        # 单组 CSS 类 可选项: string
        return self.set("itemClassName", itemClassName)

        
    def itemsWrapperClassName(self, itemsWrapperClassName):
        # 组合区域 CSS 类 可选项: string
        return self.set("itemsWrapperClassName", itemsWrapperClassName)

        
    def deleteBtn(self, deleteBtn):
        # 只有当`removable`为 `true` 时有效; 如果为`string`则为按钮的文本；如果为`Button`则根据配置渲染删除按钮。 可选项: [Button](../button.md)orstring
        return self.set("deleteBtn", deleteBtn)

        
    def addBtn(self, addBtn):
        # 可新增自定义配置渲染新增按钮，在`tabsMode: true`下不生效。 可选项: [Button](../button.md)
        return self.set("addBtn", addBtn)

        
    def addButtonClassName(self, addButtonClassName):
        # 新增按钮 CSS 类名 可选项: string
        return self.set("addButtonClassName", addButtonClassName)

        
    def addButtonText(self, addButtonText):
        # 新增按钮文字 可选项: string
        return self.set("addButtonText", addButtonText)

        