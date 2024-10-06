
from amis.AmisComponent import AmisComponent

class Service(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "service")
        
    
    def loadingConfig(self, loadingConfig):
        
        
        return self.set("loadingConfig", loadingConfig)

        
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
        # 指定为 Service 数据拉取控件。
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def api(self, api):
        # 页面初始化的时候，可以设置一个 API 让其取拉取，发送数据会携带当前 data 数据（包含地址栏参数），获取得数据会合并到 data 中，供组件内使用。
        
        return self.set("api", api)

        
    def ws(self, ws):
        # WebScocket 地址，用于实时获取数据
        
        return self.set("ws", ws)

        
    def dataProvider(self, dataProvider):
        # 通过调用外部函数来获取数据
        
        return self.set("dataProvider", dataProvider)

        
    def body(self, body):
        # 内容区域
        
        return self.set("body", body)

        
    def fetchOn(self, fetchOn):
        
        # 表达式，语法 `data.xxx > 5`。
        return self.set("fetchOn", fetchOn)

        
    def initFetch(self, initFetch):
        # 是否默认就拉取？
        
        return self.set("initFetch", initFetch)

        
    def initFetchOn(self, initFetchOn):
        # 是否默认就拉取？通过表达式来决定.
        # 表达式，语法 `data.xxx > 5`。
        return self.set("initFetchOn", initFetchOn)

        
    def schemaApi(self, schemaApi):
        # 用来获取远程 Schema 的 api
        
        return self.set("schemaApi", schemaApi)

        
    def initFetchSchema(self, initFetchSchema):
        # 是否默认加载 schemaApi
        
        return self.set("initFetchSchema", initFetchSchema)

        
    def initFetchSchemaOn(self, initFetchSchemaOn):
        # 用表达式来配置。
        # 表达式，语法 `data.xxx > 5`。
        return self.set("initFetchSchemaOn", initFetchSchemaOn)

        
    def interval(self, interval):
        # 是否轮询拉取
        
        return self.set("interval", interval)

        
    def silentPolling(self, silentPolling):
        # 是否静默拉取
        
        return self.set("silentPolling", silentPolling)

        
    def stopAutoRefreshWhen(self, stopAutoRefreshWhen):
        # 关闭轮询的条件。
        # 表达式，语法 `data.xxx > 5`。
        return self.set("stopAutoRefreshWhen", stopAutoRefreshWhen)

        
    def messages(self, messages):
        
        # 消息文案配置，记住这个优先级是最低的，如果你的接口返回了 msg，接口返回的优先。
        return self.set("messages", messages)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def showErrorMsg(self, showErrorMsg):
        # 是否以Alert的形式显示api接口响应的错误信息，默认展示
        
        return self.set("showErrorMsg", showErrorMsg)

        