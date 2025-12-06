from string import ascii_lowercase as _ASC

def slotgen(number: int):
    if number < 0:
        raise ValueError("Oh, man, it must be positive!!!")

    def _name():
        if number == 0:
            return []
        L = 1
        p = 26
        while p < number:
            L += 1
            p *= 26
        names = []

        for k in range(number):
            n = k
            s = []
            for _ in range(L):
                s.append(_ASC[n % 26])
                n //= 26
            names.append("".join(reversed(s)))
        return names
    
    slot_names = tuple(_name())

    def decorate(cls):
        ns = {}

        for k, v in cls.__dict__.items():
            if k in ("__dict__", "__weakref__", "__slots__"):
                continue
            ns[k] = v

        for k in slot_names:
            ns.pop(k, None)

        ns["__module__"] = cls.__module__
        if cls.__doc__ is not None:
            ns["__doc__"] = cls.__doc__
        ns["__slots__"] = slot_names

        return type(cls.__name__, cls.__bases__, ns)

    return decorate