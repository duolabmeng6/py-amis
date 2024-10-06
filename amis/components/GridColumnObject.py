
from amis.AmisComponent import AmisComponent

class GridColumnObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "grid-column-object")
        
    
    def id(self, id):
        # 组件唯一 id
        
        return self.set("id", id)

        
    def xs(self, xs):
        # 极小屏（<768px）时宽度占比
        
        return self.set("xs", xs)

        
    def sm(self, sm):
        # 小屏时（>=768px）宽度占比
        
        return self.set("sm", sm)

        
    def md(self, md):
        # 中屏时(>=992px)宽度占比
        
        return self.set("md", md)

        
    def lg(self, lg):
        # 大屏时(>=1200px)宽度占比
        
        return self.set("lg", lg)

        
    def valign(self, valign):
        # 垂直对齐方式# 可选项: ['top', 'middle', 'bottom', 'between']
        
        return self.set("valign", valign)

        
    def mode(self, mode):
        # 配置子表单项默认的展示方式。# 可选项: ['normal', 'inline', 'horizontal']
        
        return self.set("mode", mode)

        
    def horizontal(self, horizontal):
        # 如果是水平排版，这个属性可以细化水平排版的左右宽度占比。
        
        return self.set("horizontal", horizontal)

        
    def body(self, body):
        
        
        return self.set("body", body)

        
    def columnClassName(self, columnClassName):
        # 列类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("columnClassName", columnClassName)

        
    def style(self, style):
        # 样式
        
        return self.set("style", style)

        
    def wrapperCustomStyle(self, wrapperCustomStyle):
        
        
        return self.set("wrapperCustomStyle", wrapperCustomStyle)

        
    def themeCss(self, themeCss):
        
        
        return self.set("themeCss", themeCss)

        