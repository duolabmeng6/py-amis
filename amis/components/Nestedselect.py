
from amis.AmisComponent import AmisComponent

class Nestedselect(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "nestedselect")
    
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
    def delimiter(self, delimiter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: boolean
        return self.set("delimiter", delimiter)

        
    def labelField(self, labelField):
        # [选项标签字段](./options#%E9%80%89%E9%A1%B9%E6%A0%87%E7%AD%BE%E5%AD%97%E6%AE%B5-labelfield) 可选项: boolean
        return self.set("labelField", labelField)

        
    def valueField(self, valueField):
        # [选项值字段](./options#%E9%80%89%E9%A1%B9%E5%80%BC%E5%AD%97%E6%AE%B5-valuefield) 可选项: boolean
        return self.set("valueField", valueField)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def autoFill(self, autoFill):
        # [自动填充](./options#%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85-autofill) 可选项: object
        return self.set("autoFill", autoFill)

        
    def cascade(self, cascade):
        # 设置 `true`时，当选中父节点时不自动选择子节点。 可选项: boolean
        return self.set("cascade", cascade)

        
    def withChildren(self, withChildren):
        # 设置 `true`时，选中父节点时，值里面将包含子节点的值，否则只会保留父节点的值。 可选项: boolean
        return self.set("withChildren", withChildren)

        
    def onlyChildren(self, onlyChildren):
        # 多选时，选中父节点时，是否只将其子节点加入到值中。 可选项: boolean
        return self.set("onlyChildren", onlyChildren)

        
    def searchable(self, searchable):
        # 可否搜索 可选项: boolean
        return self.set("searchable", searchable)

        
    def searchPromptText(self, searchPromptText):
        # 搜索框占位文本 可选项: string
        return self.set("searchPromptText", searchPromptText)

        
    def noResultsText(self, noResultsText):
        # 无结果时的文本 可选项: string
        return self.set("noResultsText", noResultsText)

        
    def multiple(self, multiple):
        # 可否多选 可选项: boolean
        return self.set("multiple", multiple)

        
    def hideNodePathLabel(self, hideNodePathLabel):
        # 是否隐藏选择框中已选择节点的路径 label 信息 可选项: boolean
        return self.set("hideNodePathLabel", hideNodePathLabel)

        
    def onlyLeaf(self, onlyLeaf):
        # 只允许选择叶子节点 可选项: boolean
        return self.set("onlyLeaf", onlyLeaf)

        