
from amis.AmisComponent import AmisComponent

class ChartRadios(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "chart-radios")
    
    def 属性名(self, 属性名):
        # 说明 ## 二级标题 可选项: 类型
        return self.set("属性名", 属性名)

        
    def config(self, config):
        # echart 图表配置 可选项: object
        return self.set("config", config)

        
    def showTooltipOnHighlight(self, showTooltipOnHighlight):
        # 高亮的时候是否显示 tooltip 可选项: boolean
        return self.set("showTooltipOnHighlight", showTooltipOnHighlight)

        
    def chartValueField(self, chartValueField):
        # 图表数值字段名 可选项: string
        return self.set("chartValueField", chartValueField)

        