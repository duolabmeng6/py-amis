
from amis.AmisComponent import AmisComponent

class Carousel(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "carousel")
        
    
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
        # 指定为轮播图类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def auto(self, auto):
        # 是否自动播放
        
        return self.set("auto", auto)

        
    def interval(self, interval):
        # 轮播间隔时间
        
        return self.set("interval", interval)

        
    def duration(self, duration):
        # 动画时长
        
        return self.set("duration", duration)

        
    def width(self, width):
        # 设置宽度
        
        return self.set("width", width)

        
    def height(self, height):
        # 设置高度
        
        return self.set("height", height)

        
    def controlsTheme(self, controlsTheme):
        # 可选项: ['light', 'dark']
        
        return self.set("controlsTheme", controlsTheme)

        
    def placeholder(self, placeholder):
        # 占位
        
        return self.set("placeholder", placeholder)

        
    def controls(self, controls):
        # 配置控件内容
        
        return self.set("controls", controls)

        
    def animation(self, animation):
        # 动画类型# 可选项: ['fade', 'slide']
        
        return self.set("animation", animation)

        
    def itemSchema(self, itemSchema):
        # 配置单条呈现模板
        
        return self.set("itemSchema", itemSchema)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def thumbMode(self, thumbMode):
        # 预览图模式# 可选项: ['contain', 'cover']
        
        return self.set("thumbMode", thumbMode)

        
    def options(self, options):
        # 配置固定值
        
        return self.set("options", options)

        
    def alwaysShowArrow(self, alwaysShowArrow):
        # 是否一直显示箭头
        
        return self.set("alwaysShowArrow", alwaysShowArrow)

        
    def multiple(self, multiple):
        # 多图模式配置项
        
        return self.set("multiple", multiple)

        
    def icons(self, icons):
        # 自定义箭头图标
        
        return self.set("icons", icons)

        