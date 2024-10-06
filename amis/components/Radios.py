
from amis.AmisComponent import AmisComponent

class Radios(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "radios")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
    def labelField(self, labelField):
        # [选项标签字段](./options#%E9%80%89%E9%A1%B9%E6%A0%87%E7%AD%BE%E5%AD%97%E6%AE%B5-labelfield) 可选项: boolean
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # [选项值字段](./options#%E9%80%89%E9%A1%B9%E5%80%BC%E5%AD%97%E6%AE%B5-valuefield) 可选项: boolean
        return self.set("valueField", valueField)

        
    def columnsCount(self, columnsCount):
        # 选项按几列显示，默认为一列 可选项: number
        return self.set("columnsCount", columnsCount)

        
    def autoFill(self, autoFill):
        # [自动填充](./options#%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85-autofill) 可选项: object
        return self.set("autoFill", autoFill)

        
    def optionClassName(self, optionClassName):
        # 选项 CSS 类名 可选项: string
        return self.set("optionClassName", optionClassName)

        