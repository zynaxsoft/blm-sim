""" Buff related classes """
from blmsim.util.time import Clock
from blmsim import skillmeta

class DurationBuff:

    def __init__(self, name, duration):
        self.name = name
        self.duration = Clock(default=duration)

    def is_exhausted(self):
        return self.duration.is_zero()

    def buff(self, target):
        pass

    def renew(self, new):
        self.duration.reset()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

class ChargeBuff(DurationBuff):

    def __init__(self, name, duration, charge, charge_limit=0):
        super().__init__(name, duration)
        self.charge = charge
        self.charge_limit = charge_limit
        self.skills_that_reduces_charge = []

    def deduct_charge_for_skill(self, skill):
        if skill.name in self.skills_that_reduces_charge:
            self.deduct_charge()
            return True
        return False

    def gain_charge(self):
        self.charge = min(self.charge_limit, self.charge+1)

    def renew(self, new):
        super().renew(new)
        self.charge = new.charge

    def deduct_charge(self):
        self.charge = max(0, self.charge-1)

    def is_exhausted(self):
        if self.charge <= 0:
            return True
        return super().is_exhausted()

class EnochianBuff(DurationBuff):

    def __init__(self):
        super().__init__(
            name='Enochian',
            duration=0,
            )
        self.exhausted = False

    def is_exhausted(self):
        return self.exhausted

    def buff(self, target):
        pass

class PolyglotBuff(ChargeBuff):

    def __init__(self):
        super().__init__(
            name='Polyglot',
            duration=0,
            charge=0,
            charge_limit=1,
            )
        self.exhausted = False
        self.gain_charge_timer = Clock(default=30)
        self.skills_that_reduces_charge = ['Foul']

    def is_exhausted(self):
        return self.exhausted

    def renew(self, new):
        pass

class AstralUmbralBuff(DurationBuff):

    def __init__(self, name, stack):
        super().__init__(
            name,
            duration=15,
            )
        self.stack = stack
        self.max_stack = 3

    def renew(self, new):
        super().renew(new)
        self.stack = min(self.max_stack, self.stack+1)

    def buff(self, target):
        pass

    def __str__(self):
        return f"{self.name} {'I'*self.stack}"

    def __eq__(self, other):
        compare = str(other) == self.name
        compare = compare or str(other) == str(self)
        compare = compare or str(other) == 'Astral or Umbral'
        return compare

class AstralFireBuff(AstralUmbralBuff):

    def __init__(self, stack):
        super().__init__('Astral Fire', stack)

    def buff(self, target):
        pass

class UmbralIceBuff(AstralUmbralBuff):

    def __init__(self, stack):
        super().__init__('Umbral Ice', stack)

    def buff(self, target):
        pass

class LeyLineBuff(DurationBuff):

    def __init__(self):
        super().__init__(
            name='Ley Line Buff',
            duration=30,
            )

    def buff(self, target):
        target.buffed['cast_time_multiplier'] *= 0.85
        target.buffed['gcd'] *= 0.85

class SwiftcastBuff(ChargeBuff):

    def __init__(self):
        super().__init__(
            name='Swiftcast Buff',
            duration=10,
            charge=1,
            )
        self.skills_that_reduces_charge = list(skillmeta.GCD_DICT)

    def buff(self, target):
        target.buffed['cast_time_multiplier'] *= 0
