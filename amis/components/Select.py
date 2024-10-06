
from amis.AmisComponent import AmisComponent

class Select(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "select")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: [API](../../../docs/types/api)或[数据映射](../../../docs/concepts/data-mapping)
        return self.set("source", source)

        
    def autoComplete(self, autoComplete):
        # [自动提示补全](./options#%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8-autocomplete) 可选项: [API](../../../docs/types/api)
        return self.set("autoComplete", autoComplete)

        
    def delimiter(self, delimiter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: string
        return self.set("delimiter", delimiter)

        
    def labelField(self, labelField):
        # [选项标签字段](./options#%E9%80%89%E9%A1%B9%E6%A0%87%E7%AD%BE%E5%AD%97%E6%AE%B5-labelfield) 可选项: string
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # [选项值字段](./options#%E9%80%89%E9%A1%B9%E5%80%BC%E5%AD%97%E6%AE%B5-valuefield) 可选项: string
        return self.set("valueField", valueField)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def checkAll(self, checkAll):
        # 是否支持全选 可选项: boolean
        return self.set("checkAll", checkAll)

        
    def checkAllLabel(self, checkAllLabel):
        # 全选的文字 可选项: string
        return self.set("checkAllLabel", checkAllLabel)

        
    def checkAllBySearch(self, checkAllBySearch):
        # 有检索时只全选检索命中的项 可选项: boolean
        return self.set("checkAllBySearch", checkAllBySearch)

        
    def defaultCheckAll(self, defaultCheckAll):
        # 默认是否全选 可选项: boolean
        return self.set("defaultCheckAll", defaultCheckAll)

        
    def creatable(self, creatable):
        # [新增选项](./options#%E5%89%8D%E7%AB%AF%E6%96%B0%E5%A2%9E-creatable) 可选项: boolean
        return self.set("creatable", creatable)

        
    def multiple(self, multiple):
        # [多选](./options#多选-multiple) 可选项: boolean
        return self.set("multiple", multiple)

        
    def searchable(self, searchable):
        # [检索](./options#检索-searchable) 可选项: boolean
        return self.set("searchable", searchable)

        
    def filterOption(self, filterOption):
        #  可选项: string
        return self.set("filterOption", filterOption)

        
    def createBtnLabel(self, createBtnLabel):
        # [新增选项](./options#%E6%96%B0%E5%A2%9E%E9%80%89%E9%A1%B9) 可选项: string
        return self.set("createBtnLabel", createBtnLabel)

        
    def addControls(self, addControls):
        # [自定义新增表单项](./options#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%96%B0%E5%A2%9E%E8%A1%A8%E5%8D%95%E9%A1%B9-addcontrols) 可选项: Array<[表单项](./formitem)>
        return self.set("addControls", addControls)

        
    def addApi(self, addApi):
        # [配置新增选项接口](./options#%E9%85%8D%E7%BD%AE%E6%96%B0%E5%A2%9E%E6%8E%A5%E5%8F%A3-addapi) 可选项: [API](../../docs/types/api)
        return self.set("addApi", addApi)

        
    def editable(self, editable):
        # [编辑选项](./options#%E5%89%8D%E7%AB%AF%E7%BC%96%E8%BE%91-editable) 可选项: boolean
        return self.set("editable", editable)

        
    def editControls(self, editControls):
        # [自定义编辑表单项](./options#%E8%87%AA%E5%AE%9A%E4%B9%89%E7%BC%96%E8%BE%91%E8%A1%A8%E5%8D%95%E9%A1%B9-editcontrols) 可选项: Array<[表单项](./formitem)>
        return self.set("editControls", editControls)

        
    def editApi(self, editApi):
        # [配置编辑选项接口](./options#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E6%8E%A5%E5%8F%A3-editapi) 可选项: [API](../../docs/types/api)
        return self.set("editApi", editApi)

        
    def removable(self, removable):
        # [删除选项](./options#%E5%88%A0%E9%99%A4%E9%80%89%E9%A1%B9) 可选项: boolean
        return self.set("removable", removable)

        
    def deleteApi(self, deleteApi):
        # [配置删除选项接口](./options#%E9%85%8D%E7%BD%AE%E5%88%A0%E9%99%A4%E6%8E%A5%E5%8F%A3-deleteapi) 可选项: [API](../../docs/types/api)
        return self.set("deleteApi", deleteApi)

        
    def autoFill(self, autoFill):
        # [自动填充](./options#%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85-autofill) 可选项: object
        return self.set("autoFill", autoFill)

        
    def menuTpl(self, menuTpl):
        # 支持配置自定义菜单 可选项: string
        return self.set("menuTpl", menuTpl)

        
    def clearable(self, clearable):
        # 单选模式下是否支持清空 可选项: boolean
        return self.set("clearable", clearable)

        
    def hideSelected(self, hideSelected):
        # 隐藏已选选项 可选项: boolean
        return self.set("hideSelected", hideSelected)

        
    def mobileClassName(self, mobileClassName):
        # 移动端浮层类名 可选项: string
        return self.set("mobileClassName", mobileClassName)

        
    def selectMode(self, selectMode):
        # 可选：`group`、`table`、`tree`、`chained`、`associated`。分别为：列表形式、表格形式、树形选择形式、级联选择形式，关联选择形式（与级联选择的区别在于，级联是无限极，而关联只有一级，关联左边可以是个 tree）。 可选项: string
        return self.set("selectMode", selectMode)

        
    def searchResultMode(self, searchResultMode):
        # 如果不设置将采用 `selectMode` 的值，可以单独配置，参考 `selectMode`，决定搜索结果的展示形式。 可选项: string
        return self.set("searchResultMode", searchResultMode)

        
    def columns(self, columns):
        # 当展示形式为 `table` 可以用来配置展示哪些列，跟 table 中的 columns 配置相似，只是只有展示功能。 可选项: Array<Object>
        return self.set("columns", columns)

        
    def leftOptions(self, leftOptions):
        # 当展示形式为 `associated` 时用来配置左边的选项集。 可选项: Array<Object>
        return self.set("leftOptions", leftOptions)

        
    def leftMode(self, leftMode):
        # 当展示形式为 `associated` 时用来配置左边的选择形式，支持 `list` 或者 `tree`。默认为 `list`。 可选项: string
        return self.set("leftMode", leftMode)

        
    def rightMode(self, rightMode):
        # 当展示形式为 `associated` 时用来配置右边的选择形式，可选：`list`、`table`、`tree`、`chained`。 可选项: string
        return self.set("rightMode", rightMode)

        
    def maxTagCount(self, maxTagCount):
        # 标签的最大展示数量，超出数量后以收纳浮层的方式展示，仅在多选模式开启后生效 可选项: number
        return self.set("maxTagCount", maxTagCount)

        
    def overflowTagPopover(self, overflowTagPopover):
        # 收纳浮层的配置属性，详细配置参考[Tooltip](../tooltip#属性表) 可选项: TooltipObject
        return self.set("overflowTagPopover", overflowTagPopover)

        
    def optionClassName(self, optionClassName):
        # 选项 CSS 类名 可选项: string
        return self.set("optionClassName", optionClassName)

        
    def popOverContainerSelector(self, popOverContainerSelector):
        # 弹层挂载位置选择器，会通过`querySelector`获取 可选项: string
        return self.set("popOverContainerSelector", popOverContainerSelector)

        
    def clearable(self, clearable):
        # 是否展示清空图标 可选项: boolean
        return self.set("clearable", clearable)

        
    def overlay(self, overlay):
        # 弹层宽度与对齐方式 `2.8.0 以上版本` 可选项: {width:string,number,align:"left","center","right"}
        return self.set("overlay", overlay)

        
    def showInvalidMatch(self, showInvalidMatch):
        # 选项值与选项组不匹配时选项值是否飘红 可选项: boolean
        return self.set("showInvalidMatch", showInvalidMatch)

        
    def noResultsText(self, noResultsText):
        # 无结果时的文本 可选项: string
        return self.set("noResultsText", noResultsText)

        