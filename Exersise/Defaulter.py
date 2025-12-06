class Defaulter:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        ann = getattr(cls, "__annotations__", {})
        for name, tp in ann.items():
            if isinstance(tp, type):
                setattr(cls, name, tp())
