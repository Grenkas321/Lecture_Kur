class ParDescr:
    def __init__(self, initial):
        self.initial = initial
        self._slot = None

    def __set_name__(self, owner, name):
        self._name = name
        self._slot = f"_ParDescr__{name}_{id(self)}"

    def __get__(self, instance, owner = None):
        if instance is None:
            return self.initial
        if hasattr(instance, self._slot):
            return getattr(instance, self._slot)
        return self.initial

    def __set__(self, instance, value):
        setattr(instance, self._slot, value)

    def __delete__(self, instance):
        if hasattr(instance, self._slot):
            delattr(instance, self._slot)
        else:
            raise KeyError(self._name)