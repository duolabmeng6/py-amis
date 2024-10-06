
from amis.AmisComponent import AmisComponent

class InputTree(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-tree")
    
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../../docs/types/api)
        return self.set("source", source)

        
    def autoComplete(self, autoComplete):
        # [自动提示补全](./options#%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8-autocomplete) 可选项: [API](../../../../docs/types/api)
        return self.set("autoComplete", autoComplete)

        
    def multiple(self, multiple):
        # 是否多选 可选项: boolean
        return self.set("multiple", multiple)

        
    def delimiter(self, delimiter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: string
        return self.set("delimiter", delimiter)

        
    def labelField(self, labelField):
        # [选项标签字段](./options#%E9%80%89%E9%A1%B9%E6%A0%87%E7%AD%BE%E5%AD%97%E6%AE%B5-labelfield) 可选项: string
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # [选项值字段](./options#%E9%80%89%E9%A1%B9%E5%80%BC%E5%AD%97%E6%AE%B5-valuefield) 可选项: string
        return self.set("valueField", valueField)

        
    def iconField(self, iconField):
        # 图标值字段 可选项: string
        return self.set("iconField", iconField)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def creatable(self, creatable):
        # [新增选项](./options#%E5%89%8D%E7%AB%AF%E6%96%B0%E5%A2%9E-creatable) 可选项: boolean
        return self.set("creatable", creatable)

        
    def addControls(self, addControls):
        # [自定义新增表单项](./options#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%96%B0%E5%A2%9E%E8%A1%A8%E5%8D%95%E9%A1%B9-addcontrols) 可选项: Array<[表单项](./formitem)>
        return self.set("addControls", addControls)

        
    def addApi(self, addApi):
        # [配置新增选项接口](./options#%E9%85%8D%E7%BD%AE%E6%96%B0%E5%A2%9E%E6%8E%A5%E5%8F%A3-addapi) 可选项: [API](../../../docs/types/api)
        return self.set("addApi", addApi)

        
    def editable(self, editable):
        # [编辑选项](./options#%E5%89%8D%E7%AB%AF%E7%BC%96%E8%BE%91-editable) 可选项: boolean
        return self.set("editable", editable)

        
    def editControls(self, editControls):
        # [自定义编辑表单项](./options#%E8%87%AA%E5%AE%9A%E4%B9%89%E7%BC%96%E8%BE%91%E8%A1%A8%E5%8D%95%E9%A1%B9-editcontrols) 可选项: Array<[表单项](./formitem)>
        return self.set("editControls", editControls)

        
    def editApi(self, editApi):
        # [配置编辑选项接口](./options#%E9%85%8D%E7%BD%AE%E7%BC%96%E8%BE%91%E6%8E%A5%E5%8F%A3-editapi) 可选项: [API](../../../docs/types/api)
        return self.set("editApi", editApi)

        
    def removable(self, removable):
        # [删除选项](./options#%E5%88%A0%E9%99%A4%E9%80%89%E9%A1%B9) 可选项: boolean
        return self.set("removable", removable)

        
    def deleteApi(self, deleteApi):
        # [配置删除选项接口](./options#%E9%85%8D%E7%BD%AE%E5%88%A0%E9%99%A4%E6%8E%A5%E5%8F%A3-deleteapi) 可选项: [API](../../../docs/types/api)
        return self.set("deleteApi", deleteApi)

        
    def hideRoot(self, hideRoot):
        # 如果想要显示个顶级节点，请设置为 `false` 可选项: boolean
        return self.set("hideRoot", hideRoot)

        
    def rootLabel(self, rootLabel):
        # 当 `hideRoot` 不为 `false` 时有用，用来设置顶级节点的文字。 可选项: boolean
        return self.set("rootLabel", rootLabel)

        
    def showIcon(self, showIcon):
        # 是否显示图标 可选项: boolean
        return self.set("showIcon", showIcon)

        
    def showRadio(self, showRadio):
        # 是否显示单选按钮，`multiple` 为 `false` 是有效。 可选项: boolean
        return self.set("showRadio", showRadio)

        
    def showOutline(self, showOutline):
        # 是否显示树层级展开线 可选项: boolean
        return self.set("showOutline", showOutline)

        
    def initiallyOpen(self, initiallyOpen):
        # 设置是否默认展开所有层级。 可选项: boolean
        return self.set("initiallyOpen", initiallyOpen)

        
    def unfoldedLevel(self, unfoldedLevel):
        # 设置默认展开的级数，只有`initiallyOpen`不是`true`时生效。 可选项: number
        return self.set("unfoldedLevel", unfoldedLevel)

        
    def autoCheckChildren(self, autoCheckChildren):
        # 当选中父节点时级联选择子节点。 可选项: boolean
        return self.set("autoCheckChildren", autoCheckChildren)

        
    def cascade(self, cascade):
        # autoCheckChildren 为 true 时生效；默认行为：子节点禁用，值只包含父节点值；设置为 true 时，子节点可反选，值包含父子节点值。 可选项: boolean
        return self.set("cascade", cascade)

        
    def withChildren(self, withChildren):
        # cascade 为 false 时生效，选中父节点时，值里面将包含父子节点的值，否则只会保留父节点的值。 可选项: boolean
        return self.set("withChildren", withChildren)

        
    def onlyChildren(self, onlyChildren):
        # autoCheckChildren 为 true 时生效，不受 cascade 影响；onlyChildren 为 true，ui 行为级联选中子节点，子节点可反选，值只包含子节点的值。 可选项: boolean
        return self.set("onlyChildren", onlyChildren)

        
    def onlyLeaf(self, onlyLeaf):
        # 只允许选择叶子节点 可选项: boolean
        return self.set("onlyLeaf", onlyLeaf)

        
    def rootCreatable(self, rootCreatable):
        # 是否可以创建顶级节点 可选项: boolean
        return self.set("rootCreatable", rootCreatable)

        
    def rootCreateTip(self, rootCreateTip):
        # 创建顶级节点的悬浮提示 可选项: string
        return self.set("rootCreateTip", rootCreateTip)

        
    def minLength(self, minLength):
        # 最少选中的节点数 可选项: number
        return self.set("minLength", minLength)

        
    def maxLength(self, maxLength):
        # 最多选中的节点数 可选项: number
        return self.set("maxLength", maxLength)

        
    def treeContainerClassName(self, treeContainerClassName):
        # tree 最外层容器类名 可选项: string
        return self.set("treeContainerClassName", treeContainerClassName)

        
    def enableNodePath(self, enableNodePath):
        # 是否开启节点路径模式 可选项: boolean
        return self.set("enableNodePath", enableNodePath)

        
    def pathSeparator(self, pathSeparator):
        # 节点路径的分隔符，`enableNodePath`为`true`时生效 可选项: string
        return self.set("pathSeparator", pathSeparator)

        
    def highlightTxt(self, highlightTxt):
        # 标签中需要高亮的字符，支持变量 可选项: string
        return self.set("highlightTxt", highlightTxt)

        
    def itemHeight(self, itemHeight):
        # 每个选项的高度，用于虚拟渲染 可选项: number
        return self.set("itemHeight", itemHeight)

        
    def virtualThreshold(self, virtualThreshold):
        # 在选项数量超过多少时开启虚拟渲染 可选项: number
        return self.set("virtualThreshold", virtualThreshold)

        