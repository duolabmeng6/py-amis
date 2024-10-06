
from amis.AmisComponent import AmisComponent

class CRUDTable(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "crud")
        self.set("mode", "table")
    
    def affixHeader(self, affixHeader):
        # 是否固定表头
        
        return self.set("affixHeader", affixHeader)

        
    def affixFooter(self, affixFooter):
        # 是否固底
        
        return self.set("affixFooter", affixFooter)

        
    def columns(self, columns):
        # 表格的列信息
        
        return self.set("columns", columns)

        
    def columnsTogglable(self, columnsTogglable):
        # 展示列显示开关，自动即：列数量大于或等于5个时自动开启
        
        return self.set("columnsTogglable", columnsTogglable)

        
    def footable(self, footable):
        # 是否开启底部展示功能，适合移动端展示
        
        return self.set("footable", footable)

        
    def footerClassName(self, footerClassName):
        # 底部外层 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("footerClassName", footerClassName)

        
    def headerClassName(self, headerClassName):
        # 顶部外层 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def placeholder(self, placeholder):
        # 占位符
        
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

        
    def tableClassName(self, tableClassName):
        # 表格 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("tableClassName", tableClassName)

        
    def title(self, title):
        # 标题
        
        return self.set("title", title)

        
    def toolbarClassName(self, toolbarClassName):
        # 工具栏 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("toolbarClassName", toolbarClassName)

        
    def combineNum(self, combineNum):
        # 合并单元格配置，配置数字表示从左到右的多少列自动合并单元格。
        
        return self.set("combineNum", combineNum)

        
    def combineFromIndex(self, combineFromIndex):
        # 合并单元格配置，配置从第几列开始合并。
        
        return self.set("combineFromIndex", combineFromIndex)

        
    def prefixRow(self, prefixRow):
        # 顶部总结行
        
        return self.set("prefixRow", prefixRow)

        
    def affixRow(self, affixRow):
        # 底部总结行
        
        return self.set("affixRow", affixRow)

        
    def resizable(self, resizable):
        # 是否可调整列宽
        
        return self.set("resizable", resizable)

        
    def rowClassNameExpr(self, rowClassNameExpr):
        # 行样式表表达式
        
        return self.set("rowClassNameExpr", rowClassNameExpr)

        
    def itemBadge(self, itemBadge):
        # 行角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("itemBadge", itemBadge)

        
    def autoGenerateFilter(self, autoGenerateFilter):
        # 开启查询区域，会根据列元素的searchable属性值，自动生成查询条件表单
        
        return self.set("autoGenerateFilter", autoGenerateFilter)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 表格是否可以获取父级数据域值，默认为false
        
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def autoFillHeight(self, autoFillHeight):
        # 内容区域占满屏幕剩余空间
        
        return self.set("autoFillHeight", autoFillHeight)

        
    def tableLayout(self, tableLayout):
        # table layout# 可选项: ['fixed', 'auto']
        
        return self.set("tableLayout", tableLayout)

        
    def deferApi(self, deferApi):
        # 懒加载 API，当行数据中用 defer: true 标记了，则其孩子节点将会用这个 API 来拉取数据。
        
        return self.set("deferApi", deferApi)

        
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

        
    def mode(self, mode):
        # 指定内容区的展示模式。
        
        return self.set("mode", mode)

        
    def loadingConfig(self, loadingConfig):
        
        
        return self.set("loadingConfig", loadingConfig)

        
    def type(self, type):
        # 指定为 CRUD 渲染器。
        
        return self.set("type", type)

        
    def api(self, api):
        # 初始化数据 API
        
        return self.set("api", api)

        
    def bulkActions(self, bulkActions):
        # 批量操作
        
        return self.set("bulkActions", bulkActions)

        
    def itemActions(self, itemActions):
        # 单条操作
        
        return self.set("itemActions", itemActions)

        
    def perPage(self, perPage):
        # 每页个数，默认为 10，如果不是请设置。
        
        return self.set("perPage", perPage)

        
    def orderBy(self, orderBy):
        # 默认排序字段
        
        return self.set("orderBy", orderBy)

        
    def orderDir(self, orderDir):
        # 默认排序方向# 可选项: ['asc', 'desc']
        
        return self.set("orderDir", orderDir)

        
    def defaultParams(self, defaultParams):
        # 可以默认给定初始参数如： {\"perPage\": 24}
        
        return self.set("defaultParams", defaultParams)

        
    def draggable(self, draggable):
        # 是否可通过拖拽排序
        
        return self.set("draggable", draggable)

        
    def draggableOn(self, draggableOn):
        # 是否可通过拖拽排序，通过表达式来配置
        # 表达式，语法 `data.xxx > 5`。
        return self.set("draggableOn", draggableOn)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def filter(self, filter):
        # 过滤器表单
        
        return self.set("filter", filter)

        
    def initFetch(self, initFetch):
        # 初始是否拉取
        
        return self.set("initFetch", initFetch)

        
    def initFetchOn(self, initFetchOn):
        # 初始是否拉取，用表达式来配置。
        # 表达式，语法 `data.xxx > 5`。
        return self.set("initFetchOn", initFetchOn)

        
    def innerClassName(self, innerClassName):
        # 配置内部 DOM 的 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("innerClassName", innerClassName)

        
    def interval(self, interval):
        # 设置自动刷新时间
        
        return self.set("interval", interval)

        
    def orderField(self, orderField):
        # 设置用来确定位置的字段名，设置后新的顺序将被赋值到该字段中。
        
        return self.set("orderField", orderField)

        
    def pageField(self, pageField):
        # 设置分页页码字段名。
        
        return self.set("pageField", pageField)

        
    def perPageField(self, perPageField):
        # 设置分页一页显示的多少条数据的字段名。
        
        return self.set("perPageField", perPageField)

        
    def pageDirectionField(self, pageDirectionField):
        # 设置分页方向的字段名。单位简单分页时清楚时向前还是向后翻页。
        
        return self.set("pageDirectionField", pageDirectionField)

        
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

        
    def headerToolbar(self, headerToolbar):
        # 顶部工具栏
        
        return self.set("headerToolbar", headerToolbar)

        
    def footerToolbar(self, footerToolbar):
        # 底部工具栏
        
        return self.set("footerToolbar", footerToolbar)

        
    def perPageAvailable(self, perPageAvailable):
        # 每页显示多少个空间成员的配置如： [10, 20, 50, 100]。
        
        return self.set("perPageAvailable", perPageAvailable)

        
    def messages(self, messages):
        
        # 消息文案配置，记住这个优先级是最低的，如果你的接口返回了 msg，接口返回的优先。
        return self.set("messages", messages)

        
    def hideQuickSaveBtn(self, hideQuickSaveBtn):
        # 是否隐藏快速编辑的按钮。
        
        return self.set("hideQuickSaveBtn", hideQuickSaveBtn)

        
    def autoJumpToTopOnPagerChange(self, autoJumpToTopOnPagerChange):
        # 是否自动跳顶部，当切分页的时候。
        
        return self.set("autoJumpToTopOnPagerChange", autoJumpToTopOnPagerChange)

        
    def silentPolling(self, silentPolling):
        # 静默拉取
        
        return self.set("silentPolling", silentPolling)

        
    def stopAutoRefreshWhen(self, stopAutoRefreshWhen):
        
        # 表达式，语法 `data.xxx > 5`。
        return self.set("stopAutoRefreshWhen", stopAutoRefreshWhen)

        
    def stopAutoRefreshWhenModalIsOpen(self, stopAutoRefreshWhenModalIsOpen):
        
        
        return self.set("stopAutoRefreshWhenModalIsOpen", stopAutoRefreshWhenModalIsOpen)

        
    def filterTogglable(self, filterTogglable):
        
        
        return self.set("filterTogglable", filterTogglable)

        
    def filterDefaultVisible(self, filterDefaultVisible):
        
        
        return self.set("filterDefaultVisible", filterDefaultVisible)

        
    def syncResponse2Query(self, syncResponse2Query):
        # 是否将接口返回的内容自动同步到地址栏，前提是开启了同步地址栏。
        
        return self.set("syncResponse2Query", syncResponse2Query)

        
    def keepItemSelectionOnPageChange(self, keepItemSelectionOnPageChange):
        # 分页的时候是否保留用户选择。
        
        return self.set("keepItemSelectionOnPageChange", keepItemSelectionOnPageChange)

        
    def labelTpl(self, labelTpl):
        # 当配置 keepItemSelectionOnPageChange 时有用，用来配置已勾选项的文案。
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("labelTpl", labelTpl)

        
    def loadDataOnce(self, loadDataOnce):
        # 是否为前端单次加载模式，可以用来实现前端分页。
        
        return self.set("loadDataOnce", loadDataOnce)

        
    def loadDataOnceFetchOnFilter(self, loadDataOnceFetchOnFilter):
        # 在开启loadDataOnce时，当修改过滤条件时是否重新请求api  如果没有配置，当查询条件表单触发的会重新请求 api，当是列过滤或者是 search-box 触发的则不重新请求 api 如果配置为 true，则不管是什么触发都会重新请求 api 如果配置为 false 则不管是什么触发都不会重新请求 api
        
        return self.set("loadDataOnceFetchOnFilter", loadDataOnceFetchOnFilter)

        
    def matchFunc(self, matchFunc):
        # 自定义搜索匹配函数，当开启loadDataOnce时，会基于该函数计算的匹配结果进行过滤，主要用于处理列字段类型较为复杂或者字段值格式和后端返回不一致的场景
        
        return self.set("matchFunc", matchFunc)

        
    def expandConfig(self, expandConfig):
        # 如果时内嵌模式，可以通过这个来配置默认的展开选项。
        
        return self.set("expandConfig", expandConfig)

        
    def alwaysShowPagination(self, alwaysShowPagination):
        # 默认只有当分页数大于 1 是才显示，如果总是想显示请配置。
        
        return self.set("alwaysShowPagination", alwaysShowPagination)

        
    def parsePrimitiveQuery(self, parsePrimitiveQuery):
        # 是否开启Query信息转换，开启后将会对url中的Query进行转换，默认开启，默认仅转化布尔值
        
        return self.set("parsePrimitiveQuery", parsePrimitiveQuery)

        