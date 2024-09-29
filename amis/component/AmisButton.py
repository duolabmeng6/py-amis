import json
from typing import List, Dict, Any, Union, Literal

from amis.component.AmisComponent import AmisComponent


class AmisButton(AmisComponent):
    def __init__(self):
        super().__init__("button")

    def className(self, value: str) -> 'AmisButton':
        self._props["className"] = value
        return self

    def url(self, value: str) -> 'AmisButton':
        self._props["url"] = value
        return self

    def size(self, value: Literal['xs', 'sm', 'md', 'lg']) -> 'AmisButton':
        self._props["size"] = value
        return self

    def actionType(self, value: Literal['button', 'reset', 'submit', 'clear', 'url']) -> 'AmisButton':
        self._props["actionType"] = value
        return self

    def level(self, value: Literal[
        'link', 'primary', 'enhance', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']) -> 'AmisButton':
        self._props["level"] = value
        return self

    def tooltip(self, value: Union[str, Dict[str, Any]]) -> 'AmisButton':
        self._props["tooltip"] = value
        return self

    def tooltipPlacement(self, value: Literal['top', 'right', 'bottom', 'left']) -> 'AmisButton':
        self._props["tooltipPlacement"] = value
        return self

    def tooltipTrigger(self, value: Literal['hover', 'focus']) -> 'AmisButton':
        self._props["tooltipTrigger"] = value
        return self

    def disabled(self, value: bool) -> 'AmisButton':
        self._props["disabled"] = value
        return self

    def disabledTip(self, value: Union[str, Dict[str, Any]]) -> 'AmisButton':
        self._props["disabledTip"] = value
        return self

    def block(self, value: bool) -> 'AmisButton':
        self._props["block"] = value
        return self

    def loading(self, value: bool) -> 'AmisButton':
        self._props["loading"] = value
        return self

    def loadingOn(self, value: str) -> 'AmisButton':
        self._props["loadingOn"] = value
        return self
