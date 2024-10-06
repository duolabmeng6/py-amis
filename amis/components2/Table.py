
from amis.AmisComponent import AmisComponent

class Table(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "table")
        
    
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
        # 指定为表格渲染器。# 可选项: ['table', 'static-table']
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
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
        # 数据源：绑定当前环境变量
        
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
        # 表格自动计算高度
        
        return self.set("autoFillHeight", autoFillHeight)

        
    def tableLayout(self, tableLayout):
        # table layout# 可选项: ['fixed', 'auto']
        
        return self.set("tableLayout", tableLayout)

        
    def deferApi(self, deferApi):
        # 懒加载 API，当行数据中用 defer: true 标记了，则其孩子节点将会用这个 API 来拉取数据。
        
        return self.set("deferApi", deferApi)

        