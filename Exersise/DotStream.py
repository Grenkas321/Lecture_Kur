class Dots:
    def __init__(self, a: float, b: float):
        self.a = float(a)
        self.b = float(b)

    def _step(self, n: int) -> float:
        if not isinstance(n, int):
            raise TypeError("n должен быть целым числом")
        if n <= 0:
            raise ValueError("n должен быть положительным")
        return 0.0 if n == 1 else (self.b - self.a) / (n - 1)

    def _value(self, i: int, n: int) -> float:
        if not isinstance(i, int):
            raise TypeError("индексы должны быть целыми")
        s = self._step(n)
        return float(self.a + i * s)

    def _iter_range(self, i: int, j: int, n: int):
        s = self._step(n)
        x = self.a + i * s
        for _k in range(i, j):
            yield float(x)
            x += s

    def __getitem__(self, key):
        if isinstance(key, int):
            n = key
            return self._iter_range(0, n, n)
        if isinstance(key, slice):
            if key.step is None:
                i = 0 if key.start is None else key.start
                n = key.stop
                if n is None:
                    raise TypeError("нужно указать n")
                return self._value(i, n)
            else:
                n = key.step
                i = 0 if key.start is None else key.start
                j = n if key.stop is None else key.stop
                return self._iter_range(i, j, n)
        raise TypeError("некорректный индекс")
