
from amis.AmisComponent import AmisComponent

class CRUD2Cards(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "crud2")
        self.set("mode", "cards")
    
    def card(self, card):
        
        
        return self.set("card", card)

        
    def headerClassName(self, headerClassName):
        # 头部 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def footerClassName(self, footerClassName):
        # 底部 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("footerClassName", footerClassName)

        
    def itemClassName(self, itemClassName):
        # 卡片 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("itemClassName", itemClassName)

        
    def placeholder(self, placeholder):
        # 无数据提示
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("placeholder", placeholder)

        
    def showFooter(self, showFooter):
        # 是否显示底部
        
        return self.set("showFooter", showFooter)

        
    def showHeader(self, showHeader):
        # 是否显示头部
        
        return self.set("showHeader", showHeader)

        
    def source(self, source):
        # 也可以直接从环境变量中读取，但是不太推荐。
        
        return self.set("source", source)

        
    def title(self, title):
        # 标题
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("title", title)

        
    def hideCheckToggler(self, hideCheckToggler):
        # 是否隐藏勾选框
        
        return self.set("hideCheckToggler", hideCheckToggler)

        
    def affixHeader(self, affixHeader):
        # 是否固顶
        
        return self.set("affixHeader", affixHeader)

        
    def affixFooter(self, affixFooter):
        # 是否固底
        
        return self.set("affixFooter", affixFooter)

        
    def header(self, header):
        # 顶部区域
        
        return self.set("header", header)

        
    def footer(self, footer):
        # 底部区域
        
        return self.set("footer", footer)

        
    def itemCheckableOn(self, itemCheckableOn):
        # 配置某项是否可以点选
        # 表达式，语法 `data.xxx > 5`。
        return self.set("itemCheckableOn", itemCheckableOn)

        
    def itemDraggableOn(self, itemDraggableOn):
        # 配置某项是否可拖拽排序，前提是要开启拖拽功能
        # 表达式，语法 `data.xxx > 5`。
        return self.set("itemDraggableOn", itemDraggableOn)

        
    def checkOnItemClick(self, checkOnItemClick):
        # 点击卡片的时候是否勾选卡片。
        
        return self.set("checkOnItemClick", checkOnItemClick)

        
    def masonryLayout(self, masonryLayout):
        # 是否为瀑布流布局？
        
        return self.set("masonryLayout", masonryLayout)

        
    def valueField(self, valueField):
        # 可以用来作为值的字段
        
        return self.set("valueField", valueField)

        
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

        
    def loadingConfig(self, loadingConfig):
        
        
        return self.set("loadingConfig", loadingConfig)

        
    def mode(self, mode):
        # 指定内容区的展示模式。
        
        return self.set("mode", mode)

        
    def type(self, type):
        # 指定为 CRUD2 渲染器。
        
        return self.set("type", type)

        
    def api(self, api):
        # 初始化数据 API
        
        return self.set("api", api)

        
    def silentPolling(self, silentPolling):
        # 静默拉取
        
        return self.set("silentPolling", silentPolling)

        
    def interval(self, interval):
        # 设置自动刷新时间
        
        return self.set("interval", interval)

        
    def stopAutoRefreshWhen(self, stopAutoRefreshWhen):
        
        # 表达式，语法 `data.xxx > 5`。
        return self.set("stopAutoRefreshWhen", stopAutoRefreshWhen)

        
    def loadType(self, loadType):
        # 数据展示模式 无限加载 or 分页# 可选项: ['more', 'pagination']
        
        return self.set("loadType", loadType)

        
    def perPage(self, perPage):
        # 无限加载时，根据此项设置其每页加载数量，可以不限制
        
        return self.set("perPage", perPage)

        
    def loadDataOnce(self, loadDataOnce):
        # 是否为前端单次加载模式，可以用来实现前端分页。
        
        return self.set("loadDataOnce", loadDataOnce)

        
    def selectable(self, selectable):
        # 是否可以选择数据，外部事件动作
        
        return self.set("selectable", selectable)

        
    def multiple(self, multiple):
        # 是否可以多选数据，仅当selectable为 true 时生效
        
        return self.set("multiple", multiple)

        
    def showSelection(self, showSelection):
        # 是否展示已选数据区域，仅当selectable为 true 时生效
        
        return self.set("showSelection", showSelection)

        
    def quickSaveApi(self, quickSaveApi):
        # 快速编辑后用来批量保存的 API
        
        return self.set("quickSaveApi", quickSaveApi)

        
    def quickSaveItemApi(self, quickSaveItemApi):
        # 快速编辑配置成及时保存时使用的 API
        
        return self.set("quickSaveItemApi", quickSaveItemApi)

        
    def saveOrderApi(self, saveOrderApi):
        # 保存排序的 api
        
        return self.set("saveOrderApi", saveOrderApi)

        
    def syncLocation(self, syncLocation):
        # 是否将过滤条件的参数同步到地址栏,默认为true
        
        return self.set("syncLocation", syncLocation)

        
    def pageField(self, pageField):
        # 设置分页页码字段名。
        
        return self.set("pageField", pageField)

        
    def perPageField(self, perPageField):
        # 设置分页一页显示的多少条数据的字段名。
        
        return self.set("perPageField", perPageField)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def hideQuickSaveBtn(self, hideQuickSaveBtn):
        # 是否隐藏快速编辑的按钮。
        
        return self.set("hideQuickSaveBtn", hideQuickSaveBtn)

        
    def autoJumpToTopOnPagerChange(self, autoJumpToTopOnPagerChange):
        # 是否自动跳顶部，当切分页的时候。
        
        return self.set("autoJumpToTopOnPagerChange", autoJumpToTopOnPagerChange)

        
    def headerToolbar(self, headerToolbar):
        # 顶部区域
        
        return self.set("headerToolbar", headerToolbar)

        
    def headerToolbarClassName(self, headerToolbarClassName):
        # 顶部区域CSS类名
        
        return self.set("headerToolbarClassName", headerToolbarClassName)

        
    def footerToolbar(self, footerToolbar):
        # 底部区域
        
        return self.set("footerToolbar", footerToolbar)

        
    def footerToolbarClassName(self, footerToolbarClassName):
        # 底部区域CSS类名
        
        return self.set("footerToolbarClassName", footerToolbarClassName)

        
    def syncResponse2Query(self, syncResponse2Query):
        # 是否将接口返回的内容自动同步到地址栏，前提是开启了同步地址栏。
        
        return self.set("syncResponse2Query", syncResponse2Query)

        
    def keepItemSelectionOnPageChange(self, keepItemSelectionOnPageChange):
        # 翻页时是否保留用户已选的数据
        
        return self.set("keepItemSelectionOnPageChange", keepItemSelectionOnPageChange)

        
    def autoFillHeight(self, autoFillHeight):
        # 内容区域占满屏幕剩余空间
        
        return self.set("autoFillHeight", autoFillHeight)

        
    def primaryField(self, primaryField):
        # 行标识符，默认为id
        
        return self.set("primaryField", primaryField)

        
    def parsePrimitiveQuery(self, parsePrimitiveQuery):
        # 是否开启Query信息转换，开启后将会对url中的Query进行转换，默认开启，默认仅转化布尔值
        
        return self.set("parsePrimitiveQuery", parsePrimitiveQuery)

        