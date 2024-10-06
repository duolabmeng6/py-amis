
from amis.AmisComponent import AmisComponent

class Button(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "button")
    
    def className(self, className):
        # 指定添加 button 类名 可选项: string
        return self.set("className", className)

        
    def url(self, url):
        # 点击跳转的地址，指定此属性 button 的行为和 a 链接一致 可选项: string
        return self.set("url", url)

        
    def size(self, size):
        # 设置按钮大小 可选项: xs,sm,md,lg
        return self.set("size", size)

        
    def actionType(self, actionType):
        # 设置按钮类型 可选项: button,reset,submit,clear,url
        return self.set("actionType", actionType)

        
    def level(self, level):
        # 设置按钮样式 可选项: link,primary,enhance,secondary,info,success,warning,danger,light,dark,default
        return self.set("level", level)

        
    def tooltip(self, tooltip):
        # 气泡提示内容 可选项: string,TooltipObject
        return self.set("tooltip", tooltip)

        
    def tooltipPlacement(self, tooltipPlacement):
        # 气泡框位置器 可选项: top,right,bottom,left
        return self.set("tooltipPlacement", tooltipPlacement)

        
    def tooltipTrigger(self, tooltipTrigger):
        # 触发 tooltip 可选项: hover,focus
        return self.set("tooltipTrigger", tooltipTrigger)

        
    def disabled(self, disabled):
        # 按钮失效状态 可选项: boolean
        return self.set("disabled", disabled)

        
    def disabledTip(self, disabledTip):
        # 按钮失效状态下的提示 可选项: string,TooltipObject
        return self.set("disabledTip", disabledTip)

        
    def block(self, block):
        # 将按钮宽度调整为其父宽度的选项 可选项: boolean
        return self.set("block", block)

        
    def loading(self, loading):
        # 显示按钮 loading 效果 可选项: boolean
        return self.set("loading", loading)

        
    def loadingOn(self, loadingOn):
        # 显示按钮 loading 表达式 可选项: string
        return self.set("loadingOn", loadingOn)

        