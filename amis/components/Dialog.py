
from amis.AmisComponent import AmisComponent

class Dialog(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "dialog")
        
    
    def className(self, className):
        # 容器 css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("className", className)

        
    def disabled(self, disabled):
        # 是否禁用
        
        return self.set("disabled", disabled)

        
    def disabledOn(self, disabledOn):
        # 是否禁用表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("disabledOn", disabledOn)

        
    def hidden(self, hidden):
        # 是否隐藏
        
        return self.set("hidden", hidden)

        
    def hiddenOn(self, hiddenOn):
        # 是否隐藏表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("hiddenOn", hiddenOn)

        
    def visible(self, visible):
        # 是否显示
        
        return self.set("visible", visible)

        
    def visibleOn(self, visibleOn):
        # 是否显示表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("visibleOn", visibleOn)

        
    def id(self, id):
        # 组件唯一 id，主要用于日志采集
        
        return self.set("id", id)

        
    def onEvent(self, onEvent):
        # 事件动作配置
        
        return self.set("onEvent", onEvent)

        
    def static(self, static):
        # 是否静态展示
        
        return self.set("static", static)

        
    def staticOn(self, staticOn):
        # 是否静态展示表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("staticOn", staticOn)

        
    def staticPlaceholder(self, staticPlaceholder):
        # 静态展示空值占位
        
        return self.set("staticPlaceholder", staticPlaceholder)

        
    def staticClassName(self, staticClassName):
        # 静态展示表单项类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticClassName", staticClassName)

        
    def staticLabelClassName(self, staticLabelClassName):
        # 静态展示表单项Label类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticLabelClassName", staticLabelClassName)

        
    def staticInputClassName(self, staticInputClassName):
        # 静态展示表单项Value类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("staticInputClassName", staticInputClassName)

        
    def staticSchema(self, staticSchema):
        
        
        return self.set("staticSchema", staticSchema)

        
    def style(self, style):
        # 组件样式
        
        return self.set("style", style)

        
    def editorSetting(self, editorSetting):
        # 编辑器配置，运行时可以忽略
        
        return self.set("editorSetting", editorSetting)

        
    def useMobileUI(self, useMobileUI):
        # 可以组件级别用来关闭移动端样式
        
        return self.set("useMobileUI", useMobileUI)

        
    def testIdBuilder(self, testIdBuilder):
        
        
        return self.set("testIdBuilder", testIdBuilder)

        
    def type(self, type):
        
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def inputParams(self, inputParams):
        # 弹窗参数说明，值格式为 JSONSchema。
        
        return self.set("inputParams", inputParams)

        
    def actions(self, actions):
        # 默认不用填写，自动会创建确认和取消按钮。
        
        return self.set("actions", actions)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def bodyClassName(self, bodyClassName):
        # 配置 Body 容器 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("bodyClassName", bodyClassName)

        
    def closeOnEsc(self, closeOnEsc):
        # 是否支持按 ESC 关闭 Dialog
        
        return self.set("closeOnEsc", closeOnEsc)

        
    def closeOnOutside(self, closeOnOutside):
        # 是否支持点其它区域关闭 Dialog
        
        return self.set("closeOnOutside", closeOnOutside)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def size(self, size):
        # Dialog 大小# 可选项: ['xs', 'sm', 'md', 'lg', 'xl', 'full']
        
        return self.set("size", size)

        
    def height(self, height):
        # Dialog 高度
        
        return self.set("height", height)

        
    def width(self, width):
        # Dialog 宽度
        
        return self.set("width", width)

        
    def title(self, title):
        # 请通过配置 title 设置标题
        
        return self.set("title", title)

        
    def header(self, header):
        
        
        return self.set("header", header)

        
    def headerClassName(self, headerClassName):
        
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def footer(self, footer):
        
        
        return self.set("footer", footer)

        
    def confirm(self, confirm):
        # 影响自动生成的按钮，如果自己配置了按钮这个配置无效。
        
        return self.set("confirm", confirm)

        
    def showCloseButton(self, showCloseButton):
        # 是否显示关闭按钮
        
        return self.set("showCloseButton", showCloseButton)

        
    def showErrorMsg(self, showErrorMsg):
        # 是否显示错误信息
        
        return self.set("showErrorMsg", showErrorMsg)

        
    def showLoading(self, showLoading):
        # 是否显示 spinner
        
        return self.set("showLoading", showLoading)

        
    def overlay(self, overlay):
        # 是否显示蒙层
        
        return self.set("overlay", overlay)

        
    def dialogType(self, dialogType):
        # 弹框类型 confirm 确认弹框
        
        return self.set("dialogType", dialogType)

        
    def draggable(self, draggable):
        # 可拖拽
        
        return self.set("draggable", draggable)

        
    def data(self, data):
        # 数据映射
        
        return self.set("data", data)

        