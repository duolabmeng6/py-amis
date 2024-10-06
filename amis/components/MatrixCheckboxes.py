
from amis.AmisComponent import AmisComponent

class MatrixCheckboxes(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "matrix-checkboxes")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def columns(self, columns):
        # 列信息，数组中 `label` 字段是必须给出的 可选项: Array<column>
        return self.set("columns", columns)

        
    def rows(self, rows):
        # 行信息， 数组中 `label` 字段是必须给出的 可选项: Array<row>
        return self.set("rows", rows)

        
    def rowLabel(self, rowLabel):
        # 行标题说明 可选项: string
        return self.set("rowLabel", rowLabel)

        
    def source(self, source):
        # Api 地址，如果选项组不固定，可以通过配置 `source` 动态拉取。 可选项: [API](../../../docs/types/api)
        return self.set("source", source)

        
    def multiple(self, multiple):
        # 是否多选 可选项: boolean
        return self.set("multiple", multiple)

        
    def singleSelectMode(self, singleSelectMode):
        # 设置单选模式，`multiple`为`false`时有效，可设置为`cell`, `row`, `column` 分别为全部选项中只能单选某个单元格、每行只能单选某个单元格，每列只能单选某个单元格 可选项: string
        return self.set("singleSelectMode", singleSelectMode)

        
    def textAlign(self, textAlign):
        # 当开启多选+全选时，默认为'left' 可选项: string
        return self.set("textAlign", textAlign)

        
    def yCheckAll(self, yCheckAll):
        # 列上的全选 可选项: boolean
        return self.set("yCheckAll", yCheckAll)

        
    def xCheckAll(self, xCheckAll):
        # 行上的全选 可选项: boolean
        return self.set("xCheckAll", xCheckAll)

        