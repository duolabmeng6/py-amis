
from amis.AmisComponent import AmisComponent

class Column(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "column")
        
    
    def name(self, name):
        # 指定列唯一标识
        
        return self.set("name", name)

        
    def title(self, title):
        # 指定列标题
        
        return self.set("title", title)

        
    def type(self, type):
        # 指定列内容渲染器
        
        return self.set("type", type)

        
    def rowSpanExpr(self, rowSpanExpr):
        # 指定行合并表达式
        
        return self.set("rowSpanExpr", rowSpanExpr)

        
    def colSpanExpr(self, colSpanExpr):
        # 指定列合并表达式
        
        return self.set("colSpanExpr", colSpanExpr)

        
    def children(self, children):
        # 表头分组
        
        return self.set("children", children)

        
    def copyable(self, copyable):
        # 可复制
        
        return self.set("copyable", copyable)

        
    def remark(self, remark):
        # 列表头提示
        
        return self.set("remark", remark)

        
    def searchable(self, searchable):
        # 快速搜索
        
        return self.set("searchable", searchable)

        
    def sorter(self, sorter):
        # 快速排序
        
        return self.set("sorter", sorter)

        
    def sortable(self, sortable):
        # 兼容table快速排序
        
        return self.set("sortable", sortable)

        
    def filterable(self, filterable):
        # 兼容table列筛选
        
        return self.set("filterable", filterable)

        
    def align(self, align):
        # 内容居左、居中、居右
        
        return self.set("align", align)

        
    def fixed(self, fixed):
        # 是否固定在左侧/右侧
        
        return self.set("fixed", fixed)

        
    def toggled(self, toggled):
        # 当前列是否展示
        
        return self.set("toggled", toggled)

        
    def className(self, className):
        # 列样式
        
        return self.set("className", className)

        
    def titleClassName(self, titleClassName):
        # 表头单元格样式
        
        return self.set("titleClassName", titleClassName)

        
    def classNameExpr(self, classNameExpr):
        # 单元格样式
        
        return self.set("classNameExpr", classNameExpr)

        
    def quickEdit(self, quickEdit):
        # 配置快速编辑功能
        
        return self.set("quickEdit", quickEdit)

        
    def width(self, width):
        
        
        return self.set("width", width)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 表格列单元格是否可以获取父级数据域值，默认为true，该配置对当前列内单元格生效
        
        return self.set("canAccessSuperData", canAccessSuperData)

        