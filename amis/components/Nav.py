
from amis.AmisComponent import AmisComponent

class Nav(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "nav")
        
    
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
        # 指定为 Nav 导航渲染器
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def links(self, links):
        # 链接地址集合
        
        return self.set("links", links)

        
    def indentSize(self, indentSize):
        
        
        return self.set("indentSize", indentSize)

        
    def source(self, source):
        # 可以通过 API 拉取。
        
        return self.set("source", source)

        
    def deferApi(self, deferApi):
        # 懒加载 api，如果不配置复用 source 接口。
        
        return self.set("deferApi", deferApi)

        
    def stacked(self, stacked):
        # true 为垂直排列，false 为水平排列类似如 tabs。# 可选项: [True, False]
        
        return self.set("stacked", stacked)

        
    def itemActions(self, itemActions):
        # 更多操作菜单列表
        
        return self.set("itemActions", itemActions)

        
    def draggable(self, draggable):
        # 可拖拽
        
        return self.set("draggable", draggable)

        
    def saveOrderApi(self, saveOrderApi):
        # 保存排序的 api
        
        return self.set("saveOrderApi", saveOrderApi)

        
    def itemBadge(self, itemBadge):
        # 角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("itemBadge", itemBadge)

        
    def badge(self, badge):
        # 角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("badge", badge)

        
    def dragOnSameLevel(self, dragOnSameLevel):
        # 仅允许同层级拖拽
        
        return self.set("dragOnSameLevel", dragOnSameLevel)

        
    def overflow(self, overflow):
        # 横向导航时自动收纳配置
        
        return self.set("overflow", overflow)

        
    def level(self, level):
        # 最多展示多少层级
        
        return self.set("level", level)

        
    def defaultOpenLevel(self, defaultOpenLevel):
        # 默认展开层级 小于等于该层数的节点默认全部打开
        
        return self.set("defaultOpenLevel", defaultOpenLevel)

        
    def showKey(self, showKey):
        # 控制仅展示指定key菜单下的子菜单项
        
        return self.set("showKey", showKey)

        
    def collapsed(self, collapsed):
        # 控制菜单缩起
        
        return self.set("collapsed", collapsed)

        
    def mode(self, mode):
        # 垂直模式 非折叠状态下 控制菜单打开方式# 可选项: ['float', 'inline']
        
        return self.set("mode", mode)

        
    def expandIcon(self, expandIcon):
        # 自定义展开图标
        
        return self.set("expandIcon", expandIcon)

        
    def expandPosition(self, expandPosition):
        # 自定义展开图标位置 默认在前面 before after
        
        return self.set("expandPosition", expandPosition)

        
    def themeColor(self, themeColor):
        # 主题配色 默认light# 可选项: ['light', 'dark']
        
        return self.set("themeColor", themeColor)

        
    def accordion(self, accordion):
        # 手风琴展开 仅垂直inline模式支持
        
        return self.set("accordion", accordion)

        
    def popupClassName(self, popupClassName):
        # 子菜单项展开浮层样式
        
        return self.set("popupClassName", popupClassName)

        
    def searchable(self, searchable):
        # 是否开启搜索
        
        return self.set("searchable", searchable)

        
    def searchConfig(self, searchConfig):
        # 搜索框相关配置
        
        return self.set("searchConfig", searchConfig)

        