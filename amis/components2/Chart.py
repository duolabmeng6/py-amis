
from amis.AmisComponent import AmisComponent

class Chart(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "chart")
        
    
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
        # style样式
        
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
        # 指定为 chart 类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def chartTheme(self, chartTheme):
        # Chart 主题配置
        
        return self.set("chartTheme", chartTheme)

        
    def api(self, api):
        # 图表配置接口
        
        return self.set("api", api)

        
    def initFetch(self, initFetch):
        # 是否初始加载。
        
        return self.set("initFetch", initFetch)

        
    def initFetchOn(self, initFetchOn):
        # 是否初始加载用表达式来配置
        # 表达式，语法 `data.xxx > 5`。
        return self.set("initFetchOn", initFetchOn)

        
    def config(self, config):
        # 配置echart的config，支持数据映射。如果用了数据映射，为了同步更新，请设置 trackExpression
        
        return self.set("config", config)

        
    def trackExpression(self, trackExpression):
        # 跟踪表达式，如果这个表达式的运行结果发生变化了，则会更新 Echart，当 config 中用了数据映射时有用。
        
        return self.set("trackExpression", trackExpression)

        
    def width(self, width):
        # 宽度设置
        
        return self.set("width", width)

        
    def height(self, height):
        # 高度设置
        
        return self.set("height", height)

        
    def interval(self, interval):
        # 刷新时间
        
        return self.set("interval", interval)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def dataFilter(self, dataFilter):
        
        
        return self.set("dataFilter", dataFilter)

        
    def source(self, source):
        
        
        return self.set("source", source)

        
    def disableDataMapping(self, disableDataMapping):
        # 默认开启 Config 中的数据映射，如果想关闭，请开启此功能。
        
        return self.set("disableDataMapping", disableDataMapping)

        
    def clickAction(self, clickAction):
        # 点击行为配置，可以用来满足下钻操作等。
        
        return self.set("clickAction", clickAction)

        
    def replaceChartOption(self, replaceChartOption):
        # 默认配置时追加的，如果更新配置想完全替换配置请配置为 true.
        
        return self.set("replaceChartOption", replaceChartOption)

        
    def unMountOnHidden(self, unMountOnHidden):
        # 不可见的时候隐藏
        
        return self.set("unMountOnHidden", unMountOnHidden)

        
    def mapURL(self, mapURL):
        # 获取 geo json 文件的地址
        
        return self.set("mapURL", mapURL)

        
    def mapName(self, mapName):
        # 地图名称
        
        return self.set("mapName", mapName)

        
    def loadBaiduMap(self, loadBaiduMap):
        # 加载百度地图
        
        return self.set("loadBaiduMap", loadBaiduMap)

        