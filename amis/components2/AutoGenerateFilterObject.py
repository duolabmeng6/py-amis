
from amis.AmisComponent import AmisComponent

class AutoGenerateFilterObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "auto-generate-filter-object")
        
    
    def columnsNum(self, columnsNum):
        # 过滤条件单行列数
        
        return self.set("columnsNum", columnsNum)

        
    def showBtnToolbar(self, showBtnToolbar):
        # 是否显示设置查询字段
        
        return self.set("showBtnToolbar", showBtnToolbar)

        
    def defaultCollapsed(self, defaultCollapsed):
        # 是否默认收起
        
        return self.set("defaultCollapsed", defaultCollapsed)

        