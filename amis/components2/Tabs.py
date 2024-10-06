
from amis.AmisComponent import AmisComponent

class Tabs(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tabs")
        
    
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

        
    def tabs(self, tabs):
        # 选项卡成员。当配置了 source 时，选项卡成员，将会根据目标数据进行重复。
        
        return self.set("tabs", tabs)

        
    def source(self, source):
        # 关联已有数据，选项卡直接根据目标数据重复。
        
        return self.set("source", source)

        
    def tabsMode(self, tabsMode):
        # 展示形式
        
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
        # 可以在右侧配置点其他功能按钮。
        
        return self.set("toolbar", toolbar)

        
    def subFormMode(self, subFormMode):
        # 配置子表单项默认的展示方式。# 可选项: ['normal', 'inline', 'horizontal']
        
        return self.set("subFormMode", subFormMode)

        
    def subFormHorizontal(self, subFormHorizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("subFormHorizontal", subFormHorizontal)

        
    def addable(self, addable):
        # 是否支持新增
        
        return self.set("addable", addable)

        
    def closable(self, closable):
        # 是否支持删除
        
        return self.set("closable", closable)

        
    def draggable(self, draggable):
        # 是否支持拖拽
        
        return self.set("draggable", draggable)

        
    def showTip(self, showTip):
        # 是否显示提示
        
        return self.set("showTip", showTip)

        
    def showTipClassName(self, showTipClassName):
        # tooltip 提示的类名
        
        return self.set("showTipClassName", showTipClassName)

        
    def editable(self, editable):
        # 是否可编辑标签名
        
        return self.set("editable", editable)

        
    def scrollable(self, scrollable):
        # 是否导航支持内容溢出滚动。属性废弃，为了兼容暂且保留
        
        return self.set("scrollable", scrollable)

        
    def sidePosition(self, sidePosition):
        # 编辑器模式，侧边的位置# 可选项: ['left', 'right']
        
        return self.set("sidePosition", sidePosition)

        
    def addBtnText(self, addBtnText):
        # 自定义增加按钮文案
        
        return self.set("addBtnText", addBtnText)

        
    def defaultKey(self, defaultKey):
        # 初始化激活的选项卡，hash值或索引值，支持使用表达式
        
        return self.set("defaultKey", defaultKey)

        
    def activeKey(self, activeKey):
        # 激活的选项卡，hash值或索引值，支持使用表达式
        
        return self.set("activeKey", activeKey)

        
    def collapseOnExceed(self, collapseOnExceed):
        # 超过多少个时折叠按钮
        
        return self.set("collapseOnExceed", collapseOnExceed)

        
    def collapseBtnLabel(self, collapseBtnLabel):
        # 折叠按钮文字
        
        return self.set("collapseBtnLabel", collapseBtnLabel)

        
    def swipeable(self, swipeable):
        # 是否滑动切换只在移动端生效
        
        return self.set("swipeable", swipeable)

        