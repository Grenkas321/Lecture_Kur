from collections import Counter

class DefCounter(Counter):
    def __init__(self, *args, missing = -1, **kwargs):
        self.missing = missing
        super().__init__(*args, **kwargs)

    def __missing__(self, key):
        return self.missing

    def __abs__(self):
        return sum (v for v in self.values() if v > 0)

    def __repr__(self):
        items = ", ".join(f"{k!r}: {v!r}" for k, v in self.most_common())
        return f"{self.__class__.__name__}({{{items}}})"