import json
from typing import List, Dict, Any, Union, Literal


class AmisComponent:
    def __init__(self, component_type: str):
        self._props = {"type": component_type}

    def label(self, value: str):
        self._props["label"] = value
        return self

    def __getattr__(self, name):
        def setter(*args):
            if len(args) == 1:
                self._props[name] = args[0]
            else:
                self._props[name] = args
            return self

        return setter

    def set(self, key: str, value: Any):
        self._props[key] = value
        return self

    def to_dict(self) -> Dict[str, Any]:
        return self._props

    def to_json(self) -> str:
        return json.dumps(self._props, indent=2, ensure_ascii=False)

