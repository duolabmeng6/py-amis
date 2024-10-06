
from amis.AmisComponent import AmisComponent

class InputPassword(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-password")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def revealPassword(self, revealPassword):
        # 是否展示密码显/隐按钮 可选项: boolean
        return self.set("revealPassword", revealPassword)

        