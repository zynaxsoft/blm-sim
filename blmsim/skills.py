from blmsim.util.time import Clock, Time
from blmsim.buffs import *

class Skill:

    def __init__(self, name, clock, cast_time):
        self.name = name
        self.clock = clock
        self.cast_time = cast_time

    def is_ready(self):
        return self.clock.is_zero()

    def process(self, target):
        pass

    def execute(self, target=None):
        if self.is_ready():
            self.clock.reset()
            self.process(target)
            return True
        return False

class GCD(Skill):

    def __init__(self, name, gcd_clock, cast_time):
        super().__init__(name, gcd_clock, cast_time)

class OGCD(Skill):

    def __init__(self, name, cooldown):
        super().__init__(name, Clock(0, default=cooldown), 0.75)

class FireIV(GCD):

    def __init__(self, gcd_clock):
        super().__init__(
                name = 'Fire IV',
                gcd_clock = gcd_clock,
                cast_time = 2.8,
                )

    def process(self, target):
        print('FFIIRREE')

class LeyLine(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Ley Line',
                cooldown = 90,
                )

    def process(self, target):
        buff = LeyLineBuff()
        target.receive_buff(buff)

class SwiftCast(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Swiftcast',
                cooldown = 60,
                )

    def process(self, target):
        buff = SwiftcastBuff()
        target.receive_buff(buff)
