
from amis.AmisComponent import AmisComponent

class InputNumber(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-number")
    
    def min(self, min):
        # 最小值 可选项: [模板](../../../docs/concepts/template)
        return self.set("min", min)

        
    def max(self, max):
        # 最大值 可选项: [模板](../../../docs/concepts/template)
        return self.set("max", max)

        
    def step(self, step):
        # 步长 可选项: number
        return self.set("step", step)

        
    def precision(self, precision):
        # 精度，即小数点后几位，支持 0 和正整数 可选项: number
        return self.set("precision", precision)

        
    def showSteps(self, showSteps):
        # 是否显示上下点击按钮 可选项: boolean
        return self.set("showSteps", showSteps)

        
    def readOnly(self, readOnly):
        # 只读 可选项: boolean
        return self.set("readOnly", readOnly)

        
    def prefix(self, prefix):
        # 前缀 可选项: string
        return self.set("prefix", prefix)

        
    def suffix(self, suffix):
        # 后缀 可选项: string
        return self.set("suffix", suffix)

        
    def kilobitSeparator(self, kilobitSeparator):
        # 千分分隔 可选项: boolean
        return self.set("kilobitSeparator", kilobitSeparator)

        
    def keyboard(self, keyboard):
        # 键盘事件（方向上下） 可选项: boolean
        return self.set("keyboard", keyboard)

        
    def displayMode(self, displayMode):
        # 样式类型 可选项: "base","enhance"
        return self.set("displayMode", displayMode)

        
    def borderMode(self, borderMode):
        # 边框模式，全边框，还是半边框，或者没边框 可选项: "full","half","none"
        return self.set("borderMode", borderMode)

        
    def resetValue(self, resetValue):
        # 清空输入内容时，组件值将设置为 `resetValue` 可选项: number,string
        return self.set("resetValue", resetValue)

        