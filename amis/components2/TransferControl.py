
from amis.AmisComponent import AmisComponent

class TransferControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "transfer-control")
        
    
    def loadingConfig(self, loadingConfig):
        
        
        return self.set("loadingConfig", loadingConfig)

        
    def options(self, options):
        # 选项集合
        
        return self.set("options", options)

        
    def source(self, source):
        # 可用来通过 API 拉取 options。
        
        return self.set("source", source)

        
    def selectFirst(self, selectFirst):
        # 默认选择选项第一个值。
        
        return self.set("selectFirst", selectFirst)

        
    def initFetchOn(self, initFetchOn):
        # 用表达式来配置 source 接口初始要不要拉取
        
        return self.set("initFetchOn", initFetchOn)

        
    def initFetch(self, initFetch):
        # 配置 source 接口初始拉不拉取。
        
        return self.set("initFetch", initFetch)

        
    def multiple(self, multiple):
        # 是否为多选模式
        
        return self.set("multiple", multiple)

        
    def joinValues(self, joinValues):
        # 单选模式：当用户选中某个选项时，选项中的 value 将被作为该表单项的值提交，否则，整个选项对象都会作为该表单项的值提交。 多选模式：选中的多个选项的 `value` 会通过 `delimiter` 连接起来，否则直接将以数组的形式提交值。
        
        return self.set("joinValues", joinValues)

        
    def delimiter(self, delimiter):
        # 分割符
        
        return self.set("delimiter", delimiter)

        
    def valuesNoWrap(self, valuesNoWrap):
        # 多选模式，值太多时是否避免折行
        
        return self.set("valuesNoWrap", valuesNoWrap)

        
    def extractValue(self, extractValue):
        # 开启后将选中的选项 value 的值封装为数组，作为当前表单项的值。
        
        return self.set("extractValue", extractValue)

        
    def clearable(self, clearable):
        # 是否可清除。
        
        return self.set("clearable", clearable)

        
    def resetValue(self, resetValue):
        # 点清除按钮时，将表单项设置成当前配置的值。
        
        return self.set("resetValue", resetValue)

        
    def deferField(self, deferField):
        # 懒加载字段
        
        return self.set("deferField", deferField)

        
    def deferApi(self, deferApi):
        # 延时加载的 API，当选项中有 defer: true 的选项时，点开会通过此接口扩充。
        
        return self.set("deferApi", deferApi)

        
    def addApi(self, addApi):
        # 添加时调用的接口
        
        return self.set("addApi", addApi)

        
    def addControls(self, addControls):
        # 新增时的表单项。
        
        return self.set("addControls", addControls)

        
    def addDialog(self, addDialog):
        # 控制新增弹框设置项
        
        return self.set("addDialog", addDialog)

        
    def creatable(self, creatable):
        # 是否可以新增
        
        return self.set("creatable", creatable)

        
    def createBtnLabel(self, createBtnLabel):
        # 新增文字
        
        return self.set("createBtnLabel", createBtnLabel)

        
    def editable(self, editable):
        # 是否可以编辑
        
        return self.set("editable", editable)

        
    def editApi(self, editApi):
        # 编辑时调用的 API
        
        return self.set("editApi", editApi)

        
    def editControls(self, editControls):
        # 选项修改的表单项
        
        return self.set("editControls", editControls)

        
    def editDialog(self, editDialog):
        # 控制编辑弹框设置项
        
        return self.set("editDialog", editDialog)

        
    def removable(self, removable):
        # 是否可删除
        
        return self.set("removable", removable)

        
    def deleteApi(self, deleteApi):
        # 选项删除 API
        
        return self.set("deleteApi", deleteApi)

        
    def deleteConfirmText(self, deleteConfirmText):
        # 选项删除提示文字。
        
        return self.set("deleteConfirmText", deleteConfirmText)

        
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

        
    def testIdBuilder(self, testIdBuilder):
        
        
        return self.set("testIdBuilder", testIdBuilder)

        
    def remark(self, remark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容
        
        return self.set("remark", remark)

        
    def labelRemark(self, labelRemark):
        # 显示一个小图标, 鼠标放上去的时候显示提示内容, 这个小图标跟 label 在一起
        
        return self.set("labelRemark", labelRemark)

        
    def type(self, type):
        # 表单项类型
        
        return self.set("type", type)

        
    def showArrow(self, showArrow):
        # 是否显示剪头
        
        return self.set("showArrow", showArrow)

        
    def sortable(self, sortable):
        # 可排序？
        
        return self.set("sortable", sortable)

        
    def selectMode(self, selectMode):
        # 勾选展示模式# 可选项: ['table', 'list', 'tree', 'chained', 'associated']
        
        return self.set("selectMode", selectMode)

        
    def resultListModeFollowSelect(self, resultListModeFollowSelect):
        # 结果面板是否追踪显示
        
        return self.set("resultListModeFollowSelect", resultListModeFollowSelect)

        
    def leftOptions(self, leftOptions):
        # 当 selectMode 为 associated 时用来定义左侧的选项
        
        return self.set("leftOptions", leftOptions)

        
    def leftMode(self, leftMode):
        # 当 selectMode 为 associated 时用来定义左侧的选择模式# 可选项: ['tree', 'list']
        
        return self.set("leftMode", leftMode)

        
    def rightMode(self, rightMode):
        # 当 selectMode 为 associated 时用来定义右侧的选择模式# 可选项: ['table', 'list', 'tree', 'chained']
        
        return self.set("rightMode", rightMode)

        
    def searchResultMode(self, searchResultMode):
        # 搜索结果展示模式# 可选项: ['table', 'list', 'tree', 'chained']
        
        return self.set("searchResultMode", searchResultMode)

        
    def columns(self, columns):
        # 当 selectMode 为 table 时定义表格列信息。
        
        return self.set("columns", columns)

        
    def searchResultColumns(self, searchResultColumns):
        # 当 searchResultMode 为 table 时定义表格列信息。
        
        return self.set("searchResultColumns", searchResultColumns)

        
    def searchable(self, searchable):
        # 可搜索？
        
        return self.set("searchable", searchable)

        
    def resultSearchable(self, resultSearchable):
        # 结果（右则）列表的检索功能，当设置为true时，可以通过输入检索模糊匹配检索内容
        
        return self.set("resultSearchable", resultSearchable)

        
    def searchApi(self, searchApi):
        # 搜索 API
        
        return self.set("searchApi", searchApi)

        
    def selectTitle(self, selectTitle):
        # 左侧的标题文字
        
        return self.set("selectTitle", selectTitle)

        
    def resultTitle(self, resultTitle):
        # 右侧结果的标题文字
        
        return self.set("resultTitle", resultTitle)

        
    def menuTpl(self, menuTpl):
        # 用来丰富选项展示
        
        return self.set("menuTpl", menuTpl)

        
    def valueTpl(self, valueTpl):
        # 用来丰富值的展示
        
        return self.set("valueTpl", valueTpl)

        
    def searchPlaceholder(self, searchPlaceholder):
        # 左侧列表搜索框提示
        
        return self.set("searchPlaceholder", searchPlaceholder)

        
    def resultSearchPlaceholder(self, resultSearchPlaceholder):
        # 右侧列表搜索框提示
        
        return self.set("resultSearchPlaceholder", resultSearchPlaceholder)

        
    def statistics(self, statistics):
        # 统计数字
        
        return self.set("statistics", statistics)

        
    def itemHeight(self, itemHeight):
        # 单个选项的高度，主要用于虚拟渲染
        
        return self.set("itemHeight", itemHeight)

        
    def virtualThreshold(self, virtualThreshold):
        # 在选项数量达到多少时开启虚拟渲染
        
        return self.set("virtualThreshold", virtualThreshold)

        
    def showInvalidMatch(self, showInvalidMatch):
        # 当在value值未匹配到当前options中的选项时，是否value值对应文本飘红显示
        
        return self.set("showInvalidMatch", showInvalidMatch)

        
    def onlyChildren(self, onlyChildren):
        # 树形模式下，仅选中子节点
        
        return self.set("onlyChildren", onlyChildren)

        
    def initiallyOpen(self, initiallyOpen):
        # 是否默认都展开
        
        return self.set("initiallyOpen", initiallyOpen)

        
    def autoCheckChildren(self, autoCheckChildren):
        # ui级联关系，true代表级联选中，false代表不级联，默认为true
        
        return self.set("autoCheckChildren", autoCheckChildren)

        
    def pagination(self, pagination):
        # 分页配置，selectMode为默认和table才会生效
        
        return self.set("pagination", pagination)

        