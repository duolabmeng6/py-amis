
from amis.AmisComponent import AmisComponent

class InputRichText(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-rich-text")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def saveAsUbb(self, saveAsUbb):
        # 是否保存为 ubb 格式 可选项: boolean
        return self.set("saveAsUbb", saveAsUbb)

        
    def receiver(self, receiver):
        # 默认的图片保存 API 可选项: [API](../../../docs/types/api)
        return self.set("receiver", receiver)

        
    def videoReceiver(self, videoReceiver):
        # 默认的视频保存 API `仅支持 froala 编辑器` 可选项: [API](../../../docs/types/api)
        return self.set("videoReceiver", videoReceiver)

        
    def fileField(self, fileField):
        # 上传文件时的字段名 可选项: string
        return self.set("fileField", fileField)

        
    def size(self, size):
        # 框的大小，可设置为 `md` 或者 `lg` 可选项: string
        return self.set("size", size)

        
    def options(self, options):
        # 需要参考 [tinymce](https://www.tiny.cloud/docs/configure/integration-and-setup/) 或 [froala](https://www.froala.com/wysiwyg-editor/docs/options) 的文档 可选项: object
        return self.set("options", options)

        
    def buttons(self, buttons):
        # froala 专用，配置显示的按钮，tinymce 可以通过前面的 options 设置 [toolbar](https://www.tiny.cloud/docs/demo/custom-toolbar-button/) 字符串 可选项: Array<string>
        return self.set("buttons", buttons)

        