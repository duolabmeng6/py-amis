
from amis.AmisComponent import AmisComponent

class InputColor(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-color")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def format(self, format):
        # 请选择 `hex`、`hexa`、`hls`、`rgb`或者`rgba`。 可选项: string
        return self.set("format", format)

        
    def presetColors(self, presetColors):
        # 选择器底部的默认颜色，数组内为空则不显示默认颜色 可选项: Array<string>
        return self.set("presetColors", presetColors)

        
    def allowCustomColor(self, allowCustomColor):
        # 为`false`时只能选择颜色，使用 `presetColors` 设定颜色选择范围 可选项: boolean
        return self.set("allowCustomColor", allowCustomColor)

        
    def clearable(self, clearable):
        # 是否显示清除按钮 可选项: boolean
        return self.set("clearable", clearable)

        
    def resetValue(self, resetValue):
        # 清除后，表单项值调整成该值 可选项: string
        return self.set("resetValue", resetValue)

        