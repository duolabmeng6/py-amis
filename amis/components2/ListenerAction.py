
from amis.AmisComponent import AmisComponent

class ListenerAction(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "listener-action")
        
    
    def actionType(self, actionType):
        
        
        return self.set("actionType", actionType)

        
    def description(self, description):
        
        
        return self.set("description", description)

        
    def componentId(self, componentId):
        
        
        return self.set("componentId", componentId)

        
    def componentName(self, componentName):
        
        
        return self.set("componentName", componentName)

        
    def ignoreError(self, ignoreError):
        
        
        return self.set("ignoreError", ignoreError)

        
    def args(self, args):
        
        
        return self.set("args", args)

        
    def data(self, data):
        
        
        return self.set("data", data)

        
    def dataMergeMode(self, dataMergeMode):
        # 可选项: ['merge', 'override']
        
        return self.set("dataMergeMode", dataMergeMode)

        
    def outputVar(self, outputVar):
        
        
        return self.set("outputVar", outputVar)

        
    def preventDefault(self, preventDefault):
        
        
        return self.set("preventDefault", preventDefault)

        
    def stopPropagation(self, stopPropagation):
        
        
        return self.set("stopPropagation", stopPropagation)

        
    def expression(self, expression):
        
        
        return self.set("expression", expression)

        
    def execOn(self, execOn):
        
        
        return self.set("execOn", execOn)

        