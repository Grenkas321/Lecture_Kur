class positioned(type):
    def __new__(metaclass, name, bases, namespace, **kwargs):
        annotations = namespace.get("__annotations__", {})
        field_name = tuple(annotations.keys())

        cls = super().__new__(metaclass, name, bases, namespace, **kwargs)
        cls.__match_args__ = field_name

        if field_name and "__init__" not in namespace:
            def __init__(self, *args, **kwargs):
                for fname, value in zip(field_name, args):
                    setattr(self, fname, value)

            cls.__init__ = __init__

        if field_name and "__str__" not in namespace:
            def __str__(self):
                parts = []
                for fname in field_name:
                    val = getattr(self, fname)
                    parts.append(f"{fname}={val}")
                return " ".join(parts)

            cls.__str__ = __str__

        return cls