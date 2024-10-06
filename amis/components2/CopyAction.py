
from amis.AmisComponent import AmisComponent

class CopyAction(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "copy-action")
        
    
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
        # 主要用于用户行为跟踪里区分是哪个按钮
        
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
        # 指定按钮类型，支持 button、submit或者reset三种类型。# 可选项: ['button', 'submit', 'reset']
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def block(self, block):
        # 是否为块状展示，默认为内联。
        
        return self.set("block", block)

        
    def disabledTip(self, disabledTip):
        # 禁用时的文案提示。
        
        return self.set("disabledTip", disabledTip)

        
    def icon(self, icon):
        # 按钮图标， iconfont 的类名
        # iconfont 里面的类名。
        return self.set("icon", icon)

        
    def iconClassName(self, iconClassName):
        # icon 上的css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("iconClassName", iconClassName)

        
    def rightIcon(self, rightIcon):
        # 右侧按钮图标， iconfont 的类名
        # iconfont 里面的类名。
        return self.set("rightIcon", rightIcon)

        
    def rightIconClassName(self, rightIconClassName):
        # 右侧 icon 上的 css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("rightIconClassName", rightIconClassName)

        
    def loadingClassName(self, loadingClassName):
        # loading 上的css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("loadingClassName", loadingClassName)

        
    def label(self, label):
        # 按钮文字
        
        return self.set("label", label)

        
    def level(self, level):
        # 按钮样式# 可选项: ['info', 'success', 'warning', 'danger', 'link', 'primary', 'dark', 'light', 'secondary']
        
        return self.set("level", level)

        
    def primary(self, primary):
        
        
        return self.set("primary", primary)

        
    def size(self, size):
        # 按钮大小# 可选项: ['xs', 'sm', 'md', 'lg']
        
        return self.set("size", size)

        
    def tooltip(self, tooltip):
        
        
        return self.set("tooltip", tooltip)

        
    def tooltipPlacement(self, tooltipPlacement):
        # 可选项: ['top', 'right', 'bottom', 'left']
        
        return self.set("tooltipPlacement", tooltipPlacement)

        
    def confirmText(self, confirmText):
        # 提示文字，配置了操作前会要求用户确认。
        
        return self.set("confirmText", confirmText)

        
    def required(self, required):
        # 如果按钮在form中，配置此属性会要求用户把指定的字段通过验证后才会触发行为。
        
        return self.set("required", required)

        
    def activeLevel(self, activeLevel):
        # 激活状态时的样式
        
        return self.set("activeLevel", activeLevel)

        
    def activeClassName(self, activeClassName):
        # 激活状态时的类名
        
        return self.set("activeClassName", activeClassName)

        
    def close(self, close):
        # 如果按钮在弹框中，可以配置这个动作完成后是否关闭弹窗，或者指定关闭目标弹框。
        
        return self.set("close", close)

        
    def requireSelected(self, requireSelected):
        # 当按钮时批量操作按钮时，默认必须有勾选元素才能可点击，如果此属性配置成 false，则没有点选成员也能点击。
        
        return self.set("requireSelected", requireSelected)

        
    def mergeData(self, mergeData):
        # 是否将弹框中数据 merge 到父级作用域。
        
        return self.set("mergeData", mergeData)

        
    def target(self, target):
        # 可以指定让谁来触发这个动作。
        
        return self.set("target", target)

        
    def countDown(self, countDown):
        # 点击后的禁止倒计时（秒）
        
        return self.set("countDown", countDown)

        
    def countDownTpl(self, countDownTpl):
        # 倒计时文字自定义
        
        return self.set("countDownTpl", countDownTpl)

        
    def badge(self, badge):
        # 角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("badge", badge)

        
    def hotKey(self, hotKey):
        # 键盘快捷键
        
        return self.set("hotKey", hotKey)

        
    def loadingOn(self, loadingOn):
        # 是否显示loading效果
        
        return self.set("loadingOn", loadingOn)

        
    def onClick(self, onClick):
        # 自定义事件处理函数
        
        return self.set("onClick", onClick)

        
    def body(self, body):
        # 子内容
        
        return self.set("body", body)

        
    def actionType(self, actionType):
        # 指定为复制内容行为
        
        return self.set("actionType", actionType)

        
    def copy(self, copy):
        # 复制啥内容由此配置，支持模板语法。
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("copy", copy)

        