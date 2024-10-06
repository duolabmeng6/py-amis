
from amis.AmisComponent import AmisComponent

class PdfViewer(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "pdf-viewer")
    
    def src(self, src):
        # 文档地址 可选项: Api
        return self.set("src", src)

        
    def width(self, width):
        # 宽度 可选项: number
        return self.set("width", width)

        
    def height(self, height):
        # 高度 可选项: number
        return self.set("height", height)

        
    def background(self, background):
        # PDF 背景色 可选项: string
        return self.set("background", background)

        