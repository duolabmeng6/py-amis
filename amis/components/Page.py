
from amis.AmisComponent import AmisComponent

class Page(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "page")
        
    
    def loadingConfig(self, loadingConfig):
        
        
        return self.set("loadingConfig", loadingConfig)

        
    def className(self, className):
        # 配置容器 className
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
        # 自定义样式
        
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
        # 指定为 page 渲染器。
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def title(self, title):
        # 页面标题
        
        return self.set("title", title)

        
    def subTitle(self, subTitle):
        # 页面副标题
        
        return self.set("subTitle", subTitle)

        
    def remark(self, remark):
        # 页面描述, 标题旁边会出现个小图标，放上去会显示这个属性配置的内容。
        
        return self.set("remark", remark)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def bodyClassName(self, bodyClassName):
        # 内容区 css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("bodyClassName", bodyClassName)

        
    def aside(self, aside):
        # 边栏区域
        
        return self.set("aside", aside)

        
    def asideResizor(self, asideResizor):
        # 边栏是否允许拖动
        
        return self.set("asideResizor", asideResizor)

        
    def asideSticky(self, asideSticky):
        # 边栏内容是否粘住，即不跟随滚动。
        
        return self.set("asideSticky", asideSticky)

        
    def asideMinWidth(self, asideMinWidth):
        # 边栏最小宽度
        
        return self.set("asideMinWidth", asideMinWidth)

        
    def asideMaxWidth(self, asideMaxWidth):
        # 边栏最小宽度
        
        return self.set("asideMaxWidth", asideMaxWidth)

        
    def asideClassName(self, asideClassName):
        # 边栏区 css 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("asideClassName", asideClassName)

        
    def css(self, css):
        # 自定义页面级别样式表
        
        return self.set("css", css)

        
    def mobileCSS(self, mobileCSS):
        # 移动端下的样式表
        
        return self.set("mobileCSS", mobileCSS)

        
    def data(self, data):
        # 页面级别的初始数据
        # 初始数据，设置得值可用于组件内部模板使用。
        return self.set("data", data)

        
    def headerClassName(self, headerClassName):
        # 配置 header 容器 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def initApi(self, initApi):
        # 页面初始化的时候，可以设置一个 API 让其取拉取，发送数据会携带当前 data 数据（包含地址栏参数），获取得数据会合并到 data 中，供组件内使用。
        
        return self.set("initApi", initApi)

        
    def initFetch(self, initFetch):
        # 是否默认就拉取？
        
        return self.set("initFetch", initFetch)

        
    def initFetchOn(self, initFetchOn):
        # 是否默认就拉取表达式
        # 表达式，语法 `data.xxx > 5`。
        return self.set("initFetchOn", initFetchOn)

        
    def messages(self, messages):
        
        # 消息文案配置，记住这个优先级是最低的，如果你的接口返回了 msg，接口返回的优先。
        return self.set("messages", messages)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def toolbar(self, toolbar):
        # 页面顶部区域，当存在 title 时在右上角显示。
        
        return self.set("toolbar", toolbar)

        
    def toolbarClassName(self, toolbarClassName):
        # 配置 toolbar 容器 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("toolbarClassName", toolbarClassName)

        
    def definitions(self, definitions):
        
        
        return self.set("definitions", definitions)

        
    def interval(self, interval):
        # 配置轮询间隔，配置后 initApi 将轮询加载。
        
        return self.set("interval", interval)

        
    def silentPolling(self, silentPolling):
        # 是否要静默加载，也就是说不显示进度
        
        return self.set("silentPolling", silentPolling)

        
    def stopAutoRefreshWhen(self, stopAutoRefreshWhen):
        # 配置停止轮询的条件。
        # 表达式，语法 `data.xxx > 5`。
        return self.set("stopAutoRefreshWhen", stopAutoRefreshWhen)

        
    def showErrorMsg(self, showErrorMsg):
        # 是否显示错误信息，默认是显示的。
        
        return self.set("showErrorMsg", showErrorMsg)

        
    def cssVars(self, cssVars):
        # css 变量
        
        return self.set("cssVars", cssVars)

        
    def regions(self, regions):
        # 默认不设置自动感觉内容来决定要不要展示这些区域 如果配置了，以配置为主。
        
        return self.set("regions", regions)

        
    def pullRefresh(self, pullRefresh):
        # 下拉刷新配置
        
        return self.set("pullRefresh", pullRefresh)

        