
from amis.AmisComponent import AmisComponent

class Portlet(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "portlet")
        
    
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
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
        # 自定义样式
        
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
        # 指定为 portlet 类型
        
        return self.set("type", type)

        
    def tabs(self, tabs):
        
        
        return self.set("tabs", tabs)

        
    def source(self, source):
        # 关联已有数据，选项卡直接根据目标数据重复。
        
        return self.set("source", source)

        
    def tabsClassName(self, tabsClassName):
        # 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("tabsClassName", tabsClassName)

        
    def tabsMode(self, tabsMode):
        # 展示形式# 可选项: ['', 'line', 'card', 'radio', 'vertical', 'tiled']
        
        return self.set("tabsMode", tabsMode)

        
    def contentClassName(self, contentClassName):
        # 内容类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("contentClassName", contentClassName)

        
    def linksClassName(self, linksClassName):
        # 链接外层类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("linksClassName", linksClassName)

        
    def mountOnEnter(self, mountOnEnter):
        # 卡片是否只有在点开的时候加载？
        
        return self.set("mountOnEnter", mountOnEnter)

        
    def unmountOnExit(self, unmountOnExit):
        # 卡片隐藏的时候是否销毁卡片内容
        
        return self.set("unmountOnExit", unmountOnExit)

        
    def toolbar(self, toolbar):
        # 可以在右侧配置点其他功能按钮。不会随着tab切换
        
        return self.set("toolbar", toolbar)

        
    def scrollable(self, scrollable):
        # 是否支持溢出滚动
        
        return self.set("scrollable", scrollable)

        
    def divider(self, divider):
        # header和内容是否展示分割线
        
        return self.set("divider", divider)

        
    def description(self, description):
        # 标题右侧的描述
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("description", description)

        
    def hideHeader(self, hideHeader):
        # 隐藏头部
        
        return self.set("hideHeader", hideHeader)

        