class Generative(type):
    _count = 0

    @property
    def generation(cls):
        return Generative._count

    def __new__(mcls, name, bases, namespace, **kwargs):
        def __getattr__(self, attr):
            if attr == "generation":
                return type(self).generation
            raise AttributeError(attr)

        namespace.setdefault("__getattr__", __getattr__)
        cls = super().__new__(mcls, name, bases, namespace)
        Generative._count += 1
        return cls
