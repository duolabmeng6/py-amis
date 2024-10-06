
from amis.AmisComponent import AmisComponent

class TableColumnObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "table-column-object")
        
    
    def label(self, label):
        # 列标题
        
        return self.set("label", label)

        
    def fixed(self, fixed):
        # 配置是否固定当前列# 可选项: ['left', 'right', 'none']
        
        return self.set("fixed", fixed)

        
    def name(self, name):
        # 绑定字段名
        
        return self.set("name", name)

        
    def popOver(self, popOver):
        # 配置查看详情功能
        
        return self.set("popOver", popOver)

        
    def quickEdit(self, quickEdit):
        # 配置快速编辑功能
        
        return self.set("quickEdit", quickEdit)

        
    def quickEditOnUpdate(self, quickEditOnUpdate):
        # 作为表单项时，可以单独配置编辑时的快速编辑面板。
        
        return self.set("quickEditOnUpdate", quickEditOnUpdate)

        
    def copyable(self, copyable):
        # 配置点击复制功能
        
        return self.set("copyable", copyable)

        
    def sortable(self, sortable):
        # 配置是否可以排序
        
        return self.set("sortable", sortable)

        
    def searchable(self, searchable):
        # 是否可快速搜索
        
        return self.set("searchable", searchable)

        
    def toggled(self, toggled):
        # 配置是否默认展示
        
        return self.set("toggled", toggled)

        
    def width(self, width):
        # 列宽度
        
        return self.set("width", width)

        
    def align(self, align):
        # 列对齐方式# 可选项: ['left', 'right', 'center', 'justify']
        
        return self.set("align", align)

        
    def vAlign(self, vAlign):
        # 列垂直对齐方式# 可选项: ['top', 'middle', 'bottom']
        
        return self.set("vAlign", vAlign)

        
    def headerAlign(self, headerAlign):
        # 标题左右对齐方式# 可选项: ['left', 'right', 'center', 'justify']
        
        return self.set("headerAlign", headerAlign)

        
    def className(self, className):
        # 列样式表
        
        return self.set("className", className)

        
    def classNameExpr(self, classNameExpr):
        # 单元格样式表达式
        
        return self.set("classNameExpr", classNameExpr)

        
    def labelClassName(self, labelClassName):
        # 列头样式表
        
        return self.set("labelClassName", labelClassName)

        
    def filterable(self, filterable):
        # todo
        
        return self.set("filterable", filterable)

        
    def breakpoint(self, breakpoint):
        # 结合表格的 footable 一起使用。 填写 *、xs、sm、md、lg指定 footable 的触发条件，可以填写多个用空格隔开# 可选项: ['*', 'xs', 'sm', 'md', 'lg']
        
        return self.set("breakpoint", breakpoint)

        
    def remark(self, remark):
        # 提示信息
        
        return self.set("remark", remark)

        
    def value(self, value):
        # 默认值, 只有在 inputTable 里面才有用
        
        return self.set("value", value)

        
    def unique(self, unique):
        # 是否唯一, 只有在 inputTable 里面才有用
        
        return self.set("unique", unique)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 表格列单元格是否可以获取父级数据域值，默认为true，该配置对当前列内单元格生效
        
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def lazyRenderAfter(self, lazyRenderAfter):
        # 当一次性渲染太多列上有用，默认为 100，可以用来提升表格渲染性能
        
        return self.set("lazyRenderAfter", lazyRenderAfter)

        
    def innerStyle(self, innerStyle):
        # 单元格内部组件自定义样式 style作为单元格自定义样式的配置
        
        return self.set("innerStyle", innerStyle)

        