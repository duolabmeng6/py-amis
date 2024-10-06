
from amis.AmisComponent import AmisComponent

class InputTag(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-tag")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def optionsTip(self, optionsTip):
        # 选项提示 可选项: Array<object>或Array<string>
        return self.set("optionsTip", optionsTip)

        
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

        
    def clearable(self, clearable):
        # 在有值的时候是否显示一个删除图标在右侧。 可选项: boolean
        return self.set("clearable", clearable)

        
    def resetValue(self, resetValue):
        # 删除后设置此配置项给定的值。 可选项: string
        return self.set("resetValue", resetValue)

        
    def max(self, max):
        # 允许添加的标签的最大数量 可选项: number
        return self.set("max", max)

        
    def maxTagLength(self, maxTagLength):
        # 单个标签的最大文本长度 可选项: number
        return self.set("maxTagLength", maxTagLength)

        
    def maxTagCount(self, maxTagCount):
        # 标签的最大展示数量，超出数量后以收纳浮层的方式展示，仅在多选模式开启后生效 可选项: number
        return self.set("maxTagCount", maxTagCount)

        
    def overflowTagPopover(self, overflowTagPopover):
        # 收纳浮层的配置属性，详细配置参考[Tooltip](../tooltip#属性表) 可选项: TooltipObject
        return self.set("overflowTagPopover", overflowTagPopover)

        
    def enableBatchAdd(self, enableBatchAdd):
        # 是否开启批量添加模式 可选项: boolean
        return self.set("enableBatchAdd", enableBatchAdd)

        
    def separator(self, separator):
        # 开启批量添加后，输入多个标签的分隔符，支持传入多个符号，默认为"-" 可选项: string
        return self.set("separator", separator)

        