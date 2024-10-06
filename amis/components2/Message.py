
from amis.AmisComponent import AmisComponent

class Message(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "message")
        
    
    def fetchFailed(self, fetchFailed):
        # 获取失败时的提示
        
        return self.set("fetchFailed", fetchFailed)

        
    def fetchSuccess(self, fetchSuccess):
        # 获取成功的提示，默认为空。
        
        return self.set("fetchSuccess", fetchSuccess)

        
    def saveFailed(self, saveFailed):
        # 保存失败时的提示。
        
        return self.set("saveFailed", saveFailed)

        
    def saveSuccess(self, saveSuccess):
        # 保存成功时的提示。
        
        return self.set("saveSuccess", saveSuccess)

        