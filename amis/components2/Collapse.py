
from amis.AmisComponent import AmisComponent

class Collapse(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "collapse")
        
    
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
        # 指定为折叠器类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def key(self, key):
        # 标识
        
        return self.set("key", key)

        
    def headerPosition(self, headerPosition):
        # 标题展示位置# 可选项: ['top', 'bottom']
        
        return self.set("headerPosition", headerPosition)

        
    def header(self, header):
        # 标题
        
        return self.set("header", header)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def bodyClassName(self, bodyClassName):
        # 配置 Body 容器 className
        
        return self.set("bodyClassName", bodyClassName)

        
    def collapsable(self, collapsable):
        # 是否可折叠
        
        return self.set("collapsable", collapsable)

        
    def collapsed(self, collapsed):
        # 默认是否折叠
        
        return self.set("collapsed", collapsed)

        
    def showArrow(self, showArrow):
        # 图标是否展示
        
        return self.set("showArrow", showArrow)

        
    def expandIcon(self, expandIcon):
        # 自定义切换图标
        
        return self.set("expandIcon", expandIcon)

        
    def headingClassName(self, headingClassName):
        # 标题 CSS 类名
        
        return self.set("headingClassName", headingClassName)

        
    def collapseHeader(self, collapseHeader):
        # 收起的标题
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("collapseHeader", collapseHeader)

        
    def size(self, size):
        # 控件大小# 可选项: ['xs', 'sm', 'md', 'lg', 'base']
        
        return self.set("size", size)

        
    def mountOnEnter(self, mountOnEnter):
        # 点开时才加载内容
        
        return self.set("mountOnEnter", mountOnEnter)

        
    def unmountOnExit(self, unmountOnExit):
        # 卡片隐藏就销毁内容。
        
        return self.set("unmountOnExit", unmountOnExit)

        
    def divideLine(self, divideLine):
        # 标题内容分割线
        
        return self.set("divideLine", divideLine)

        