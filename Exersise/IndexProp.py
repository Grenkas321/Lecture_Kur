class Sequence:
    _Miss = object()

    def __init__ (self, initial = _Miss):
        if initial is self._Miss:
            self._seq = []
            self._fact = list
        else:
            self.sequence = initial

    @staticmethod
    def _is_indexable(obj):
        return hasattr(obj, "__getitem__")

    @property
    def sequence(self):
        return self._seq

    @sequence.setter
    def sequence(self, value):
        if self._is_indexable(value):
            self._seq = value
            self._fact = type(value)
        else:
            self._seq = [value]
            self._fact = list

    @sequence.deleter
    def sequence(self):
        self._seq = self._fact()