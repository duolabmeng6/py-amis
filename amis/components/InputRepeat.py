
from amis.AmisComponent import AmisComponent

class InputRepeat(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-repeat")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def options(self, options):
        # 可用配置 `secondly,minutely,hourly,daily,weekdays,weekly,monthly,yearly` 可选项: string
        return self.set("options", options)

        
    def placeholder(self, placeholder):
        # 当不指定值时的说明。 可选项: string
        return self.set("placeholder", placeholder)

        