
from amis.AmisComponent import AmisComponent

class FileControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "file-control")
        
    
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
        # 指定为文件上传
        
        return self.set("type", type)

        
    def btnLabel(self, btnLabel):
        # 上传文件按钮说明
        
        return self.set("btnLabel", btnLabel)

        
    def accept(self, accept):
        # 默认只支持纯文本，要支持其他类型，请配置此属性。建议直接填写文件后缀 如：.txt,.csv  多个类型用逗号隔开。
        
        return self.set("accept", accept)

        
    def capture(self, capture):
        # 控制 input 标签的 capture 属性，用于移动端拍照或录像。
        
        return self.set("capture", capture)

        
    def asBase64(self, asBase64):
        # 如果上传的文件比较小可以设置此选项来简单的把文件 base64 的值给 form 一起提交，目前不支持多选。
        
        return self.set("asBase64", asBase64)

        
    def asBlob(self, asBlob):
        # 如果不希望 File 组件上传，可以配置 `asBlob` 或者 `asBase64`，采用这种方式后，组件不再自己上传了，而是直接把文件数据作为表单项的值，文件内容会在 Form 表单提交的接口里面一起带上。
        
        return self.set("asBlob", asBlob)

        
    def autoUpload(self, autoUpload):
        # 是否自动开始上传
        
        return self.set("autoUpload", autoUpload)

        
    def chunkApi(self, chunkApi):
        # 默认 `/api/upload/chunk` 想自己存储时才需要关注。
        
        return self.set("chunkApi", chunkApi)

        
    def chunkSize(self, chunkSize):
        # 分块大小，默认为 5M.
        
        return self.set("chunkSize", chunkSize)

        
    def concurrency(self, concurrency):
        # 分块上传的并发数
        
        return self.set("concurrency", concurrency)

        
    def delimiter(self, delimiter):
        # 分割符
        
        return self.set("delimiter", delimiter)

        
    def downloadUrl(self, downloadUrl):
        # 默认显示文件路径的时候会支持直接下载， 可以支持加前缀如：`http://xx.dom/filename=` ， 如果不希望这样，可以把当前配置项设置为 `false`。  1.1.6 版本开始将支持变量 ${xxx} 来自己拼凑个下载地址，并且支持配置成 post.
        
        return self.set("downloadUrl", downloadUrl)

        
    def templateUrl(self, templateUrl):
        # 模板下载地址
        
        return self.set("templateUrl", templateUrl)

        
    def fileField(self, fileField):
        # 默认 `file`, 如果你不想自己存储，则可以忽略此属性。
        
        return self.set("fileField", fileField)

        
    def finishChunkApi(self, finishChunkApi):
        # 默认 `/api/upload/finishChunkApi` 想自己存储时才需要关注。
        
        return self.set("finishChunkApi", finishChunkApi)

        
    def hideUploadButton(self, hideUploadButton):
        # 是否隐藏上传按钮
        
        return self.set("hideUploadButton", hideUploadButton)

        
    def maxLength(self, maxLength):
        # 最多的个数
        
        return self.set("maxLength", maxLength)

        
    def maxSize(self, maxSize):
        # 默认没有限制，当设置后，文件大小大于此值将不允许上传。
        
        return self.set("maxSize", maxSize)

        
    def receiver(self, receiver):
        # 默认 `/api/upload/file` 如果想自己存储，请设置此选项。
        
        return self.set("receiver", receiver)

        
    def startChunkApi(self, startChunkApi):
        # 默认 `/api/upload/startChunk` 想自己存储时才需要关注。
        
        return self.set("startChunkApi", startChunkApi)

        
    def useChunk(self, useChunk):
        # 默认为 'auto' amis 所在服务器，限制了文件上传大小不得超出10M，所以 amis 在用户选择大文件的时候，自动会改成分块上传模式。
        
        return self.set("useChunk", useChunk)

        
    def btnClassName(self, btnClassName):
        # 按钮 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnClassName", btnClassName)

        
    def btnUploadClassName(self, btnUploadClassName):
        # 上传按钮 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("btnUploadClassName", btnUploadClassName)

        
    def multiple(self, multiple):
        # 是否为多选
        
        return self.set("multiple", multiple)

        
    def joinValues(self, joinValues):
        # 1. 单选模式：当用户选中某个选项时，选项中的 value 将被作为该表单项的值提交， 否则，整个选项对象都会作为该表单项的值提交。 2. 多选模式：选中的多个选项的 `value` 会通过 `delimiter` 连接起来， 否则直接将以数组的形式提交值。
        
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # 开启后将选中的选项 value 的值封装为数组，作为当前表单项的值。
        
        return self.set("extractValue", extractValue)

        
    def resetValue(self, resetValue):
        # 清除时设置的值
        
        return self.set("resetValue", resetValue)

        
    def valueField(self, valueField):
        # 接口返回的数据中，哪个用来当做值
        
        return self.set("valueField", valueField)

        
    def nameField(self, nameField):
        # 接口返回的数据中，哪个用来展示文件名
        
        return self.set("nameField", nameField)

        
    def urlField(self, urlField):
        # 接口返回的数据中哪个用来作为下载地址。
        
        return self.set("urlField", urlField)

        
    def stateTextMap(self, stateTextMap):
        # 按钮状态文案配置。
        
        return self.set("stateTextMap", stateTextMap)

        
    def documentation(self, documentation):
        # 说明文档内容配置
        
        return self.set("documentation", documentation)

        
    def documentLink(self, documentLink):
        # 说明文档链接配置
        
        return self.set("documentLink", documentLink)

        
    def drag(self, drag):
        # 是否为拖拽上传
        
        return self.set("drag", drag)

        