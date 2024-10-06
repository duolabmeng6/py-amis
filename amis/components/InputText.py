
from amis.AmisComponent import AmisComponent

class InputText(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-text")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
    def autoComplete(self, autoComplete):
        # [自动补全](./options#%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8-autocomplete) 可选项: string或[API](../../../docs/types/api)
        return self.set("autoComplete", autoComplete)

        
    def multiple(self, multiple):
        # [是否多选](./options#%E5%A4%9A%E9%80%89-multiple) 可选项: boolean
        return self.set("multiple", multiple)

        
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

        
    def addOn(self, addOn):
        # 输入框附加组件，比如附带一个提示文字，或者附带一个提交按钮。 可选项: addOn
        return self.set("addOn", addOn)

        
    def trimContents(self, trimContents):
        # 是否去除首尾空白文本。 可选项: boolean
        return self.set("trimContents", trimContents)

        
    def clearValueOnEmpty(self, clearValueOnEmpty):
        # 文本内容为空时去掉这个值 可选项: boolean
        return self.set("clearValueOnEmpty", clearValueOnEmpty)

        
    def creatable(self, creatable):
        # 是否可以创建，默认为可以，除非设置为 false 即只能选择选项中的值 可选项: boolean
        return self.set("creatable", creatable)

        
    def clearable(self, clearable):
        # 是否可清除 可选项: boolean
        return self.set("clearable", clearable)

        
    def resetValue(self, resetValue):
        # 清除后设置此配置项给定的值。 可选项: string
        return self.set("resetValue", resetValue)

        
    def prefix(self, prefix):
        # 前缀 可选项: string
        return self.set("prefix", prefix)

        
    def suffix(self, suffix):
        # 后缀 可选项: string
        return self.set("suffix", suffix)

        
    def showCounter(self, showCounter):
        # 是否显示计数器 可选项: boolean
        return self.set("showCounter", showCounter)

        
    def minLength(self, minLength):
        # 限制最小字数 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 限制最大字数 可选项: number
        return self.set("maxLength", maxLength)

        
    def transform(self, transform):
        # 自动转换值，可选 `transform: { lowerCase: true, upperCase: true }` 可选项: object
        return self.set("transform", transform)

        
    def borderMode(self, borderMode):
        # 输入框边框模式，全边框，还是半边框，或者没边框。 可选项: "full","half","none"
        return self.set("borderMode", borderMode)

        
    def inputControlClassName(self, inputControlClassName):
        # control 节点的 CSS 类名 可选项: string
        return self.set("inputControlClassName", inputControlClassName)

        
    def nativeInputClassName(self, nativeInputClassName):
        # 原生 input 标签的 CSS 类名 可选项: string
        return self.set("nativeInputClassName", nativeInputClassName)

        
    def nativeAutoComplete(self, nativeAutoComplete):
        # 原生 input 标签的 `autoComplete` 属性，比如配置集成 `new-password` 可选项: string
        return self.set("nativeAutoComplete", nativeAutoComplete)

        