
from amis.AmisComponent import AmisComponent

class JsonSchema(AmisComponent):
    def __init__(self):
        super().__init__()
        self.set("type", "json-schema")
    
    def schema(self, schema):
        # 指定 json-schema 可选项: object,string
        return self.set("schema", schema)

        