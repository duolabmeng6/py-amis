
from amis.AmisComponent import AmisComponent

class Transfer(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "transfer")
    
    def options(self, options):
        # [选项组](./options#%E9%9D%99%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-options) 可选项: Array<object>或Array<string>
        return self.set("options", options)

        
    def source(self, source):
        # [动态选项组](./options#%E5%8A%A8%E6%80%81%E9%80%89%E9%A1%B9%E7%BB%84-source) 可选项: string或[API](../../../docs/types/api)
        return self.set("source", source)

        
    def delimeter(self, delimeter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: string
        return self.set("delimeter", delimeter)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def searchApi(self, searchApi):
        # 如果想通过接口检索，可以设置这个 api。 可选项: [API](../../../docs/types/api)
        return self.set("searchApi", searchApi)

        
    def resultListModeFollowSelect(self, resultListModeFollowSelect):
        # 结果面板跟随模式，目前只支持`list`、`table`、`tree`（tree 目前只支持非延时加载的`tree`） 可选项: boolean
        return self.set("resultListModeFollowSelect", resultListModeFollowSelect)

        
    def statistics(self, statistics):
        # 是否显示统计数据 可选项: boolean
        return self.set("statistics", statistics)

        
    def selectTitle(self, selectTitle):
        # 左侧的标题文字 可选项: string
        return self.set("selectTitle", selectTitle)

        
    def resultTitle(self, resultTitle):
        # 右侧结果的标题文字 可选项: string
        return self.set("resultTitle", resultTitle)

        
    def sortable(self, sortable):
        # 结果可以进行拖拽排序（结果列表为树时，不支持排序） 可选项: boolean
        return self.set("sortable", sortable)

        
    def selectMode(self, selectMode):
        # 可选：`list`、`table`、`tree`、`chained`、`associated`。分别为：列表形式、表格形式、树形选择形式、级联选择形式，关联选择形式（与级联选择的区别在于，级联是无限极，而关联只有一级，关联左边可以是个 tree）。 可选项: string
        return self.set("selectMode", selectMode)

        
    def searchResultMode(self, searchResultMode):
        # 如果不设置将采用 `selectMode` 的值，可以单独配置，参考 `selectMode`，决定搜索结果的展示形式。 可选项: string
        return self.set("searchResultMode", searchResultMode)

        
    def searchable(self, searchable):
        # 左侧列表搜索功能，当设置为  true  时表示可以通过输入部分内容检索出选项项。 可选项: boolean
        return self.set("searchable", searchable)

        
    def searchPlaceholder(self, searchPlaceholder):
        # 左侧列表搜索框提示 可选项: string
        return self.set("searchPlaceholder", searchPlaceholder)

        
    def columns(self, columns):
        # 当展示形式为 `table` 可以用来配置展示哪些列，跟 table 中的 columns 配置相似，只是只有展示功能。 可选项: Array<Object>
        return self.set("columns", columns)

        
    def leftOptions(self, leftOptions):
        # 当展示形式为 `associated` 时用来配置左边的选项集。 可选项: Array<Object>
        return self.set("leftOptions", leftOptions)

        
    def leftMode(self, leftMode):
        # 当展示形式为 `associated` 时用来配置左边的选择形式，支持 `list` 或者 `tree`。默认为 `list`。 可选项: string
        return self.set("leftMode", leftMode)

        
    def rightMode(self, rightMode):
        # 当展示形式为 `associated` 时用来配置右边的选择形式，可选：`list`、`table`、`tree`、`chained`。 可选项: string
        return self.set("rightMode", rightMode)

        
    def resultSearchable(self, resultSearchable):
        # 结果（右则）列表的检索功能，当设置为 true 时，可以通过输入检索模糊匹配检索内容（目前树的延时加载不支持结果搜索功能） 可选项: boolean
        return self.set("resultSearchable", resultSearchable)

        
    def resultSearchPlaceholder(self, resultSearchPlaceholder):
        # 右侧列表搜索框提示 可选项: string
        return self.set("resultSearchPlaceholder", resultSearchPlaceholder)

        
    def menuTpl(self, menuTpl):
        # 用来自定义选项展示 可选项: string,[SchemaNode](../../docs/types/schemanode)
        return self.set("menuTpl", menuTpl)

        
    def valueTpl(self, valueTpl):
        # 用来自定义值的展示 可选项: string,[SchemaNode](../../docs/types/schemanode)
        return self.set("valueTpl", valueTpl)

        
    def itemHeight(self, itemHeight):
        # 每个选项的高度，用于虚拟渲染 可选项: number
        return self.set("itemHeight", itemHeight)

        
    def virtualThreshold(self, virtualThreshold):
        # 在选项数量超过多少时开启虚拟渲染 可选项: number
        return self.set("virtualThreshold", virtualThreshold)

        