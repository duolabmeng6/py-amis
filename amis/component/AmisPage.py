from amis.component.AmisComponent import AmisComponent
import json
from typing import List, Dict, Any, Union, Literal


class AmisPage(AmisComponent):
    def __init__(self):
        super().__init__("page")

    def body(self, *components):
        self._props["body"] = [comp.to_dict() for comp in components]
        return self
