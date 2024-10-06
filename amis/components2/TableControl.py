
from amis.AmisComponent import AmisComponent

class TableControl(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "table-control")
        
    
    def affixHeader(self, affixHeader):
        # 是否固定表头
        
        return self.set("affixHeader", affixHeader)

        
    def affixFooter(self, affixFooter):
        # 是否固底
        
        return self.set("affixFooter", affixFooter)

        
    def columns(self, columns):
        # 表格的列信息
        
        return self.set("columns", columns)

        
    def columnsTogglable(self, columnsTogglable):
        # 展示列显示开关，自动即：列数量大于或等于5个时自动开启
        
        return self.set("columnsTogglable", columnsTogglable)

        
    def footable(self, footable):
        # 是否开启底部展示功能，适合移动端展示
        
        return self.set("footable", footable)

        
    def footerClassName(self, footerClassName):
        # 底部外层 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("footerClassName", footerClassName)

        
    def headerClassName(self, headerClassName):
        # 顶部外层 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("headerClassName", headerClassName)

        
    def placeholder(self, placeholder):
        # 占位符
        
        return self.set("placeholder", placeholder)

        
    def showFooter(self, showFooter):
        # 是否显示底部
        
        return self.set("showFooter", showFooter)

        
    def showHeader(self, showHeader):
        # 是否显示头部
        
        return self.set("showHeader", showHeader)

        
    def source(self, source):
        # 数据源：绑定当前环境变量
        
        return self.set("source", source)

        
    def tableClassName(self, tableClassName):
        # 表格 CSS 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("tableClassName", tableClassName)

        
    def title(self, title):
        # 标题
        
        return self.set("title", title)

        
    def toolbarClassName(self, toolbarClassName):
        # 底部工具栏CSS样式类
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("toolbarClassName", toolbarClassName)

        
    def combineNum(self, combineNum):
        # 合并单元格配置，配置数字表示从左到右的多少列自动合并单元格。
        
        return self.set("combineNum", combineNum)

        
    def combineFromIndex(self, combineFromIndex):
        # 合并单元格配置，配置从第几列开始合并。
        
        return self.set("combineFromIndex", combineFromIndex)

        
    def prefixRow(self, prefixRow):
        # 顶部总结行
        
        return self.set("prefixRow", prefixRow)

        
    def affixRow(self, affixRow):
        # 底部总结行
        
        return self.set("affixRow", affixRow)

        
    def resizable(self, resizable):
        # 是否可调整列宽
        
        return self.set("resizable", resizable)

        
    def rowClassNameExpr(self, rowClassNameExpr):
        # 行样式表表达式
        
        return self.set("rowClassNameExpr", rowClassNameExpr)

        
    def itemBadge(self, itemBadge):
        # 行角标
        # Badge 角标。 文档：https://aisuda.bce.baidu.com/amis/zh-CN/components/badge
        return self.set("itemBadge", itemBadge)

        
    def autoGenerateFilter(self, autoGenerateFilter):
        # 开启查询区域，会根据列元素的searchable属性值，自动生成查询条件表单
        
        return self.set("autoGenerateFilter", autoGenerateFilter)

        
    def canAccessSuperData(self, canAccessSuperData):
        # 是否可以访问父级数据，正常 combo 已经关联到数组成员，是不能访问父级数据的。
        
        return self.set("canAccessSuperData", canAccessSuperData)

        
    def autoFillHeight(self, autoFillHeight):
        # 表格自动计算高度
        
        return self.set("autoFillHeight", autoFillHeight)

        
    def tableLayout(self, tableLayout):
        # table layout# 可选项: ['fixed', 'auto']
        
        return self.set("tableLayout", tableLayout)

        
    def deferApi(self, deferApi):
        # 懒加载 API，当行数据中用 defer: true 标记了，则其孩子节点将会用这个 API 来拉取数据。
        
        return self.set("deferApi", deferApi)

        
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

        
    def type(self, type):
        
        
        return self.set("type", type)

        
    def addable(self, addable):
        # 可新增
        
        return self.set("addable", addable)

        
    def childrenAddable(self, childrenAddable):
        # 是否可以新增子项
        
        return self.set("childrenAddable", childrenAddable)

        
    def copyable(self, copyable):
        # 可复制新增
        
        return self.set("copyable", copyable)

        
    def copyBtnLabel(self, copyBtnLabel):
        # 复制按钮文字
        
        return self.set("copyBtnLabel", copyBtnLabel)

        
    def copyBtnIcon(self, copyBtnIcon):
        # 复制按钮图标
        
        return self.set("copyBtnIcon", copyBtnIcon)

        
    def copyAddBtn(self, copyAddBtn):
        # 是否显示复制按钮
        
        return self.set("copyAddBtn", copyAddBtn)

        
    def copyData(self, copyData):
        # 复制的时候用来配置复制映射的数据。默认值是 {&:$$}，相当与复制整个行数据 通常有时候需要用来标记是复制过来的，也可能需要删掉一下主键字段。
        
        return self.set("copyData", copyData)

        
    def draggable(self, draggable):
        # 是否可以拖拽排序
        
        return self.set("draggable", draggable)

        
    def addApi(self, addApi):
        # 新增 API
        
        return self.set("addApi", addApi)

        
    def addBtnLabel(self, addBtnLabel):
        # 新增按钮文字
        
        return self.set("addBtnLabel", addBtnLabel)

        
    def addBtnIcon(self, addBtnIcon):
        # 新增按钮图标
        
        return self.set("addBtnIcon", addBtnIcon)

        
    def subAddBtnLabel(self, subAddBtnLabel):
        # 孩子新增按钮文字
        
        return self.set("subAddBtnLabel", subAddBtnLabel)

        
    def subAddBtnIcon(self, subAddBtnIcon):
        # 孩子新增按钮图标
        
        return self.set("subAddBtnIcon", subAddBtnIcon)

        
    def removable(self, removable):
        # 可否删除
        
        return self.set("removable", removable)

        
    def deleteApi(self, deleteApi):
        # 删除的 API
        
        return self.set("deleteApi", deleteApi)

        
    def editable(self, editable):
        # 可否编辑
        
        return self.set("editable", editable)

        
    def editBtnLabel(self, editBtnLabel):
        # 更新按钮名称
        
        return self.set("editBtnLabel", editBtnLabel)

        
    def editBtnIcon(self, editBtnIcon):
        # 更新按钮图标
        
        return self.set("editBtnIcon", editBtnIcon)

        
    def confirmBtnLabel(self, confirmBtnLabel):
        # 确认按钮文字
        
        return self.set("confirmBtnLabel", confirmBtnLabel)

        
    def confirmBtnIcon(self, confirmBtnIcon):
        # 确认按钮图标
        
        return self.set("confirmBtnIcon", confirmBtnIcon)

        
    def cancelBtnLabel(self, cancelBtnLabel):
        # 取消按钮文字
        
        return self.set("cancelBtnLabel", cancelBtnLabel)

        
    def cancelBtnIcon(self, cancelBtnIcon):
        # 取消按钮图标
        
        return self.set("cancelBtnIcon", cancelBtnIcon)

        
    def deleteBtnLabel(self, deleteBtnLabel):
        # 删除按钮文字
        
        return self.set("deleteBtnLabel", deleteBtnLabel)

        
    def deleteBtnIcon(self, deleteBtnIcon):
        # 删除按钮图标
        
        return self.set("deleteBtnIcon", deleteBtnIcon)

        
    def updateApi(self, updateApi):
        # 更新 API
        
        return self.set("updateApi", updateApi)

        
    def scaffold(self, scaffold):
        # 初始值，新增的时候
        
        return self.set("scaffold", scaffold)

        
    def deleteConfirmText(self, deleteConfirmText):
        # 删除确认文字
        
        return self.set("deleteConfirmText", deleteConfirmText)

        
    def valueField(self, valueField):
        # 值字段
        
        return self.set("valueField", valueField)

        
    def needConfirm(self, needConfirm):
        # 是否为确认的编辑模式。
        
        return self.set("needConfirm", needConfirm)

        
    def showIndex(self, showIndex):
        # 是否显示序号
        
        return self.set("showIndex", showIndex)

        
    def perPage(self, perPage):
        # 分页个数，默认不分页
        
        return self.set("perPage", perPage)

        
    def maxLength(self, maxLength):
        # 限制最大个数
        
        return self.set("maxLength", maxLength)

        
    def minLength(self, minLength):
        # 限制最小个数
        
        return self.set("minLength", minLength)

        
    def showFooterAddBtn(self, showFooterAddBtn):
        # 是否显示底部新增按钮
        
        return self.set("showFooterAddBtn", showFooterAddBtn)

        
    def showTableAddBtn(self, showTableAddBtn):
        # 是否显示表格操作栏新增按钮
        
        return self.set("showTableAddBtn", showTableAddBtn)

        
    def footerAddBtn(self, footerAddBtn):
        # 底部新增按钮配置
        
        return self.set("footerAddBtn", footerAddBtn)

        
    def enableStaticTransform(self, enableStaticTransform):
        # 是否开启 static 状态切换
        
        return self.set("enableStaticTransform", enableStaticTransform)

        