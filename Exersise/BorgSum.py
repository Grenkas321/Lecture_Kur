import weakref

class Borg:
    _refs = []

    def __init__(self, value=0):
        self.value = value
        Borg._refs.append(weakref.ref(self))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        for r in Borg._refs:
            obj = r()
            if obj is not None:
                yield obj.value

    def __iadd__(self, num):
        for r in Borg._refs:
            obj = r()
            if obj is not None:
                obj.value += num
        return self

    def __isub__(self, num):
        for r in Borg._refs:
            obj = r()
            if obj is not None:
                obj.value -= num
        return self
