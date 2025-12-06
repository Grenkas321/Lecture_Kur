import inspect

class Absolute(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        width_name = kwargs.pop("width", "width")
        height_name = kwargs.pop("height", "height")

        cls = super().__new__(mcls, name, bases, namespace, **kwargs)

        def zero_arg_ok(func):
            try:
                sig = inspect.signature(func)
            except (TypeError, ValueError):
                return False
            params = list(sig.parameters.values())
            if params:
                params = params[1:]
            for p in params:
                if p.kind in (
                    inspect.Parameter.VAR_POSITIONAL,
                    inspect.Parameter.VAR_KEYWORD,
                ):
                    continue
                if p.default is inspect._empty:
                    return False
            return True

        existing_abs = namespace.get("__abs__")
        if not (callable(existing_abs)):
            func_abs = namespace.get("abs")
            if callable(func_abs) and zero_arg_ok(func_abs):
                def __abs__(self, _f=func_abs):
                    return _f(self)
                cls.__abs__ = __abs__

            else:
                func_len = namespace.get("__len__")
                if callable(func_len) and zero_arg_ok(func_len):
                    def __abs__(self):
                        return len(self)
                    cls.__abs__ = __abs__

                else:
                    w_obj = namespace.get(width_name)
                    h_obj = namespace.get(height_name)
                    if (
                        callable(w_obj) and callable(h_obj)
                        and zero_arg_ok(w_obj) and zero_arg_ok(h_obj)
                    ):
                        def __abs__(self, wn=width_name, hn=height_name):
                            return getattr(self, wn)() * getattr(self, hn)()
                        cls.__abs__ = __abs__
                    else:
                        w_val = getattr(cls, width_name, None)
                        h_val = getattr(cls, height_name, None)
                        if (
                            w_val is not None and h_val is not None
                            and not callable(w_val) and not callable(h_val)
                        ):
                            def __abs__(self, wn=width_name, hn=height_name):
                                return getattr(self, wn) * getattr(self, hn)
                            cls.__abs__ = __abs__
                        else:
                        
                            def __abs__(self):
                                return "No abs"
                            cls.__abs__ = __abs__

        class AbsDescriptor:
            def __get__(self, instance, owner=None):
                if instance is None:
                    return self
                return instance.__abs__()

        cls.abs = AbsDescriptor()
        return cls
