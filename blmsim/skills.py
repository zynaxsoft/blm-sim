from blmsim.util.time import Clock, Time

class Skill:

    def __init__(self, name, clock, cast_time):
        self.name = name
        self.clock = clock
        self.cast_time = cast_time

    def is_ready(self):
        return self.clock.is_zero()

    def execute(self):
        if self.is_ready():
            self.clock.reset()
            return True
        return False

class GCD(Skill):

    def __init__(self, name, gcd_clock, cast_time):
        super().__init__(name, gcd_clock, cast_time)

class OGCD(Skill):

    def __init__(self, name, cooldown):
        super().__init__(name, Clock(default=cooldown))
        self.cast_time = 0.75

class FireIV(GCD):

    def __init__(self, gcd_clock):
        super().__init__(
                'FireIV',
                gcd_clock,
                cast_time=2.8,
                )

    def execute(self):
        return super().execute()
