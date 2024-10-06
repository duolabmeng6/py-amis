
from amis.AmisComponent import AmisComponent

class Wizard(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "wizard")
        
    
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
        # 指定为表单向导
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def actionClassName(self, actionClassName):
        # 配置按钮 className
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("actionClassName", actionClassName)

        
    def actionFinishLabel(self, actionFinishLabel):
        # 完成按钮的文字描述
        
        return self.set("actionFinishLabel", actionFinishLabel)

        
    def actionNextLabel(self, actionNextLabel):
        # 下一步按钮的文字描述
        
        return self.set("actionNextLabel", actionNextLabel)

        
    def actionNextSaveLabel(self, actionNextSaveLabel):
        # 下一步并且保存按钮的文字描述
        
        return self.set("actionNextSaveLabel", actionNextSaveLabel)

        
    def actionPrevLabel(self, actionPrevLabel):
        # 上一步按钮的文字描述
        
        return self.set("actionPrevLabel", actionPrevLabel)

        
    def api(self, api):
        # Wizard 用来保存数据的 api。 [详情](https://baidu.github.io/amis/docs/api#wizard)
        
        return self.set("api", api)

        
    def bulkSubmit(self, bulkSubmit):
        # 是否合并后再提交
        
        return self.set("bulkSubmit", bulkSubmit)

        
    def initApi(self, initApi):
        # Wizard 用来获取初始数据的 api。
        
        return self.set("initApi", initApi)

        
    def mode(self, mode):
        # 展示模式# 可选项: ['vertical', 'horizontal']
        
        return self.set("mode", mode)

        
    def name(self, name):
        
        # 组件名字，这个名字可以用来定位，用于组件通信
        return self.set("name", name)

        
    def readOnly(self, readOnly):
        # 是否为只读模式。
        
        return self.set("readOnly", readOnly)

        
    def redirect(self, redirect):
        # 保存完后，可以指定跳转地址，支持相对路径和组内绝对路径，同时可以通过 $xxx 使用变量
        
        return self.set("redirect", redirect)

        
    def reload(self, reload):
        
        # 配置刷新动作，这个动作通常在完成渲染器本省的固定动作后出发。  一般用来配置目标组件的 name 属性。多个目标可以用逗号隔开。  当目标是 windows 时表示刷新整个页面。  刷新目标的同时还支持传递参数如： `foo?a=${a}&b=${b},boo?c=${c}`
        return self.set("reload", reload)

        
    def target(self, target):
        # 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 `CRUD` 模型的 name 值。 如果 target 目标是一个 `Form` ，则目标 `Form` 会重新触发 `initApi` 和 `schemaApi`，api 可以拿到当前 form 数据。如果目标是一个 `CRUD` 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。
        
        return self.set("target", target)

        
    def affixFooter(self, affixFooter):
        # 是否将底部按钮固定在底部。
        
        return self.set("affixFooter", affixFooter)

        
    def steps(self, steps):
        
        
        return self.set("steps", steps)

        
    def startStep(self, startStep):
        
        
        return self.set("startStep", startStep)

        
    def stepsClassName(self, stepsClassName):
        # 步骤条区域css类
        
        return self.set("stepsClassName", stepsClassName)

        
    def bodyClassName(self, bodyClassName):
        # 表单区域css类
        
        return self.set("bodyClassName", bodyClassName)

        
    def stepClassName(self, stepClassName):
        # step + body区域css类
        
        return self.set("stepClassName", stepClassName)

        
    def footerClassName(self, footerClassName):
        # 底部操作栏的css类
        
        return self.set("footerClassName", footerClassName)

        
    def wrapWithPanel(self, wrapWithPanel):
        # 是否用panel包裹
        
        return self.set("wrapWithPanel", wrapWithPanel)

        