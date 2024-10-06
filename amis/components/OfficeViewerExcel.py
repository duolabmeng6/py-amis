
from amis.AmisComponent import AmisComponent

class OfficeViewerExcel(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "office-viewer-excel")
    