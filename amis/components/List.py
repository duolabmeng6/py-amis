
from amis.AmisComponent import AmisComponent

class List(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "list")
        
    
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
        # 指定为 List 列表展示控件。# 可选项: ['list', 'static-list']
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def title(self, title):
        # 标题
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("title", title)

        
    def footer(self, footer):
        # 底部区域
        
        return self.set("footer", footer)

        
    def footerClassName(self, footerClassName):
        # 底部区域类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("footerClassName", footerClassName)

        
    def header(self, header):
        # 顶部区域
        
        return self.set("header", header)

        
    def headerClassName(self, headerClassName):
        # 顶部区域类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def listItem(self, listItem):
        # 单条数据展示内容配置
        
        return self.set("listItem", listItem)

        
    def source(self, source):
        # 数据源: 绑定当前环境变量
        
        return self.set("source", source)

        
    def showFooter(self, showFooter):
        # 是否显示底部
        
        return self.set("showFooter", showFooter)

        
    def showHeader(self, showHeader):
        # 是否显示头部
        
        return self.set("showHeader", showHeader)

        
    def placeholder(self, placeholder):
        # 无数据提示
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("placeholder", placeholder)

        
    def hideCheckToggler(self, hideCheckToggler):
        # 是否隐藏勾选框
        
        return self.set("hideCheckToggler", hideCheckToggler)

        
    def affixHeader(self, affixHeader):
        # 是否固顶
        
        return self.set("affixHeader", affixHeader)

        
    def affixFooter(self, affixFooter):
        # 是否固底
        
        return self.set("affixFooter", affixFooter)

        
    def itemCheckableOn(self, itemCheckableOn):
        # 配置某项是否可以点选
        # 表达式，语法 `data.xxx > 5`。
        return self.set("itemCheckableOn", itemCheckableOn)

        
    def itemDraggableOn(self, itemDraggableOn):
        # 配置某项是否可拖拽排序，前提是要开启拖拽功能
        # 表达式，语法 `data.xxx > 5`。
        return self.set("itemDraggableOn", itemDraggableOn)

        
    def checkOnItemClick(self, checkOnItemClick):
        # 点击列表单行时，是否选择
        
        return self.set("checkOnItemClick", checkOnItemClick)

        
    def valueField(self, valueField):
        # 可以用来作为值的字段
        
        return self.set("valueField", valueField)

        
    def size(self, size):
        # 大小# 可选项: ['sm', 'base']
        
        return self.set("size", size)

        
    def itemAction(self, itemAction):
        # 点击列表项的行为
        
        return self.set("itemAction", itemAction)

        