
from amis.AmisComponent import AmisComponent

class TransferPicker(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "transfer-picker")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def borderMode(self, borderMode):
        # 边框模式，`'full'`为全边框，`'half'`为半边框，`'none'`为没边框 可选项: full,half,none
        return self.set("borderMode", borderMode)

        
    def pickerSize(self, pickerSize):
        # 弹窗大小，支持: xs、sm、md、lg、xl、full 可选项: string
        return self.set("pickerSize", pickerSize)

        