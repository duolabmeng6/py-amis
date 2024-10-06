
from amis.AmisComponent import AmisComponent

class InputVerificationCode(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-verification-code")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def length(self, length):
        # 验证码的长度，根据长度渲染对应个数的输入框 可选项: number
        return self.set("length", length)

        
    def masked(self, masked):
        # 是否是密码模式 可选项: boolean
        return self.set("masked", masked)

        
    def separator(self, separator):
        # 分隔符，支持表达式, 表达式`只`可以访问 index、character 变量, 参考自定义分隔符 可选项: string
        return self.set("separator", separator)

        