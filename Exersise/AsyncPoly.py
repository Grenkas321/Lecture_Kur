import asyncio

class YesFuture:
    def __init__(self, value=None):
        self._value = value

    def set(self, value):
        self._value = value

    def __await__(self):
        async def _inner():
            return self._value
        return _inner().__await__()


DIGITS = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
}


def parse_poly(poly: str, x: YesFuture):
    s = poly.replace(" ", "")
    if not s:
        terms = []
    else:
        if s[0] not in "+-":
            s = "+" + s

        i = 0
        terms = []
        n = len(s)

        while i < n:
            sign = 1
            if s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "-":
                sign = -1
                i += 1

            coef_digits = []
            while i < n and s[i].isdigit():
                coef_digits.append(s[i])
                i += 1
            coef_str = "".join(coef_digits)

            has_x = False
            if i < n and s[i] == "x":
                has_x = True
                i += 1

            power = 0
            if has_x:
                if i < n and s[i] in DIGITS:
                    pow_digits = []
                    while i < n and s[i] in DIGITS:
                        pow_digits.append(DIGITS[s[i]])
                        i += 1
                    power = int("".join(pow_digits))
                else:
                    power = 1
            else:
                power = 0

            if coef_str:
                base_coef = int(coef_str)
            else:
                base_coef = 1 if has_x else 0

            if base_coef != 0:
                terms.append((sign, base_coef, power))

    def const(v):
        return YesFuture(v)

    def build_term(sign, base_coef, power):
        if power == 0:
            p = const(1)
        elif power == 1:
            p = x
        else:
            p = Pow(x, const(power))

        if base_coef == 1:
            term = p
        else:
            term = Mul(const(base_coef), p)

        if sign == -1:
            term = Mul(const(-1), term)
        return term

    mono_awaitables = [build_term(sgn, cf, pw) for (sgn, cf, pw) in terms]

    async def eval_poly():
        if not mono_awaitables:
            return 0
        acc = mono_awaitables[0]
        for t in mono_awaitables[1:]:
            acc = Sum(acc, t)
        return await acc

    return eval_poly()
