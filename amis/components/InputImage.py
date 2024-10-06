
from amis.AmisComponent import AmisComponent

class InputImage(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "input-image")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def receiver(self, receiver):
        # 上传文件接口 可选项: [API](../../../docs/types/api)
        return self.set("receiver", receiver)

        
    def accept(self, accept):
        # 支持的图片类型格式，请配置此属性为图片后缀，例如`.jpg,.png` 可选项: string
        return self.set("accept", accept)

        
    def capture(self, capture):
        # 用于控制 input[type=file] 标签的 capture 属性，在移动端可控制输入来源 可选项: string
        return self.set("capture", capture)

        
    def maxSize(self, maxSize):
        # 默认没有限制，当设置后，文件大小大于此值将不允许上传。单位为`B` 可选项: number
        return self.set("maxSize", maxSize)

        
    def maxLength(self, maxLength):
        # 默认没有限制，当设置后，一次只允许上传指定数量文件。 可选项: number
        return self.set("maxLength", maxLength)

        
    def multiple(self, multiple):
        # 是否多选。 可选项: boolean
        return self.set("multiple", multiple)

        
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

        
    def fileField(self, fileField):
        # 如果你不想自己存储，则可以忽略此属性。 可选项: string
        return self.set("fileField", fileField)

        
    def crop(self, crop):
        # 用来设置是否支持裁剪。 可选项: boolean或{"aspectRatio":""}
        return self.set("crop", crop)

        
    def cropFormat(self, cropFormat):
        # 裁剪文件格式 可选项: string
        return self.set("cropFormat", cropFormat)

        
    def cropQuality(self, cropQuality):
        # 裁剪文件格式的质量，用于 jpeg/webp，取值在 0 和 1 之间 可选项: number
        return self.set("cropQuality", cropQuality)

        
    def limit(self, limit):
        # 限制图片大小，超出不让上传。 可选项: Limit
        return self.set("limit", limit)

        
    def frameImage(self, frameImage):
        # 默认占位图地址 可选项: string
        return self.set("frameImage", frameImage)

        
    def fixedSize(self, fixedSize):
        # 是否开启固定尺寸,若开启，需同时设置 fixedSizeClassName 可选项: boolean
        return self.set("fixedSize", fixedSize)

        
    def fixedSizeClassName(self, fixedSizeClassName):
        # 开启固定尺寸时，根据此值控制展示尺寸。例如`h-30`,即图片框高为 h-30,AMIS 将自动缩放比率设置默认图所占位置的宽度，最终上传图片根据此尺寸对应缩放。 可选项: string
        return self.set("fixedSizeClassName", fixedSizeClassName)

        
    def initAutoFill(self, initAutoFill):
        # 表单反显时是否执行 autoFill 可选项: boolean
        return self.set("initAutoFill", initAutoFill)

        
    def uploadBtnText(self, uploadBtnText):
        # 上传按钮文案。支持 tpl、schema 形式配置。 可选项: string,[SchemaNode](../../docs/types/schemanode)
        return self.set("uploadBtnText", uploadBtnText)

        
    def dropCrop(self, dropCrop):
        # 图片上传后是否进入裁剪模式 可选项: boolean
        return self.set("dropCrop", dropCrop)

        
    def initCrop(self, initCrop):
        # 图片选择器初始化后是否立即进入裁剪模式 可选项: boolean
        return self.set("initCrop", initCrop)

        
    def draggable(self, draggable):
        # 开启后支持拖拽排序改变图片值顺序 可选项: boolean
        return self.set("draggable", draggable)

        
    def draggableTip(self, draggableTip):
        # 拖拽提示文案 可选项: string
        return self.set("draggableTip", draggableTip)

        