
from amis.AmisComponent import AmisComponent

class ListBodyFieldObject(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "list-body-field-object")
        
    
    def label(self, label):
        # 列标题
        
        return self.set("label", label)

        
    def labelClassName(self, labelClassName):
        # label 类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("labelClassName", labelClassName)

        
    def innerClassName(self, innerClassName):
        # 内层组件的CSS类名
        # css类名，配置字符串，或者对象。      className: "red"  用对象配置时意味着你能跟表达式一起搭配使用，如：      className: {         "red": "data.progress > 80",         "blue": "data.progress > 60"     }
        return self.set("innerClassName", innerClassName)

        
    def name(self, name):
        # 绑定字段名
        
        return self.set("name", name)

        
    def popOver(self, popOver):
        # 配置查看详情功能
        
        return self.set("popOver", popOver)

        
    def quickEdit(self, quickEdit):
        # 配置快速编辑功能
        
        return self.set("quickEdit", quickEdit)

        
    def copyable(self, copyable):
        # 配置点击复制功能
        
        return self.set("copyable", copyable)

        