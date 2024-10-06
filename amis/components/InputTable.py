
from amis.AmisComponent import AmisComponent

class InputTable(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-table")
    
    def type(self, type):
        # 指定为 Table 渲染器 可选项: string
        return self.set("type", type)

        
    def addable(self, addable):
        # 是否可增加一行 可选项: boolean
        return self.set("addable", addable)

        
    def copyable(self, copyable):
        # 是否可复制一行 可选项: boolean
        return self.set("copyable", copyable)

        
    def copyData(self, copyData):
        # 控制复制时的数据映射，不配置时复制整行数据 可选项: PlainObject
        return self.set("copyData", copyData)

        
    def childrenAddable(self, childrenAddable):
        # 是否可增加子级节点 可选项: boolean
        return self.set("childrenAddable", childrenAddable)

        
    def editable(self, editable):
        # 是否可编辑 可选项: boolean
        return self.set("editable", editable)

        
    def removable(self, removable):
        # 是否可删除 可选项: boolean
        return self.set("removable", removable)

        
    def showTableAddBtn(self, showTableAddBtn):
        # 是否显示表格操作栏添加按钮，前提是要开启可新增功能 可选项: boolean
        return self.set("showTableAddBtn", showTableAddBtn)

        
    def showFooterAddBtn(self, showFooterAddBtn):
        # 是否显示表格下方添加按，前提是要开启可新增功能 可选项: boolean
        return self.set("showFooterAddBtn", showFooterAddBtn)

        
    def addApi(self, addApi):
        # 新增时提交的 API 可选项: [API](../../../docs/types/api)
        return self.set("addApi", addApi)

        
    def footerAddBtn(self, footerAddBtn):
        # 底部新增按钮配置 可选项: [SchemaNode](../../docs/types/schemanode)
        return self.set("footerAddBtn", footerAddBtn)

        
    def updateApi(self, updateApi):
        # 修改时提交的 API 可选项: [API](../../../docs/types/api)
        return self.set("updateApi", updateApi)

        
    def deleteApi(self, deleteApi):
        # 删除时提交的 API 可选项: [API](../../../docs/types/api)
        return self.set("deleteApi", deleteApi)

        
    def addBtnLabel(self, addBtnLabel):
        # 增加按钮名称 可选项: string
        return self.set("addBtnLabel", addBtnLabel)

        
    def addBtnIcon(self, addBtnIcon):
        # 增加按钮图标 可选项: string
        return self.set("addBtnIcon", addBtnIcon)

        
    def subAddBtnLabel(self, subAddBtnLabel):
        # 子级增加按钮名称 可选项: string
        return self.set("subAddBtnLabel", subAddBtnLabel)

        
    def subAddBtnIcon(self, subAddBtnIcon):
        # 子级增加按钮图标 可选项: string
        return self.set("subAddBtnIcon", subAddBtnIcon)

        
    def copyBtnLabel(self, copyBtnLabel):
        # 复制按钮文字 可选项: string
        return self.set("copyBtnLabel", copyBtnLabel)

        
    def copyBtnIcon(self, copyBtnIcon):
        # 复制按钮图标 可选项: string
        return self.set("copyBtnIcon", copyBtnIcon)

        
    def editBtnLabel(self, editBtnLabel):
        # 编辑按钮名称 可选项: string
        return self.set("editBtnLabel", editBtnLabel)

        
    def editBtnIcon(self, editBtnIcon):
        # 编辑按钮图标 可选项: string
        return self.set("editBtnIcon", editBtnIcon)

        
    def deleteBtnLabel(self, deleteBtnLabel):
        # 删除按钮名称 可选项: string
        return self.set("deleteBtnLabel", deleteBtnLabel)

        
    def deleteBtnIcon(self, deleteBtnIcon):
        # 删除按钮图标 可选项: string
        return self.set("deleteBtnIcon", deleteBtnIcon)

        
    def confirmBtnLabel(self, confirmBtnLabel):
        # 确认编辑按钮名称 可选项: string
        return self.set("confirmBtnLabel", confirmBtnLabel)

        
    def confirmBtnIcon(self, confirmBtnIcon):
        # 确认编辑按钮图标 可选项: string
        return self.set("confirmBtnIcon", confirmBtnIcon)

        
    def cancelBtnLabel(self, cancelBtnLabel):
        # 取消编辑按钮名称 可选项: string
        return self.set("cancelBtnLabel", cancelBtnLabel)

        
    def cancelBtnIcon(self, cancelBtnIcon):
        # 取消编辑按钮图标 可选项: string
        return self.set("cancelBtnIcon", cancelBtnIcon)

        
    def needConfirm(self, needConfirm):
        # 是否需要确认操作，，可用来控控制表格的操作交互 可选项: boolean
        return self.set("needConfirm", needConfirm)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 是否可以访问父级数据，也就是表单中的同级数据，通常需要跟 strictMode 搭配使用 可选项: boolean
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def strictMode(self, strictMode):
        # 为了性能，默认其他表单项项值变化不会让当前表格更新，有时候为了同步获取其他表单项字段，需要开启这个。 可选项: boolean
        return self.set("strictMode", strictMode)

        
    def minLength(self, minLength):
        # 最小行数, `2.4.1`版本后支持变量 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 最大行数, `2.4.1`版本后支持变量 可选项: number
        return self.set("maxLength", maxLength)

        
    def perPage(self, perPage):
        # 每页展示几行数据，如果不配置则不会显示分页器 可选项: number
        return self.set("perPage", perPage)

        
    def columns(self, columns):
        # 列信息 可选项: array
        return self.set("columns", columns)

        