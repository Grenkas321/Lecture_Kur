class SubString:
    __slots__ = ("_s",)

    def __init__(self, obj=""):
        self._s = str(obj)

    def __str__(self):
        return self._s

    def __repr__(self):
        return f"SubString({self._s!r})"

    def __len__(self):
        return len(self._s)

    def __iter__(self):
        return iter(self._s)

    def __contains__(self, item):
        return str(item) in self._s

    def __getitem__(self, key):
        res = self._s[key]
        return SubString(res) if isinstance(res, str) else res

    def __eq__(self, other):
        return self._s == (other._s if isinstance(other, SubString) else str(other))

    def __hash__(self):
        return hash(self._s)

    def __add__(self, other):
        return SubString(self._s + str(other))

    def __radd__(self, other):
        return SubString(str(other) + self._s)

    def __mul__(self, n: int):
        return SubString(self._s * int(n))

    __rmul__ = __mul__

    def __sub__(self, other):
        o = str(other)
        counts = {}
        for ch in o:
            counts[ch] = counts.get(ch, 0) + 1
        out = []
        for ch in self._s:
            c = counts.get(ch, 0)
            if c:
                counts[ch] = c - 1
            else:
                out.append(ch)
        return SubString("".join(out))

    def __rsub__(self, other):
        return SubString(str(other)).__sub__(self._s)

    def __getattr__(self, name):
        attr = getattr(self._s, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                def _coerce(x):
                    return x._s if isinstance(x, SubString) else x
                args = tuple(_coerce(a) for a in args)
                kwargs = {k: _coerce(v) for k, v in kwargs.items()}
                res = attr(*args, **kwargs)
                if isinstance(res, str):
                    return SubString(res)
                if isinstance(res, tuple):
                    return tuple(SubString(x) if isinstance(x, str) else x for x in res)
                return res
            return wrapper
        return attr
