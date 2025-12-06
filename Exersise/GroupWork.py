import asyncio

class Loop:
    wrappers = []
    n = 0
    current = 0
    stop = False

    def __call__(self, func):
        idx = len(Loop.wrappers)

        async def wrapper(*args, **kwargs):
            while True:
                while True:
                    if Loop.stop:
                        return None
                    if Loop.current == idx:
                        break
                    await asyncio.sleep(0)

                if Loop.stop:
                    return None

                res = await func(*args, **kwargs)

                if res is None:
                    Loop.stop = True
                    Loop.current = (Loop.current + 1) % Loop.n
                    return None
                else:
                    Loop.current = (Loop.current + 1) % Loop.n

        Loop.wrappers.append(wrapper)
        Loop.n = len(Loop.wrappers)
        return wrapper