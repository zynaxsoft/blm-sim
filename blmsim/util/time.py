import math

class Time:
    def __init__(self, time=0.0, ticks=None, tick_value=0.001):
        self.tick_value = tick_value
        if ticks is not None:
            self.ticks = ticks
        else:
            self.set_time(time)
        self.epsilon = self.tick_value / 10.0
        self.significant_order = int(-1*math.log10(self.tick_value))

    def set_time(self, time):
        self.ticks = int(math.ceil(float(time)/self.tick_value))

    def get_time(self):
        return self.ticks * self.tick_value

    def is_zero(self):
        return self.ticks == 0

    def __repr__(self):
        return f'{self.get_time():.{self.significant_order}f}'

    def __check_ticks(self, other):
        if self.tick_value != other.tick_value:
            raise TickValueError

    def __lt__(self, other):
        self.__check_ticks(other)
        return self.ticks < other.ticks

    def __gt__(self, other):
        self.__check_ticks(other)
        return self.ticks > other.ticks

    def __add__(self, other):
        self.__check_ticks(other)
        return Time(ticks=self.ticks + other.ticks)

    def __eq__(self, other):
        self.__check_ticks(other)
        return self.ticks == other.ticks

    def __sub__(self, other):
        self.__check_ticks(other)
        return Time(ticks=self.ticks - other.ticks)

class TickValueError(Exception):
    def __init__(self):
        self.message = 'Error: operating with different tick value'

class Clock(Time):
    def __init__(self, time=None, ticks=None, tick_value=0.001, default=0.0):
        if time is None:
            time = default
        super().__init__(time, ticks, tick_value)
        self.hooks = []
        self.default = default

    def tick(self):
        for h in self.hooks:
            h.tock()
        self.ticks += 1

    def tock(self):
        self.ticks = max(self.ticks-1, 0)

    def reset(self):
        self.set_time(self.default)

    def hook(self, *hook):
        self.hooks = self.hooks + list(hook)

    def unhook(self, hook):
        self.hooks.remove(hook)
