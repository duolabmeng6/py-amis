
from amis.AmisComponent import AmisComponent

class InputFile(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-file")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def receiver(self, receiver):
        # 上传文件接口 可选项: [API](../../../docs/types/api)
        return self.set("receiver", receiver)

        
    def accept(self, accept):
        # 默认只支持纯文本，要支持其他类型，请配置此属性为文件后缀`.xxx` 可选项: string
        return self.set("accept", accept)

        
    def capture(self, capture):
        # 用于控制 input[type=file] 标签的 capture 属性，在移动端可控制输入来源 可选项: string
        return self.set("capture", capture)

        
    def asBase64(self, asBase64):
        # 将文件以`base64`的形式，赋值给当前组件 可选项: boolean
        return self.set("asBase64", asBase64)

        
    def asBlob(self, asBlob):
        # 将文件以二进制的形式，赋值给当前组件 可选项: boolean
        return self.set("asBlob", asBlob)

        
    def maxSize(self, maxSize):
        # 默认没有限制，当设置后，文件大小大于此值将不允许上传。单位为`B` 可选项: number
        return self.set("maxSize", maxSize)

        
    def maxLength(self, maxLength):
        # 默认没有限制，当设置后，一次只允许上传指定数量文件。 可选项: number
        return self.set("maxLength", maxLength)

        
    def multiple(self, multiple):
        # 是否多选。 可选项: boolean
        return self.set("multiple", multiple)

        
    def drag(self, drag):
        # 是否为拖拽上传 可选项: boolean
        return self.set("drag", drag)

        
    def joinValues(self, joinValues):
        # [拼接值](./options#%E6%8B%BC%E6%8E%A5%E5%80%BC-joinvalues) 可选项: boolean
        return self.set("joinValues", joinValues)

        
    def extractValue(self, extractValue):
        # [提取值](./options#%E6%8F%90%E5%8F%96%E5%A4%9A%E9%80%89%E5%80%BC-extractvalue) 可选项: boolean
        return self.set("extractValue", extractValue)

        
    def delimiter(self, delimiter):
        # [拼接符](./options#%E6%8B%BC%E6%8E%A5%E7%AC%A6-delimiter) 可选项: string
        return self.set("delimiter", delimiter)

        
    def autoUpload(self, autoUpload):
        # 否选择完就自动开始上传 可选项: boolean
        return self.set("autoUpload", autoUpload)

        
    def hideUploadButton(self, hideUploadButton):
        # 隐藏上传按钮 可选项: boolean
        return self.set("hideUploadButton", hideUploadButton)

        
    def stateTextMap(self, stateTextMap):
        # 上传状态文案 可选项: object
        return self.set("stateTextMap", stateTextMap)

        
    def fileField(self, fileField):
        # 如果你不想自己存储，则可以忽略此属性。 可选项: string
        return self.set("fileField", fileField)

        
    def nameField(self, nameField):
        # 接口返回哪个字段用来标识文件名 可选项: string
        return self.set("nameField", nameField)

        
    def valueField(self, valueField):
        # 文件的值用那个字段来标识。 可选项: string
        return self.set("valueField", valueField)

        
    def urlField(self, urlField):
        # 文件下载地址的字段名。 可选项: string
        return self.set("urlField", urlField)

        
    def btnLabel(self, btnLabel):
        # 上传按钮的文字 可选项: string
        return self.set("btnLabel", btnLabel)

        
    def downloadUrl(self, downloadUrl):
        # 默认显示文件路径的时候会支持直接下载，可以支持加前缀如：`http://xx.dom/filename=` ，如果不希望这样，可以把当前配置项设置为 `false`。 可选项: boolean或string
        return self.set("downloadUrl", downloadUrl)

        
    def useChunk(self, useChunk):
        # amis 所在服务器，限制了文件上传大小不得超出 10M，所以 amis 在用户选择大文件的时候，自动会改成分块上传模式。 可选项: boolean或"auto"
        return self.set("useChunk", useChunk)

        
    def chunkSize(self, chunkSize):
        # 分块大小 可选项: number
        return self.set("chunkSize", chunkSize)

        
    def startChunkApi(self, startChunkApi):
        # startChunkApi 可选项: [API](../../../docs/types/api)
        return self.set("startChunkApi", startChunkApi)

        
    def chunkApi(self, chunkApi):
        # chunkApi 可选项: [API](../../../docs/types/api)
        return self.set("chunkApi", chunkApi)

        
    def finishChunkApi(self, finishChunkApi):
        # finishChunkApi 可选项: [API](../../../docs/types/api)
        return self.set("finishChunkApi", finishChunkApi)

        
    def concurrency(self, concurrency):
        # 分块上传时并行个数 可选项: number
        return self.set("concurrency", concurrency)

        
    def documentation(self, documentation):
        # 文档内容 可选项: string
        return self.set("documentation", documentation)

        
    def documentLink(self, documentLink):
        # 文档链接 可选项: string
        return self.set("documentLink", documentLink)

        
    def initAutoFill(self, initAutoFill):
        # 初表单反显时是否执行 可选项: boolean
        return self.set("initAutoFill", initAutoFill)

        