
from amis.AmisComponent import AmisComponent

class InputFormula(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-formula")
    
    def title(self, title):
        # 弹框标题 可选项: string
        return self.set("title", title)

        
    def header(self, header):
        # 编辑器 header 标题，如果不设置，默认使用表单项`label`字段 可选项: string
        return self.set("header", header)

        
    def evalMode(self, evalMode):
        # 表达式模式 或者 模板模式，模板模式则需要将表达式写在 `${` 和 `}` 中间。 可选项: boolean
        return self.set("evalMode", evalMode)

        
    def variables(self, variables):
        # 可用变量 可选项: {label:string;value:string;children?:any[];tag?:string}[]
        return self.set("variables", variables)

        
    def variableMode(self, variableMode):
        # 可配置成 `tabs` 或者 `tree` 默认为列表，支持分组。 可选项: string
        return self.set("variableMode", variableMode)

        
    def functions(self, functions):
        # 可以不设置，默认就是 amis-formula 里面定义的函数，如果扩充了新的函数则需要指定 可选项: Object[]
        return self.set("functions", functions)

        
    def inputMode(self, inputMode):
        # 控件的展示模式 可选项: button,input-button,input-group
        return self.set("inputMode", inputMode)

        
    def icon(self, icon):
        # 按钮图标，例如`fa fa-list` 可选项: string
        return self.set("icon", icon)

        
    def btnLabel(self, btnLabel):
        # 按钮文本，`inputMode`为`button`时生效 可选项: string
        return self.set("btnLabel", btnLabel)

        
    def level(self, level):
        # 按钮样式 可选项: info,success,warning,danger,link,primary,dark,light
        return self.set("level", level)

        
    def allowInput(self, allowInput):
        # 输入框是否可输入 可选项: boolean
        return self.set("allowInput", allowInput)

        
    def btnSize(self, btnSize):
        # 按钮大小 可选项: xs,sm,md,lg
        return self.set("btnSize", btnSize)

        
    def borderMode(self, borderMode):
        # 输入框边框模式 可选项: full,half,none
        return self.set("borderMode", borderMode)

        
    def placeholder(self, placeholder):
        # 输入框占位符 可选项: string
        return self.set("placeholder", placeholder)

        
    def className(self, className):
        # 控件外层 CSS 样式类名 可选项: string
        return self.set("className", className)

        
    def variableClassName(self, variableClassName):
        # 变量面板 CSS 样式类名 可选项: string
        return self.set("variableClassName", variableClassName)

        
    def functionClassName(self, functionClassName):
        # 函数面板 CSS 样式类名 可选项: string
        return self.set("functionClassName", functionClassName)

        