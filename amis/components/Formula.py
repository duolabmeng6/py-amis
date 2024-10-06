
from amis.AmisComponent import AmisComponent

class Formula(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "formula")
    
    def name(self, name):
        # 需要应用的表单项`name`值，公式结果将作用到此处指定的变量中去。 可选项: string
        return self.set("name", name)

        
    def formula(self, formula):
        # 应用的公式 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("formula", formula)

        
    def condition(self, condition):
        # 公式作用条件 可选项: [表达式](../../../docs/concepts/expression)
        return self.set("condition", condition)

        
    def initSet(self, initSet):
        # 初始化时是否设置 可选项: boolean
        return self.set("initSet", initSet)

        
    def autoSet(self, autoSet):
        # 观察公式结果，如果计算结果有变化，则自动应用到变量上 可选项: boolean
        return self.set("autoSet", autoSet)

        
    def id(self, id):
        # 定义个名字，当某个按钮的目标指定为此值后，会触发一次公式应用。这个机制可以在 `autoSet` 为 false 时用来手动触发 可选项: string
        return self.set("id", id)

        