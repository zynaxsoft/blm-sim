from blmsim.util.time import Clock, Time
from blmsim.util.skilldict import gcd, ogcd
from blmsim.buffs import *

class Skill:

    def __init__(self, name, clock, cast_time):
        self.name = name
        self.clock = clock
        self.cast_time = cast_time

    def is_ready(self):
        return self.clock.is_zero()

    def process(self, caster, target):
        pass

    def is_castable(self, caster):
        return True

    def execute(self, caster, target):
        if self.is_ready() and self.is_castable(caster):
            self.clock.reset()
            self.process(caster, target)
            return True
        return False

class GCD(Skill):

    def __init__(self, name, gcd_clock, cast_time=2.5):
        super().__init__(name, gcd_clock, cast_time)

class OGCD(Skill):

    def __init__(self, name, cooldown):
        super().__init__(name, Clock(0, default=cooldown), 0.75)

@gcd
class FireIV(GCD):

    def __init__(self, gcd_clock):
        super().__init__(
                name = 'Fire IV',
                gcd_clock = gcd_clock,
                cast_time = 2.8,
                )

    def is_castable(self, caster):
        if 'Enochian' in caster.buffs:
            return True
        return False

    def process(self, caster, target):
        pass

@gcd
class BlizzardI(GCD):

    def __init__(self, gcd_clock):
        super().__init__(
                name = 'Blizzard I',
                gcd_clock = gcd_clock,
                cast_time = 2.5,
                )

    def process(self, caster, target):
        buff = UmbralIce(1)
        caster.receive_buff(buff)

@ogcd
class Enochian(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Enochian',
                cooldown = 30,
                )

    def is_castable(self, caster):
        if 'Astral or Umbral' in caster.buffs:
            return True
        return False

    def process(self, caster, target):
        buff = EnochianBuff()
        target.receive_buff(buff)

@ogcd
class LeyLine(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Ley Line',
                cooldown = 90,
                )

    def process(self, caster, target):
        buff = LeyLineBuff()
        target.receive_buff(buff)

@ogcd
class Swiftcast(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Swiftcast',
                cooldown = 60,
                )

    def process(self, caster, target):
        buff = SwiftcastBuff()
        target.receive_buff(buff)
