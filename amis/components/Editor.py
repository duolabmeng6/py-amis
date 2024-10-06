
from amis.AmisComponent import AmisComponent

class Editor(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "editor")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def language(self, language):
        # 编辑器高亮的语言，支持通过 `${xxx}` 变量获取 可选项: string
        return self.set("language", language)

        
    def size(self, size):
        # 编辑器高度，取值可以是 `md`、`lg`、`xl`、`xxl` 可选项: string
        return self.set("size", size)

        
    def allowFullscreen(self, allowFullscreen):
        # 是否显示全屏模式开关 可选项: boolean
        return self.set("allowFullscreen", allowFullscreen)

        
    def options(self, options):
        # monaco 编辑器的其它配置，比如是否显示行号等，请参考[这里](https://microsoft.github.io/monaco-editor/docs.html#interfaces/editor.IEditorOptions.html)，不过无法设置 readOnly，只读模式需要使用 `disabled: true` 可选项: object
        return self.set("options", options)

        
    def placeholder(self, placeholder):
        # 占位描述，没有值的时候展示 可选项: string
        return self.set("placeholder", placeholder)

        