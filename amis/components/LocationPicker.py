
from amis.AmisComponent import AmisComponent

class LocationPicker(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "location-picker")
    
    def 属性名(self, 属性名):
        # 说明 可选项: 类型
        return self.set("属性名", 属性名)

        
    def value(self, value):
        #  可选项: LocationData
        return self.set("value", value)

        
    def vendor(self, vendor):
        # 地图厂商，目前只实现了百度地图和高德地图 可选项: baidu,gaode
        return self.set("vendor", vendor)

        
    def ak(self, ak):
        # 百度/高德地图的 ak 可选项: string
        return self.set("ak", ak)

        
    def clearable(self, clearable):
        # 输入框是否可清空 可选项: boolean
        return self.set("clearable", clearable)

        
    def placeholder(self, placeholder):
        # 默认提示 可选项: string
        return self.set("placeholder", placeholder)

        
    def autoSelectCurrentLoc(self, autoSelectCurrentLoc):
        # 是否自动选中当前地理位置 可选项: boolean
        return self.set("autoSelectCurrentLoc", autoSelectCurrentLoc)

        
    def onlySelectCurrentLoc(self, onlySelectCurrentLoc):
        # 是否限制只能选中当前地理位置，设置为 true 后，可用于充当定位组件 可选项: boolean
        return self.set("onlySelectCurrentLoc", onlySelectCurrentLoc)

        
    def coordinatesType(self, coordinatesType):
        # 坐标系类型，默认百度坐标，使用高德地图时应设置为'gcj02'， 高德地图不支持坐标转换 可选项: bd09,gcj02
        return self.set("coordinatesType", coordinatesType)

        