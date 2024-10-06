
from amis.AmisComponent import AmisComponent

class DropdownButton(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "dropdown-button")
        
    
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
        # 指定为 DropDown Button 类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def block(self, block):
        # 是否独占一行 `display: block`
        
        return self.set("block", block)

        
    def btnClassName(self, btnClassName):
        # 给 Button 配置 className。
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnClassName", btnClassName)

        
    def buttons(self, buttons):
        # 按钮集合，支持分组
        
        return self.set("buttons", buttons)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def label(self, label):
        # 按钮文字
        
        return self.set("label", label)

        
    def level(self, level):
        # 按钮级别，样式# 可选项: ['info', 'success', 'danger', 'warning', 'primary', 'link']
        
        return self.set("level", level)

        
    def closeOnOutside(self, closeOnOutside):
        # 点击外部是否关闭
        
        return self.set("closeOnOutside", closeOnOutside)

        
    def closeOnClick(self, closeOnClick):
        # 点击内容是否关闭
        
        return self.set("closeOnClick", closeOnClick)

        
    def size(self, size):
        # 按钮大小# 可选项: ['xs', 'sm', 'md', 'lg']
        
        return self.set("size", size)

        
    def align(self, align):
        # 对齐方式# 可选项: ['left', 'right']
        
        return self.set("align", align)

        
    def iconOnly(self, iconOnly):
        # 是否只显示图标。
        
        return self.set("iconOnly", iconOnly)

        
    def rightIcon(self, rightIcon):
        # 右侧图标
        # iconfont 里面的类名。
        return self.set("rightIcon", rightIcon)

        
    def trigger(self, trigger):
        # 触发条件，默认是 click# 可选项: ['click', 'hover']
        
        return self.set("trigger", trigger)

        
    def hideCaret(self, hideCaret):
        # 是否显示下拉按钮
        
        return self.set("hideCaret", hideCaret)

        
    def menuClassName(self, menuClassName):
        # 菜单 CSS 样式
        
        return self.set("menuClassName", menuClassName)

        
    def overlayPlacement(self, overlayPlacement):
        
        
        return self.set("overlayPlacement", overlayPlacement)

        