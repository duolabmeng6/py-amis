
from amis.AmisComponent import AmisComponent

class Toast(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "toast")
    
    def actionType(self, actionType):
        # 指定为 toast 轻提示组件 可选项: string
        return self.set("actionType", actionType)

        
    def items(self, items):
        # 轻提示内容 可选项: Array<ToastItem>
        return self.set("items", items)

        
    def position(self, position):
        # 提示显示位置，可用'top-right'、'top-center'、'top-left'、'bottom-center'、'bottom-left'、'bottom-right'、'center' 可选项: string
        return self.set("position", position)

        
    def closeButton(self, closeButton):
        # 是否展示关闭按钮，移动端不展示 可选项: boolean
        return self.set("closeButton", closeButton)

        
    def showIcon(self, showIcon):
        # 是否展示图标 可选项: boolean
        return self.set("showIcon", showIcon)

        
    def timeout(self, timeout):
        # 持续时间 可选项: number
        return self.set("timeout", timeout)

        