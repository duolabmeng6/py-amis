
from amis.AmisComponent import AmisComponent

class Progress(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "progress")
        
    
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
        
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def name(self, name):
        # 关联字段名
        
        return self.set("name", name)

        
    def value(self, value):
        # 进度值
        
        return self.set("value", value)

        
    def mode(self, mode):
        # 进度条类型# 可选项: ['line', 'circle', 'dashboard']
        
        return self.set("mode", mode)

        
    def progressClassName(self, progressClassName):
        # 进度条 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("progressClassName", progressClassName)

        
    def map(self, map):
        # 配置不同的值段，用不同的样式提示用户
        
        return self.set("map", map)

        
    def showLabel(self, showLabel):
        # 是否显示值
        
        return self.set("showLabel", showLabel)

        
    def placeholder(self, placeholder):
        # 占位符
        
        return self.set("placeholder", placeholder)

        
    def stripe(self, stripe):
        # 是否显示背景间隔
        
        return self.set("stripe", stripe)

        
    def animate(self, animate):
        # 是否显示动画（只有在开启的时候才能看出来）
        
        return self.set("animate", animate)

        
    def strokeWidth(self, strokeWidth):
        # 进度条线的宽度
        
        return self.set("strokeWidth", strokeWidth)

        
    def gapDegree(self, gapDegree):
        # 仪表盘进度条缺口角度，可取值 0 ~ 295
        
        return self.set("gapDegree", gapDegree)

        
    def gapPosition(self, gapPosition):
        # 仪表盘进度条缺口位置# 可选项: ['top', 'bottom', 'left', 'right']
        
        return self.set("gapPosition", gapPosition)

        
    def valueTpl(self, valueTpl):
        # 内容的模板函数
        
        return self.set("valueTpl", valueTpl)

        
    def threshold(self, threshold):
        # 阈值
        
        return self.set("threshold", threshold)

        
    def showThresholdText(self, showThresholdText):
        # 是否显示阈值数值
        
        return self.set("showThresholdText", showThresholdText)

        