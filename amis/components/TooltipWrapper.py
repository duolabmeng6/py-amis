
from amis.AmisComponent import AmisComponent

class TooltipWrapper(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tooltip-wrapper")
        
    
    def className(self, className):
        # 内容区CSS类名
        
        return self.set("className", className)

        
    def disabled(self, disabled):
        # 是否禁用提示
        
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
        # 内容区自定义样式
        
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
        # 文字提示容器
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def title(self, title):
        # 文字提示标题
        
        return self.set("title", title)

        
    def content(self, content):
        # 文字提示内容，兼容 tooltip，但建议通过 content 来实现提示内容
        
        return self.set("content", content)

        
    def tooltip(self, tooltip):
        
        
        return self.set("tooltip", tooltip)

        
    def placement(self, placement):
        # 文字提示浮层出现位置，默认为top# 可选项: ['top', 'right', 'bottom', 'left']
        
        return self.set("placement", placement)

        
    def offset(self, offset):
        # 浮层位置相对偏移量
        
        return self.set("offset", offset)

        
    def showArrow(self, showArrow):
        # 是否展示浮层指向箭头
        
        return self.set("showArrow", showArrow)

        
    def trigger(self, trigger):
        # 浮层触发方式，默认为hover
        
        return self.set("trigger", trigger)

        
    def mouseEnterDelay(self, mouseEnterDelay):
        # 浮层延迟显示时间, 单位 ms
        
        return self.set("mouseEnterDelay", mouseEnterDelay)

        
    def mouseLeaveDelay(self, mouseLeaveDelay):
        # 浮层延迟隐藏时间, 单位 ms
        
        return self.set("mouseLeaveDelay", mouseLeaveDelay)

        
    def rootClose(self, rootClose):
        # 是否点击非内容区域关闭提示，默认为true
        
        return self.set("rootClose", rootClose)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def wrapperComponent(self, wrapperComponent):
        # 内容区包裹标签
        
        return self.set("wrapperComponent", wrapperComponent)

        
    def inline(self, inline):
        # 内容区是否内联显示，默认为false
        
        return self.set("inline", inline)

        
    def tooltipTheme(self, tooltipTheme):
        # 主题样式， 默认为light# 可选项: ['light', 'dark']
        
        return self.set("tooltipTheme", tooltipTheme)

        
    def enterable(self, enterable):
        # 是否可以移入浮层中, 默认true
        
        return self.set("enterable", enterable)

        
    def tooltipStyle(self, tooltipStyle):
        # 自定义提示浮层样式
        
        return self.set("tooltipStyle", tooltipStyle)

        
    def tooltipClassName(self, tooltipClassName):
        # 文字提示浮层CSS类名
        
        return self.set("tooltipClassName", tooltipClassName)

        