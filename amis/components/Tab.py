
from amis.AmisComponent import AmisComponent

class Tab(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tab")
        
    
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

        
    def title(self, title):
        # Tab 标题
        
        return self.set("title", title)

        
    def tab(self, tab):
        # 内容
        
        return self.set("tab", tab)

        
    def body(self, body):
        # 内容
        
        return self.set("body", body)

        
    def badge(self, badge):
        # 徽标
        
        return self.set("badge", badge)

        
    def hash(self, hash):
        # 设置以后将跟url的hash对应
        
        return self.set("hash", hash)

        
    def icon(self, icon):
        # 按钮图标
        # iconfont 里面的类名。
        return self.set("icon", icon)

        
    def iconPosition(self, iconPosition):
        # 可选项: ['left', 'right']
        
        return self.set("iconPosition", iconPosition)

        
    def reload(self, reload):
        # 设置以后内容每次都会重新渲染
        
        return self.set("reload", reload)

        
    def mountOnEnter(self, mountOnEnter):
        # 点开时才加载卡片内容
        
        return self.set("mountOnEnter", mountOnEnter)

        
    def unmountOnExit(self, unmountOnExit):
        # 卡片隐藏就销毁卡片节点。
        
        return self.set("unmountOnExit", unmountOnExit)

        
    def mode(self, mode):
        # 配置子表单项默认的展示方式。# 可选项: ['normal', 'inline', 'horizontal']
        
        return self.set("mode", mode)

        
    def horizontal(self, horizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("horizontal", horizontal)

        
    def closable(self, closable):
        # 是否可关闭，优先级高于 tabs 的 closable
        
        return self.set("closable", closable)

        