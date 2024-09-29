from typing import Dict, Any, Union, Literal

from amis.AmisComponent import AmisComponent


class button(AmisComponent):
    def __init__(self):
        super().__init__("button")

    def className(self, value: str):
        self._props["className"] = value
        return self

    def url(self, value: str):
        self._props["url"] = value
        return self

    def size(self, value: Literal['xs', 'sm', 'md', 'lg']):
        self._props["size"] = value
        return self

    def actionType(self, value: Literal['button', 'reset', 'submit', 'clear', 'url']):
        self._props["actionType"] = value
        return self

    def level(self, value: Literal[
        'link', 'primary', 'enhance', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']):
        self._props["level"] = value
        return self

    def tooltip(self, value: Union[str, Dict[str, Any]]):
        self._props["tooltip"] = value
        return self

    def tooltipPlacement(self, value: Literal['top', 'right', 'bottom', 'left']):
        self._props["tooltipPlacement"] = value
        return self

    def tooltipTrigger(self, value: Literal['hover', 'focus']):
        self._props["tooltipTrigger"] = value
        return self

    def disabled(self, value: bool):
        self._props["disabled"] = value
        return self

    def disabledTip(self, value: Union[str, Dict[str, Any]]):
        self._props["disabledTip"] = value
        return self

    def block(self, value: bool):
        self._props["block"] = value
        return self

    def loading(self, value: bool):
        self._props["loading"] = value
        return self

    def loadingOn(self, value: str):
        self._props["loadingOn"] = value
        return self
