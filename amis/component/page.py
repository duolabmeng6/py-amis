from amis.AmisComponent import AmisComponent


class page(AmisComponent):
    def __init__(self):
        super().__init__("page")

    def body(self, *components):
        self._props["body"] = [comp.to_dict() for comp in components]
        return self
