
from amis.AmisComponent import AmisComponent

class Images(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "images")
        
    
    def className(self, className):
        # 外层 CSS 类名
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
        # 指定为图片集渲染器# 可选项: ['images', 'static-images']
        
        return self.set("type", type)

        
    def testid(self, testid):
        
        
        return self.set("testid", testid)

        
    def defaultImage(self, defaultImage):
        # 默认图片地址
        
        return self.set("defaultImage", defaultImage)

        
    def placeholder(self, placeholder):
        # 列表为空时显示
        
        return self.set("placeholder", placeholder)

        
    def delimiter(self, delimiter):
        # 配置值的连接符
        
        return self.set("delimiter", delimiter)

        
    def thumbMode(self, thumbMode):
        # 预览图模式# 可选项: ['w-full', 'h-full', 'contain', 'cover']
        
        return self.set("thumbMode", thumbMode)

        
    def thumbRatio(self, thumbRatio):
        # 预览图比率# 可选项: ['1:1', '4:3', '16:9']
        
        return self.set("thumbRatio", thumbRatio)

        
    def name(self, name):
        # 关联字段名，也可以直接配置 src
        
        return self.set("name", name)

        
    def value(self, value):
        
        
        return self.set("value", value)

        
    def source(self, source):
        
        
        return self.set("source", source)

        
    def options(self, options):
        
        
        return self.set("options", options)

        
    def src(self, src):
        # 图片地址，默认读取数据中的 image 属性，如果不是请配置 ,如  ${imageUrl}
        
        return self.set("src", src)

        
    def originalSrc(self, originalSrc):
        # 大图地址，不设置用 src 属性，如果不是请配置，如：${imageOriginUrl}
        
        return self.set("originalSrc", originalSrc)

        
    def enlargeAble(self, enlargeAble):
        # 是否启动放大功能。
        
        return self.set("enlargeAble", enlargeAble)

        
    def enlargetWithImages(self, enlargetWithImages):
        # 放大时是否显示图片集
        
        return self.set("enlargetWithImages", enlargetWithImages)

        
    def showDimensions(self, showDimensions):
        # 是否显示尺寸。
        
        return self.set("showDimensions", showDimensions)

        
    def listClassName(self, listClassName):
        # 列表 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("listClassName", listClassName)

        
    def imageGallaryClassName(self, imageGallaryClassName):
        # 放大详情图 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("imageGallaryClassName", imageGallaryClassName)

        
    def showToolbar(self, showToolbar):
        # 是否展示图片工具栏
        
        return self.set("showToolbar", showToolbar)

        
    def toolbarActions(self, toolbarActions):
        # 工具栏配置
        
        return self.set("toolbarActions", toolbarActions)

        