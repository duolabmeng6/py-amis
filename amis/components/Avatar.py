
from amis.AmisComponent import AmisComponent

class Avatar(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "avatar")
        
    
    def className(self, className):
        # 类名
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
        
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def badge(self, badge):
        # 角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("badge", badge)

        
    def src(self, src):
        # 图片地址
        
        return self.set("src", src)

        
    def defaultAvatar(self, defaultAvatar):
        # 默认头像
        
        return self.set("defaultAvatar", defaultAvatar)

        
    def icon(self, icon):
        # 图标
        
        return self.set("icon", icon)

        
    def fit(self, fit):
        # 图片相对于容器的缩放方式# 可选项: ['fill', 'contain', 'cover', 'none', 'scale-down']
        
        return self.set("fit", fit)

        
    def shape(self, shape):
        # 形状# 可选项: ['circle', 'square', 'rounded']
        
        return self.set("shape", shape)

        
    def size(self, size):
        # 大小
        
        return self.set("size", size)

        
    def text(self, text):
        # 文本
        
        return self.set("text", text)

        
    def gap(self, gap):
        # 字符类型距离左右两侧边界单位像素
        
        return self.set("gap", gap)

        
    def alt(self, alt):
        # 图片无法显示时的替换文字地址
        
        return self.set("alt", alt)

        
    def draggable(self, draggable):
        # 图片是否允许拖动
        
        return self.set("draggable", draggable)

        
    def crossOrigin(self, crossOrigin):
        # 图片CORS属性# 可选项: ['anonymous', 'use-credentials', '']
        
        return self.set("crossOrigin", crossOrigin)

        
    def onError(self, onError):
        # 图片加载失败的是否默认处理，字符串函数
        
        return self.set("onError", onError)

        