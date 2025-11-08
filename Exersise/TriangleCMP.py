from math import sqrt, isclose


class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)
        if (
            self.a <= 0 or self.b <= 0 or self.c <= 0 or
            self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a
        ):
            self.empty = True
        else:
            self.empty = False

    def __bool__(self):
        return not self.empty

    def area(self):
        if self.empty:
            return 0.0
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __abs__(self):
        return self.area()

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return all(isclose(x, y) for x, y in zip(sorted([self.a, self.b, self.c]),
                                                 sorted([other.a, other.b, other.c])))

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __str__(self):
        return f"{self.a}:{self.b}:{self.c}"
