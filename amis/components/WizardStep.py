
from amis.AmisComponent import AmisComponent

class WizardStep(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "wizard-step")
        
    
    def api(self, api):
        # Form 用来保存数据的 api。  详情：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/index#%E8%A1%A8%E5%8D%95%E6%8F%90%E4%BA%A4
        
        return self.set("api", api)

        
    def asyncApi(self, asyncApi):
        # 设置此属性后，表单提交发送保存接口后，还会继续轮询请求该接口，直到返回 finished 属性为 true 才 结束。
        
        return self.set("asyncApi", asyncApi)

        
    def initApi(self, initApi):
        # 用来初始化表单数据
        
        return self.set("initApi", initApi)

        
    def jumpable(self, jumpable):
        # 是否可直接跳转到该步骤，一般编辑模式需要可直接跳转查看。
        
        return self.set("jumpable", jumpable)

        
    def jumpableOn(self, jumpableOn):
        # 通过 JS 表达式来配置当前步骤可否被直接跳转到。
        # 表达式，语法 `data.xxx > 5`。
        return self.set("jumpableOn", jumpableOn)

        
    def title(self, title):
        # 表单标题
        
        return self.set("title", title)

        
    def label(self, label):
        
        
        return self.set("label", label)

        
    def actions(self, actions):
        # 按钮集合，会固定在底部显示。
        
        return self.set("actions", actions)

        
    def redirect(self, redirect):
        
        
        return self.set("redirect", redirect)

        
    def reload(self, reload):
        
        
        return self.set("reload", reload)

        
    def target(self, target):
        # 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 `CRUD` 模型的 name 值。 如果 target 目标是一个 `Form` ，则目标 `Form` 会重新触发 `initApi` 和 `schemaApi`，api 可以拿到当前 form 数据。如果目标是一个 `CRUD` 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。
        
        return self.set("target", target)

        
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
        # 展示态时的className
        
        return self.set("static", static)

        
    def staticOn(self, staticOn):
        
        # 表达式，语法 `data.xxx > 5`。
        return self.set("staticOn", staticOn)

        
    def staticPlaceholder(self, staticPlaceholder):
        # 静态展示空值占位
        
        return self.set("staticPlaceholder", staticPlaceholder)

        
    def staticClassName(self, staticClassName):
        
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

        
    def subTitle(self, subTitle):
        # 子标题
        
        return self.set("subTitle", subTitle)

        
    def icon(self, icon):
        # 图标
        
        return self.set("icon", icon)

        
    def value(self, value):
        
        
        return self.set("value", value)

        
    def description(self, description):
        # 描述
        
        return self.set("description", description)

        
    def body(self, body):
        # 表单项集合
        
        return self.set("body", body)

        
    def tabs(self, tabs):
        
        
        return self.set("tabs", tabs)

        
    def fieldSet(self, fieldSet):
        
        
        return self.set("fieldSet", fieldSet)

        
    def data(self, data):
        
        
        return self.set("data", data)

        
    def debug(self, debug):
        # 是否开启调试，开启后会在顶部实时显示表单项数据。
        
        return self.set("debug", debug)

        
    def debugConfig(self, debugConfig):
        # Debug面板配置
        
        return self.set("debugConfig", debugConfig)

        
    def initAsyncApi(self, initAsyncApi):
        # Form 用来获取初始数据的 api,与initApi不同的是，会一直轮询请求该接口，直到返回 finished 属性为 true 才 结束。
        
        return self.set("initAsyncApi", initAsyncApi)

        
    def initFinishedField(self, initFinishedField):
        # 设置了initAsyncApi后，默认会从返回数据的data.finished来判断是否完成，也可以设置成其他的xxx，就会从data.xxx中获取
        
        return self.set("initFinishedField", initFinishedField)

        
    def initCheckInterval(self, initCheckInterval):
        # 设置了initAsyncApi以后，默认拉取的时间间隔
        
        return self.set("initCheckInterval", initCheckInterval)

        
    def initFetch(self, initFetch):
        # 是否初始加载
        
        return self.set("initFetch", initFetch)

        
    def initFetchOn(self, initFetchOn):
        # 建议改成 api 的 sendOn 属性。
        
        return self.set("initFetchOn", initFetchOn)

        
    def interval(self, interval):
        # 设置后将轮询调用 initApi
        
        return self.set("interval", interval)

        
    def silentPolling(self, silentPolling):
        # 是否静默拉取
        
        return self.set("silentPolling", silentPolling)

        
    def stopAutoRefreshWhen(self, stopAutoRefreshWhen):
        # 配置停止轮询的条件
        
        return self.set("stopAutoRefreshWhen", stopAutoRefreshWhen)

        
    def persistData(self, persistData):
        # 是否开启本地缓存
        
        return self.set("persistData", persistData)

        
    def persistDataKeys(self, persistDataKeys):
        # 开启本地缓存后限制保存哪些 key
        
        return self.set("persistDataKeys", persistDataKeys)

        
    def clearPersistDataAfterSubmit(self, clearPersistDataAfterSubmit):
        # 提交成功后清空本地缓存
        
        return self.set("clearPersistDataAfterSubmit", clearPersistDataAfterSubmit)

        
    def feedback(self, feedback):
        # Form 也可以配置 feedback。
        
        return self.set("feedback", feedback)

        
    def checkInterval(self, checkInterval):
        # 轮询请求的时间间隔，默认为 3秒。设置 asyncApi 才有效
        
        return self.set("checkInterval", checkInterval)

        
    def finishedField(self, finishedField):
        # 如果决定结束的字段名不是 `finished` 请设置此属性，比如 `is_success`
        
        return self.set("finishedField", finishedField)

        
    def resetAfterSubmit(self, resetAfterSubmit):
        # 提交完后重置表单
        
        return self.set("resetAfterSubmit", resetAfterSubmit)

        
    def clearAfterSubmit(self, clearAfterSubmit):
        # 提交后清空表单
        
        return self.set("clearAfterSubmit", clearAfterSubmit)

        
    def mode(self, mode):
        # 配置表单项默认的展示方式。# 可选项: ['normal', 'inline', 'horizontal', 'flex']
        
        return self.set("mode", mode)

        
    def columnCount(self, columnCount):
        # 表单项显示为几列
        
        return self.set("columnCount", columnCount)

        
    def horizontal(self, horizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("horizontal", horizontal)

        
    def autoFocus(self, autoFocus):
        # 是否自动将第一个表单元素聚焦。
        
        return self.set("autoFocus", autoFocus)

        
    def messages(self, messages):
        # 消息文案配置，记住这个优先级是最低的，如果你的接口返回了 msg，接口返回的优先。
        
        return self.set("messages", messages)

        
    def name(self, name):
        
        
        return self.set("name", name)

        
    def panelClassName(self, panelClassName):
        # 配置容器 panel className
        
        return self.set("panelClassName", panelClassName)

        
    def primaryField(self, primaryField):
        # 设置主键 id, 当设置后，检测表单是否完成时（asyncApi），只会携带此数据。
        
        return self.set("primaryField", primaryField)

        
    def submitOnChange(self, submitOnChange):
        # 修改的时候是否直接提交表单。
        
        return self.set("submitOnChange", submitOnChange)

        
    def submitOnInit(self, submitOnInit):
        # 表单初始先提交一次，联动的时候有用
        
        return self.set("submitOnInit", submitOnInit)

        
    def submitText(self, submitText):
        # 默认的提交按钮名称，如果设置成空，则可以把默认按钮去掉。
        
        return self.set("submitText", submitText)

        
    def wrapWithPanel(self, wrapWithPanel):
        # 是否用 panel 包裹起来
        
        return self.set("wrapWithPanel", wrapWithPanel)

        
    def affixFooter(self, affixFooter):
        # 是否固定底下的按钮在底部。
        
        return self.set("affixFooter", affixFooter)

        
    def promptPageLeave(self, promptPageLeave):
        # 页面离开提示，为了防止页面不小心跳转而导致表单没有保存。
        
        return self.set("promptPageLeave", promptPageLeave)

        
    def promptPageLeaveMessage(self, promptPageLeaveMessage):
        # 具体的提示信息，选填。
        
        return self.set("promptPageLeaveMessage", promptPageLeaveMessage)

        
    def rules(self, rules):
        # 组合校验规则，选填
        
        return self.set("rules", rules)

        
    def preventEnterSubmit(self, preventEnterSubmit):
        # 禁用回车提交
        
        return self.set("preventEnterSubmit", preventEnterSubmit)

        
    def labelAlign(self, labelAlign):
        # 表单label的对齐方式
        
        return self.set("labelAlign", labelAlign)

        
    def labelWidth(self, labelWidth):
        # label自定义宽度，默认单位为px
        
        return self.set("labelWidth", labelWidth)

        