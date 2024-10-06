
from amis.AmisComponent import AmisComponent

class Picker(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "picker")
    
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)或[数据映射](../../../docs/concepts/data-mapping)
        return self.set("source", source)

        
    def multiple(self, multiple):
        # 是否为多选。 可选项: boolean
        return self.set("multiple", multiple)

        
    def delimiter(self, delimiter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: boolean
        return self.set("delimiter", delimiter)

        
    def labelField(self, labelField):
        # [选项标签字段](./options#%E9%80%89%E9%A1%B9%E6%A0%87%E7%AD%BE%E5%AD%97%E6%AE%B5-labelfield) 可选项: boolean
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # [选项值字段](./options#%E9%80%89%E9%A1%B9%E5%80%BC%E5%AD%97%E6%AE%B5-valuefield) 可选项: boolean
        return self.set("valueField", valueField)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def autoFill(self, autoFill):
        # [自动填充](./options#%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85-autofill) 可选项: object
        return self.set("autoFill", autoFill)

        
    def modalTitle(self, modalTitle):
        # 设置模态框的标题 可选项: string
        return self.set("modalTitle", modalTitle)

        
    def modalMode(self, modalMode):
        # 设置 `dialog` 或者 `drawer`，用来配置弹出方式。 可选项: string
        return self.set("modalMode", modalMode)

        
    def pickerSchema(self, pickerSchema):
        # 即用 List 类型的渲染，来展示列表信息。更多配置参考 [CRUD](../crud) 可选项: string
        return self.set("pickerSchema", pickerSchema)

        
    def embed(self, embed):
        # 是否使用内嵌模式 可选项: boolean
        return self.set("embed", embed)

        
    def overflowConfig(self, overflowConfig):
        # 开启最大标签展示数量的相关配置 `3.4.0` 可选项: OverflowConfig
        return self.set("overflowConfig", overflowConfig)

        