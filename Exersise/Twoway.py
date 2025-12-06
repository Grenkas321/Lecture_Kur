import asyncio


class Portal:
    def __init__(self, parties: int):
        self.parties = parties
        self.entered = 0
        self.exited = 0
        self.gen = 0
        self.cond = asyncio.Condition()
        self.pending_topic = None
        self.gen_topics = {}
        self.task_gen = {}

    @property
    def topic(self):
        task = asyncio.current_task()
        if task is None:
            return None
        g = self.task_gen.get(task)
        if g is None:
            return None
        return self.gen_topics.get(g)

    async def wait(self, topic=None):
        async with self.cond:
            while self.entered == self.parties:
                await self.cond.wait()
            my_gen = self.gen
            if topic is not None:
                self.pending_topic = topic
            self.entered += 1
            if self.entered == self.parties:
                self.gen_topics[my_gen] = self.pending_topic
                self.pending_topic = None
                self.exited = 0
                self.cond.notify_all()
            else:
                while self.entered < self.parties:
                    await self.cond.wait()
        async with self.cond:
            self.exited += 1
            if self.exited == self.parties:
                self.entered = 0
                self.gen += 1
                self.cond.notify_all()
        task = asyncio.current_task()
        if task is not None:
            self.task_gen[task] = my_gen
