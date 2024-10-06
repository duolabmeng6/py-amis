
from amis.AmisComponent import AmisComponent

class Checkboxes(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "checkboxes")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # [选项组](./#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
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

        
    def columnsCount(self, columnsCount):
        # 选项按几列显示，默认为一列 可选项: number
        return self.set("columnsCount", columnsCount)

        
    def menuTpl(self, menuTpl):
        # 支持自定义选项渲染 可选项: string
        return self.set("menuTpl", menuTpl)

        
    def checkAll(self, checkAll):
        # 是否支持全选 可选项: boolean
        return self.set("checkAll", checkAll)

        
    def inline(self, inline):
        # 是否显示为一行 可选项: boolean
        return self.set("inline", inline)

        
    def defaultCheckAll(self, defaultCheckAll):
        # 默认是否全选 可选项: boolean
        return self.set("defaultCheckAll", defaultCheckAll)

        
    def creatable(self, creatable):
        # [新增选项](./options#%E5%89%8D%E7%AB%AF%E6%96%B0%E5%A2%9E-creatable) 可选项: boolean
        return self.set("creatable", creatable)

        
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

        
    def optionType(self, optionType):
        # 按钮模式 可选项: default,button
        return self.set("optionType", optionType)

        
    def itemClassName(self, itemClassName):
        # 选项样式类名 可选项: string
        return self.set("itemClassName", itemClassName)

        
    def labelClassName(self, labelClassName):
        # 选项标签样式类名 可选项: string
        return self.set("labelClassName", labelClassName)

        