
from amis.AmisComponent import AmisComponent

class ImageControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "image-control")
        
    
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

        
    def size(self, size):
        # 表单项大小# 可选项: ['xs', 'sm', 'md', 'lg', 'full']
        
        return self.set("size", size)

        
    def label(self, label):
        # 描述标题
        
        return self.set("label", label)

        
    def labelAlign(self, labelAlign):
        # 描述标题
        
        return self.set("labelAlign", labelAlign)

        
    def labelWidth(self, labelWidth):
        # label自定义宽度，默认单位为px
        
        return self.set("labelWidth", labelWidth)

        
    def labelClassName(self, labelClassName):
        # 配置 label className
        
        return self.set("labelClassName", labelClassName)

        
    def name(self, name):
        # 字段名，表单提交时的 key，支持多层级，用.连接，如： a.b.c
        
        return self.set("name", name)

        
    def extraName(self, extraName):
        # 额外的字段名，当为范围组件时可以用来将另外一个值打平出来
        
        return self.set("extraName", extraName)

        
    def remark(self, remark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容
        
        return self.set("remark", remark)

        
    def labelRemark(self, labelRemark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容, 这个小图标跟 label 在一起
        
        return self.set("labelRemark", labelRemark)

        
    def hint(self, hint):
        # 输入提示，聚焦的时候显示
        
        return self.set("hint", hint)

        
    def submitOnChange(self, submitOnChange):
        # 当修改完的时候是否提交表单。
        
        return self.set("submitOnChange", submitOnChange)

        
    def readOnly(self, readOnly):
        # 是否只读
        
        return self.set("readOnly", readOnly)

        
    def readOnlyOn(self, readOnlyOn):
        # 只读条件
        
        return self.set("readOnlyOn", readOnlyOn)

        
    def validateOnChange(self, validateOnChange):
        # 不设置时，当表单提交过后表单项每次修改都会触发重新验证， 如果设置了，则由此配置项来决定要不要每次修改都触发验证。
        
        return self.set("validateOnChange", validateOnChange)

        
    def description(self, description):
        # 描述内容，支持 Html 片段。
        
        return self.set("description", description)

        
    def desc(self, desc):
        
        
        return self.set("desc", desc)

        
    def descriptionClassName(self, descriptionClassName):
        # 配置描述上的 className
        
        return self.set("descriptionClassName", descriptionClassName)

        
    def mode(self, mode):
        # 配置当前表单项展示模式# 可选项: ['normal', 'inline', 'horizontal']
        
        return self.set("mode", mode)

        
    def horizontal(self, horizontal):
        # 当配置为水平布局的时候，用来配置具体的左右分配。
        
        return self.set("horizontal", horizontal)

        
    def inline(self, inline):
        # 表单 control 是否为 inline 模式。
        
        return self.set("inline", inline)

        
    def inputClassName(self, inputClassName):
        # 配置 input className
        
        return self.set("inputClassName", inputClassName)

        
    def placeholder(self, placeholder):
        # 占位符
        
        return self.set("placeholder", placeholder)

        
    def required(self, required):
        # 是否为必填
        
        return self.set("required", required)

        
    def validationErrors(self, validationErrors):
        # 验证失败的提示信息
        
        return self.set("validationErrors", validationErrors)

        
    def validations(self, validations):
        
        
        return self.set("validations", validations)

        
    def value(self, value):
        # 默认值，切记只能是静态值，不支持取变量，跟数据关联是通过设置 name 属性来实现的。
        
        return self.set("value", value)

        
    def clearValueOnHidden(self, clearValueOnHidden):
        # 表单项隐藏时，是否在当前 Form 中删除掉该表单项值。注意同名的未隐藏的表单项值也会删掉
        
        return self.set("clearValueOnHidden", clearValueOnHidden)

        
    def validateApi(self, validateApi):
        # 远端校验表单项接口
        
        return self.set("validateApi", validateApi)

        
    def autoFill(self, autoFill):
        # 上传后把其他字段同步到表单内部。
        
        return self.set("autoFill", autoFill)

        
    def initAutoFill(self, initAutoFill):
        # 初始化时是否把其他字段同步到表单内部。
        
        return self.set("initAutoFill", initAutoFill)

        
    def row(self, row):
        
        
        return self.set("row", row)

        
    def type(self, type):
        # 指定为图片上传控件
        
        return self.set("type", type)

        
    def src(self, src):
        # 默认展示图片的链接
        
        return self.set("src", src)

        
    def imageClassName(self, imageClassName):
        # 默认展示图片的类名
        
        return self.set("imageClassName", imageClassName)

        
    def accept(self, accept):
        # 配置接收的图片类型  建议直接填写文件后缀 如：.txt,.csv  多个类型用逗号隔开。
        
        return self.set("accept", accept)

        
    def allowInput(self, allowInput):
        # 默认都是通过用户选择图片后上传返回图片地址，如果开启此选项，则可以允许用户图片地址。
        
        return self.set("allowInput", allowInput)

        
    def autoUpload(self, autoUpload):
        # 是否自动开始上传
        
        return self.set("autoUpload", autoUpload)

        
    def uploadBtnText(self, uploadBtnText):
        # 上传按钮文案
        
        return self.set("uploadBtnText", uploadBtnText)

        
    def btnClassName(self, btnClassName):
        # 选择图片按钮的 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnClassName", btnClassName)

        
    def btnUploadClassName(self, btnUploadClassName):
        # 上传按钮的 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnUploadClassName", btnUploadClassName)

        
    def compress(self, compress):
        
        
        return self.set("compress", compress)

        
    def compressOptions(self, compressOptions):
        
        
        return self.set("compressOptions", compressOptions)

        
    def crop(self, crop):
        
        
        return self.set("crop", crop)

        
    def cropFormat(self, cropFormat):
        # 裁剪后的图片类型
        
        return self.set("cropFormat", cropFormat)

        
    def cropQuality(self, cropQuality):
        # 裁剪后的质量
        
        return self.set("cropQuality", cropQuality)

        
    def reCropable(self, reCropable):
        # 是否允许二次裁剪。
        
        return self.set("reCropable", reCropable)

        
    def hideUploadButton(self, hideUploadButton):
        # 是否隐藏上传按钮
        
        return self.set("hideUploadButton", hideUploadButton)

        
    def limit(self, limit):
        # 限制图片大小，超出不让上传。
        
        return self.set("limit", limit)

        
    def maxLength(self, maxLength):
        # 最多的个数
        
        return self.set("maxLength", maxLength)

        
    def maxSize(self, maxSize):
        # 默认没有限制，当设置后，文件大小大于此值将不允许上传。
        
        return self.set("maxSize", maxSize)

        
    def receiver(self, receiver):
        # 默认 `/api/upload` 如果想自己存储，请设置此选项。
        
        return self.set("receiver", receiver)

        
    def showCompressOptions(self, showCompressOptions):
        # 默认为 false, 开启后，允许用户输入压缩选项。
        
        return self.set("showCompressOptions", showCompressOptions)

        
    def multiple(self, multiple):
        # 是否为多选
        
        return self.set("multiple", multiple)

        
    def capture(self, capture):
        # 可配置移动端的拍照功能，比如配置 `camera` 移动端只能拍照，等
        
        return self.set("capture", capture)

        
    def joinValues(self, joinValues):
        # 单选模式：当用户选中某个选项时，选项中的 value 将被作为该表单项的值提交，否则，整个选项对象都会作为该表单项的值提交。 多选模式：选中的多个选项的 `value` 会通过 `delimiter` 连接起来，否则直接将以数组的形式提交值。
        
        return self.set("joinValues", joinValues)

        
    def delimiter(self, delimiter):
        # 分割符
        
        return self.set("delimiter", delimiter)

        
    def extractValue(self, extractValue):
        # 开启后将选中的选项 value 的值封装为数组，作为当前表单项的值。
        
        return self.set("extractValue", extractValue)

        
    def resetValue(self, resetValue):
        # 清除时设置的值
        
        return self.set("resetValue", resetValue)

        
    def thumbMode(self, thumbMode):
        # 缩路图展示模式# 可选项: ['w-full', 'h-full', 'contain', 'cover']
        
        return self.set("thumbMode", thumbMode)

        
    def thumbRatio(self, thumbRatio):
        # 缩路图展示比率。# 可选项: ['1:1', '4:3', '16:9']
        
        return self.set("thumbRatio", thumbRatio)

        
    def initCrop(self, initCrop):
        # 初始化时是否打开裁剪模式
        
        return self.set("initCrop", initCrop)

        
    def dropCrop(self, dropCrop):
        # 图片上传完毕是否进入裁剪模式
        
        return self.set("dropCrop", dropCrop)

        
    def frameImage(self, frameImage):
        # 默认占位图图片地址
        
        return self.set("frameImage", frameImage)

        
    def fixedSize(self, fixedSize):
        # 是否开启固定尺寸
        
        return self.set("fixedSize", fixedSize)

        
    def fixedSizeClassName(self, fixedSizeClassName):
        # 固定尺寸的 CSS类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("fixedSizeClassName", fixedSizeClassName)

        
    def draggable(self, draggable):
        # 是否可拖拽排序
        
        return self.set("draggable", draggable)

        
    def draggableTip(self, draggableTip):
        # 可拖拽排序的提示信息。
        
        return self.set("draggableTip", draggableTip)

        