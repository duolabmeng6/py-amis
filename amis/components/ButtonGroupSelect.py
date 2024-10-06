
from amis.AmisComponent import AmisComponent

class ButtonGroupSelect(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "button-group-select")
    
    def type(self, type):
        # 指定为 button-group-select 渲染器 可选项: string
        return self.set("type", type)

        
    def vertical(self, vertical):
        # 是否使用垂直模式 可选项: boolean
        return self.set("vertical", vertical)

        
    def tiled(self, tiled):
        # 是否使用平铺模式 可选项: boolean
        return self.set("tiled", tiled)

        
    def btnLevel(self, btnLevel):
        # 按钮样式 可选项: link,primary,secondary,info,success,warning,danger,light,dark,default
        return self.set("btnLevel", btnLevel)

        
    def btnActiveLevel(self, btnActiveLevel):
        # 选中按钮样式 可选项: link,primary,secondary,info,success,warning,danger,light,dark,default
        return self.set("btnActiveLevel", btnActiveLevel)

        
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
    def multiple(self, multiple):
        # [多选](./options#%E5%A4%9A%E9%80%89-multiple) 可选项: boolean
        return self.set("multiple", multiple)

        
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

        