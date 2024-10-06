
from amis.AmisComponent import AmisComponent

class ArrayControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "array-control")
        
    
    def scaffold(self, scaffold):
        # 新增成员时的默认值
        
        return self.set("scaffold", scaffold)

        
    def noBorder(self, noBorder):
        # 是否含有边框
        
        return self.set("noBorder", noBorder)

        
    def deleteConfirmText(self, deleteConfirmText):
        # 确认删除时的提示
        
        return self.set("deleteConfirmText", deleteConfirmText)

        
    def deleteApi(self, deleteApi):
        # 删除时调用的api
        
        return self.set("deleteApi", deleteApi)

        
    def typeSwitchable(self, typeSwitchable):
        # 是否可切换条件，配合`conditions`使用
        
        return self.set("typeSwitchable", typeSwitchable)

        
    def formClassName(self, formClassName):
        # 内部单组表单项的类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("formClassName", formClassName)

        
    def addButtonClassName(self, addButtonClassName):
        # 新增按钮CSS类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("addButtonClassName", addButtonClassName)

        
    def addButtonText(self, addButtonText):
        # 新增按钮文字
        
        return self.set("addButtonText", addButtonText)

        
    def addable(self, addable):
        # 是否可新增
        
        return self.set("addable", addable)

        
    def addattop(self, addattop):
        # Add at top
        
        return self.set("addattop", addattop)

        
    def draggable(self, draggable):
        # 是否可拖拽排序
        
        return self.set("draggable", draggable)

        
    def draggableTip(self, draggableTip):
        # 可拖拽排序的提示信息。
        
        return self.set("draggableTip", draggableTip)

        
    def flat(self, flat):
        # 是否将结果扁平化(去掉name),只有当controls的length为1且multiple为true的时候才有效
        
        return self.set("flat", flat)

        
    def delimiter(self, delimiter):
        # 当扁平化开启并且joinValues为true时，用什么分隔符
        
        return self.set("delimiter", delimiter)

        
    def joinValues(self, joinValues):
        # 当扁平化开启的时候，是否用分隔符的形式发送给后端，否则采用array的方式
        
        return self.set("joinValues", joinValues)

        
    def maxLength(self, maxLength):
        # 限制最大个数
        
        return self.set("maxLength", maxLength)

        
    def minLength(self, minLength):
        # 限制最小个数
        
        return self.set("minLength", minLength)

        
    def multiLine(self, multiLine):
        # 是否多行模式，默认一行展示完
        
        return self.set("multiLine", multiLine)

        
    def multiple(self, multiple):
        # 是否可多选
        
        return self.set("multiple", multiple)

        
    def removable(self, removable):
        # 是否可删除
        
        return self.set("removable", removable)

        
    def subFormMode(self, subFormMode):
        # 子表单的模式。# 可选项: ['normal', 'horizontal', 'inline']
        
        return self.set("subFormMode", subFormMode)

        
    def subFormHorizontal(self, subFormHorizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("subFormHorizontal", subFormHorizontal)

        
    def placeholder(self, placeholder):
        # 没有成员时显示。
        
        return self.set("placeholder", placeholder)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 是否可以访问父级数据，正常 combo 已经关联到数组成员，是不能访问父级数据的。
        
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def tabsMode(self, tabsMode):
        # 采用 Tabs 展示方式？
        
        return self.set("tabsMode", tabsMode)

        
    def tabsStyle(self, tabsStyle):
        # Tabs 的展示模式。# 可选项: ['', 'line', 'card', 'radio']
        
        return self.set("tabsStyle", tabsStyle)

        
    def tabsLabelTpl(self, tabsLabelTpl):
        # 选项卡标题的生成模板。
        # 支持两种语法，但是不能混着用。分别是：  1. `${xxx}` 或者 `${xxx|upperCase}` 2. `<%= data.xxx %>`   更多文档：https://aisuda.bce.baidu.com/amis/zh-CN/docs/concepts/template
        return self.set("tabsLabelTpl", tabsLabelTpl)

        
    def lazyLoad(self, lazyLoad):
        # 数据比较多，比较卡时，可以试试开启。
        
        return self.set("lazyLoad", lazyLoad)

        
    def strictMode(self, strictMode):
        # 严格模式，为了性能默认不开的。
        
        return self.set("strictMode", strictMode)

        
    def syncFields(self, syncFields):
        # 配置同步字段。只有 `strictMode` 为 `false` 时有效。 如果 Combo 层级比较深，底层的获取外层的数据可能不同步。 但是给 combo 配置这个属性就能同步下来。输入格式：`["os"]`
        
        return self.set("syncFields", syncFields)

        
    def nullable(self, nullable):
        # 允许为空，如果子表单项里面配置验证器，且又是单条模式。可以允许用户选择清空（不填）。
        
        return self.set("nullable", nullable)

        
    def messages(self, messages):
        # 提示信息
        
        return self.set("messages", messages)

        
    def updatePristineAfterStoreDataReInit(self, updatePristineAfterStoreDataReInit):
        
        
        return self.set("updatePristineAfterStoreDataReInit", updatePristineAfterStoreDataReInit)

        
    def testIdBuilder(self, testIdBuilder):
        
        
        return self.set("testIdBuilder", testIdBuilder)

        
    def remark(self, remark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容
        
        return self.set("remark", remark)

        
    def labelRemark(self, labelRemark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容, 这个小图标跟 label 在一起
        
        return self.set("labelRemark", labelRemark)

        
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
        # 自动填充，当选项被选择的时候，将选项中的其他值同步设置到表单内。
        
        return self.set("autoFill", autoFill)

        
    def initAutoFill(self, initAutoFill):
        
        
        return self.set("initAutoFill", initAutoFill)

        
    def row(self, row):
        
        
        return self.set("row", row)

        
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

        
    def type(self, type):
        # 指定为数组输入框类型
        
        return self.set("type", type)

        
    def items(self, items):
        # 成员渲染器配置
        
        return self.set("items", items)

        