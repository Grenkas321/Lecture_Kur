class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed = ()):
        if allowed is None:
            allowed_types = ()
        else:
            types = []
            for a in allowed:
                if isinstance(a, type) and issubclass(a, BaseException):
                    types.append(a)
                else:
                    types.append(type(a))
            allowed_types = tuple(types)

        had_exc = False
        had_unallowed = False

        for item in suite:
            try:
                self.fun(*item)
            except Exception as e:
                had_exc = True
                if not isinstance(e, allowed_types):
                    had_unallowed = True
        
        if not had_exc:
            return 0
        return 1 if had_unallowed else -1