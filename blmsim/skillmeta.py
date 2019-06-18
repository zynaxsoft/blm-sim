""" Meta for creating skills """
from blmsim.util.time import Clock

GCD_DICT = {}
OGCD_DICT = {}

def gcd(cls):
    GCD_DICT.update({cls(None).name: cls})
    return cls

def ogcd(cls):
    OGCD_DICT.update({cls().name: cls})
    return cls

class Skill:

    def __init__(self, name, clock, cast_time, skill_type=''):
        self.name = name
        self.clock = clock
        self.properties = {
            'type': skill_type,
            'caster': None,
            'target': None,
            'cast_time': cast_time,
            }

    def is_ready(self):
        return self.clock.is_zero()

    def process(self):
        pass

    def get_type(self):
        return self.properties['type']

    def is_castable(self, caster):
        return True

    def execute(self, caster, target):
        if self.is_ready() and self.is_castable(caster):
            self.caster = caster
            self.target = target
            self.clock.reset()
            return True
        return False

    def __bool__(self):
        return True

    def __str__(self):
        return self.name

class GCD(Skill):

    def __init__(self, name, gcd_clock, cast_time=2.5):
        super().__init__(name, gcd_clock, cast_time, skill_type='gcd')

class OGCD(Skill):

    def __init__(self, name, cooldown):
        super().__init__(name, Clock(0, default=cooldown), 0.75, skill_type='ogcd')

    def execute(self, caster, target):
        executed = super().execute(caster, target)
        if executed:
            self.process()
        return executed
