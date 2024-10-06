
from amis.AmisComponent import AmisComponent

class Options(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "options")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # 选项组，供用户选择 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # 选项组源，可通过数据映射获取当前数据域变量、或者配置 API 对象 可选项: [API](../../../docs/types/api)或[数据映射](../../../docs/concepts/data-mapping)
        return self.set("source", source)

        
    def multiple(self, multiple):
        # 是否支持多选 可选项: boolean
        return self.set("multiple", multiple)

        
    def labelField(self, labelField):
        # 标识选项中哪个字段是`label`值 可选项: boolean
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # 标识选项中哪个字段是`value`值 可选项: boolean
        return self.set("valueField", valueField)

        
    def deferField(self, deferField):
        # 标识选项中哪个字段是`defer`值 可选项: string
        return self.set("deferField", deferField)

        
    def joinValues(self, joinValues):
        # 是否拼接`value`值 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # 是否将`value`值抽取出来组成新的数组，只有在`joinValues`是`false`是生效 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def itemHeight(self, itemHeight):
        # 每个选项的高度，用于虚拟渲染 可选项: number
        return self.set("itemHeight", itemHeight)

        
    def virtualThreshold(self, virtualThreshold):
        # 在选项数量超过多少时开启虚拟渲染 可选项: number
        return self.set("virtualThreshold", virtualThreshold)

        
    def valuesNoWrap(self, valuesNoWrap):
        # 默认情况下多选所有选项都会显示，通过这个可以最多显示一行，超出的部分变成 ... 可选项: boolean
        return self.set("valuesNoWrap", valuesNoWrap)

        