
from amis.AmisComponent import AmisComponent

class Tasks(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "tasks")
        
    
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
        # 指定为任务类型
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def btnClassName(self, btnClassName):
        
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnClassName", btnClassName)

        
    def btnText(self, btnText):
        # 操作按钮文字
        
        return self.set("btnText", btnText)

        
    def checkApi(self, checkApi):
        # 用来获取任务状态的 API，当没有进行时任务时不会发送。
        
        return self.set("checkApi", checkApi)

        
    def interval(self, interval):
        # 当有任务进行中，会每隔一段时间再次检测，而时间间隔就是通过此项配置，默认 3s。
        
        return self.set("interval", interval)

        
    def items(self, items):
        
        
        return self.set("items", items)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def operationLabel(self, operationLabel):
        # 操作列说明
        
        return self.set("operationLabel", operationLabel)

        
    def reSubmitApi(self, reSubmitApi):
        # 如果任务失败，且可以重试，提交的时候会使用此 API
        
        return self.set("reSubmitApi", reSubmitApi)

        
    def remarkLabel(self, remarkLabel):
        # 备注列说明
        
        return self.set("remarkLabel", remarkLabel)

        
    def retryBtnClassName(self, retryBtnClassName):
        # 配置容器重试按钮 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("retryBtnClassName", retryBtnClassName)

        
    def retryBtnText(self, retryBtnText):
        # 重试操作按钮文字
        
        return self.set("retryBtnText", retryBtnText)

        
    def statusLabel(self, statusLabel):
        # 状态列说明
        
        return self.set("statusLabel", statusLabel)

        
    def statusLabelMap(self, statusLabelMap):
        # 状态显示对应的类名配置。
        
        return self.set("statusLabelMap", statusLabelMap)

        
    def statusTextMap(self, statusTextMap):
        # 状态显示对应的文字显示配置。
        
        return self.set("statusTextMap", statusTextMap)

        
    def submitApi(self, submitApi):
        # 提交任务使用的 API
        
        return self.set("submitApi", submitApi)

        
    def tableClassName(self, tableClassName):
        # 配置 table className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("tableClassName", tableClassName)

        
    def taskNameLabel(self, taskNameLabel):
        # 任务名称列说明
        
        return self.set("taskNameLabel", taskNameLabel)

        
    def initialStatusCode(self, initialStatusCode):
        
        
        return self.set("initialStatusCode", initialStatusCode)

        
    def readyStatusCode(self, readyStatusCode):
        
        
        return self.set("readyStatusCode", readyStatusCode)

        
    def loadingStatusCode(self, loadingStatusCode):
        
        
        return self.set("loadingStatusCode", loadingStatusCode)

        
    def canRetryStatusCode(self, canRetryStatusCode):
        
        
        return self.set("canRetryStatusCode", canRetryStatusCode)

        
    def finishStatusCode(self, finishStatusCode):
        
        
        return self.set("finishStatusCode", finishStatusCode)

        
    def errorStatusCode(self, errorStatusCode):
        
        
        return self.set("errorStatusCode", errorStatusCode)

        