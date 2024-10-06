
from amis.AmisComponent import AmisComponent

class Pagination(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "pagination")
        
    
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

        
    def layout(self, layout):
        # 通过控制layout属性的顺序，调整分页结构 total,perPage,pager,go
        
        return self.set("layout", layout)

        
    def maxButtons(self, maxButtons):
        # 最多显示多少个分页按钮。
        
        return self.set("maxButtons", maxButtons)

        
    def mode(self, mode):
        # 模式，默认normal，如果只想简单显示可以配置成 `simple`。
        
        return self.set("mode", mode)

        
    def activePage(self, activePage):
        # 当前页数
        
        return self.set("activePage", activePage)

        
    def total(self, total):
        # 总条数
        
        return self.set("total", total)

        
    def perPage(self, perPage):
        # 每页显示条数
        
        return self.set("perPage", perPage)

        
    def showPerPage(self, showPerPage):
        # 是否展示分页切换，也同时受layout控制
        
        return self.set("showPerPage", showPerPage)

        
    def perPageAvailable(self, perPageAvailable):
        # 指定每页可以显示多少条
        
        return self.set("perPageAvailable", perPageAvailable)

        
    def showPageInput(self, showPageInput):
        # 是否显示快速跳转输入框
        
        return self.set("showPageInput", showPageInput)

        
    def hasNext(self, hasNext):
        
        
        return self.set("hasNext", hasNext)

        
    def popOverContainerSelector(self, popOverContainerSelector):
        # 弹层挂载节点
        
        return self.set("popOverContainerSelector", popOverContainerSelector)

        