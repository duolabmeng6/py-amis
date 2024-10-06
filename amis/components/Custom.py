
from amis.AmisComponent import AmisComponent

class Custom(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "custom")
    
    def type(self, type):
        #  可选项: custom
        return self.set("type", type)

        
    def id(self, id):
        # 节点 id 可选项: string
        return self.set("id", id)

        
    def name(self, name):
        # 节点 名称 可选项: string
        return self.set("name", name)

        
    def className(self, className):
        # 节点 class 可选项: string
        return self.set("className", className)

        
    def inline(self, inline):
        # 默认使用 div 标签，如果 true 就使用 span 标签 可选项: boolean
        return self.set("inline", inline)

        
    def html(self, html):
        # 初始化节点 html 可选项: string
        return self.set("html", html)

        
    def onMount(self, onMount):
        # 节点初始化之后调的用函数 可选项: string
        return self.set("onMount", onMount)

        
    def onUpdate(self, onUpdate):
        # 数据有更新的时候调用的函数 可选项: string
        return self.set("onUpdate", onUpdate)

        
    def onUnmount(self, onUnmount):
        # 节点销毁的时候调用的函数 可选项: string
        return self.set("onUnmount", onUnmount)

        