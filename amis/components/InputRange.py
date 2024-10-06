
from amis.AmisComponent import AmisComponent

class InputRange(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-range")
    
    def className(self, className):
        # css 类名 可选项: string
        return self.set("className", className)

        
    def value(self, value):
        #  可选项: numberorstringor{min:number,max:number}or[number,number]
        return self.set("value", value)

        
    def disabled(self, disabled):
        # 是否禁用 可选项: boolean
        return self.set("disabled", disabled)

        
    def showSteps(self, showSteps):
        # 是否显示步长 可选项: boolean
        return self.set("showSteps", showSteps)

        
    def parts(self, parts):
        # 分割的块数<br/>主持数组传入分块的节点 可选项: numberornumber[]
        return self.set("parts", parts)

        
    def marks(self, marks):
        # 刻度标记<br/>- 支持自定义样式<br/>- 设置百分比 可选项: <code>{[number&#124;string]:string&#124;number&#124;SchemaObject}</code>or<code>{[number&#124;string]:{style:CSSProperties,label:string}}</code>
        return self.set("marks", marks)

        
    def tooltipVisible(self, tooltipVisible):
        # 是否显示滑块标签 可选项: boolean
        return self.set("tooltipVisible", tooltipVisible)

        
    def tooltipPlacement(self, tooltipPlacement):
        # 滑块标签的位置，默认`auto`，方向自适应<br/>前置条件：tooltipVisible 不为 false 时有效 可选项: autoorbottomorleftorright
        return self.set("tooltipPlacement", tooltipPlacement)

        
    def tipFormatter(self, tipFormatter):
        # 控制滑块标签显隐函数<br/>前置条件：tooltipVisible 不为 false 时有效 可选项: function
        return self.set("tipFormatter", tipFormatter)

        
    def multiple(self, multiple):
        # 支持选择范围 可选项: boolean
        return self.set("multiple", multiple)

        
    def joinValues(self, joinValues):
        # 默认为 `true`，选择的 `value` 会通过 `delimiter` 连接起来，否则直接将以`{min: 1, max: 100}`的形式提交<br/>前置条件：开启`multiple`时有效 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def delimiter(self, delimiter):
        # 分隔符 可选项: string
        return self.set("delimiter", delimiter)

        
    def unit(self, unit):
        # 单位 可选项: string
        return self.set("unit", unit)

        
    def clearable(self, clearable):
        # 是否可清除<br/>前置条件：开启`showInput`时有效 可选项: boolean
        return self.set("clearable", clearable)

        
    def showInput(self, showInput):
        # 是否显示输入框 可选项: boolean
        return self.set("showInput", showInput)

        
    def onChange(self, onChange):
        # 当 组件 的值发生改变时，会触发 onChange 事件，并把改变后的值作为参数传入 可选项: function
        return self.set("onChange", onChange)

        
    def onAfterChange(self, onAfterChange):
        # 与 `onmouseup` 触发时机一致，把当前值作为参数传入 可选项: function
        return self.set("onAfterChange", onAfterChange)

        