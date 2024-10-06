
from amis.AmisComponent import AmisComponent

class Breadcrumb(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "breadcrumb")
    
    def className(self, className):
        # 外层类名 可选项: string
        return self.set("className", className)

        
    def itemClassName(self, itemClassName):
        # 导航项类名 可选项: string
        return self.set("itemClassName", itemClassName)

        
    def separatorClassName(self, separatorClassName):
        # 分割符类名 可选项: string
        return self.set("separatorClassName", separatorClassName)

        
    def dropdownClassName(self, dropdownClassName):
        # 下拉菜单类名 可选项: string
        return self.set("dropdownClassName", dropdownClassName)

        
    def dropdownItemClassName(self, dropdownItemClassName):
        # 下拉菜单项类名 可选项: string
        return self.set("dropdownItemClassName", dropdownItemClassName)

        
    def separator(self, separator):
        # 分隔符 可选项: string
        return self.set("separator", separator)

        
    def labelMaxLength(self, labelMaxLength):
        # 最大展示长度 可选项: number
        return self.set("labelMaxLength", labelMaxLength)

        
    def tooltipPosition(self, tooltipPosition):
        # 浮窗提示位置 可选项: top,bottom,left,right
        return self.set("tooltipPosition", tooltipPosition)

        
    def source(self, source):
        # 动态数据 可选项: string
        return self.set("source", source)

        