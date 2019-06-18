from blmsim.util.time import Clock, Time
from blmsim.skillmeta import GCD, OGCD, gcd, ogcd
from blmsim.buffs import *

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

    def process(self):
        pass

@gcd
class BlizzardI(GCD):

    def __init__(self, gcd_clock):
        super().__init__(
                name = 'Blizzard I',
                gcd_clock = gcd_clock,
                cast_time = 2.5,
                )

    def process(self):
        buff = UmbralIce(1)
        self.caster.receive_buff(buff)

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

    def process(self):
        buff = EnochianBuff()
        self.target.receive_buff(buff)

@ogcd
class LeyLine(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Ley Line',
                cooldown = 90,
                )

    def process(self):
        buff = LeyLineBuff()
        self.target.receive_buff(buff)

@ogcd
class Swiftcast(OGCD):

    def __init__(self):
        super().__init__(
                name = 'Swiftcast',
                cooldown = 60,
                )

    def process(self):
        buff = SwiftcastBuff()
        self.target.receive_buff(buff)
