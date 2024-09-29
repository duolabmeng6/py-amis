import json
import os
from typing import List, Dict, Any, Union, Literal


class AmisComponent:
    
    _props: Dict[str, Any]
    
    def __init__(self, component_type: str):
        self._props = {}
        self.set("type", component_type)

    def label(self, value: str):
        self.set("label", value)
        return self

    def __getattr__(self, name):
        def setter(*args):
            if len(args) == 1:
                self.set(name, args[0])
            else:
                self.set(name, args)
            return self

        return setter

    def set(self, key: str, value: Any):
        self._props[key] = value
        return self

    def to_dict(self) -> Dict[str, Any]:
        return self._props

    def to_json(self) -> str:
        return json.dumps(self._props, indent=2, ensure_ascii=False)


    def to_html(self):
        # 读入 ./tpl/amis.html 替换 ${amis_json} 为 self.to_json()
        # ./当前文件路径
        with open(os.path.join(os.path.dirname(__file__), "tpl/amis.html"), "r", encoding="utf-8") as f:
            html = f.read()
        html = html.replace("${amis_json}", self.to_json())
        return html
