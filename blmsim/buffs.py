from blmsim.util.time import Clock
from blmsim.util.skilldict import GCD_dict, OGCD_dict

class DurationBuff:

    def __init__(self, name, duration):
        self.name = name
        self.duration = Clock(duration)

    def is_exhausted(self):
        return self.duration.is_zero()

    def buff(self, target):
        pass

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

    def deduct_charge_for_skill(self, skill_name):
        pass

    def gain_charge(self):
        self.charge = min(self.charge_limit, self.charge+1)

    def deduct_charge(self):
        self.charge = max(0, self.charge-1)

    def is_exhausted(self):
        if self.charge <= 0:
            return True
        return super().is_exhausted()

class EnochianBuff(DurationBuff):

    def __init__(self):
        super().__init__(
                name = 'Enochian',
                duration = 0,
                )
        self.exhausted = False

    def is_exhausted(self):
        return self.exhausted

    def buff(self, target):
        pass

class AstralUmbral(DurationBuff):

    def __init__(self, name, stack):
        super().__init__(
                name,
                duration = 15,
                )
        self.stack = stack
        self.max_stack = 3

    def gain_stack(self):
        self.stack = min(self.max_stack, self.stack+1)

    def buff(self, target):
        pass

    def __eq__(self, other):
        compare = str(self.name) == str(other)
        compare = compare or 'Astral or Umbral' == str(other)
        compare = compare or f"{self.name} {self.stack}" == str(other)
        return compare

class AstralFire(AstralUmbral):

    def __init__(self, stack):
        super().__init__('Astral Fire', stack)
        self.stack = stack

    def buff(self, target):
        pass

class UmbralIce(AstralUmbral):

    def __init__(self, stack):
        super().__init__('Umbral Ice', stack)
        self.stack = stack

    def buff(self, target):
        pass

class LeyLineBuff(DurationBuff):

    def __init__(self):
        super().__init__(
                name = 'Ley Line Buff',
                duration = 30,
                )

    def buff(self, target):
        target.buffed['cast_time_multiplier'] *= 0.85
        target.buffed['gcd'] *= 0.85

class SwiftcastBuff(ChargeBuff):

    def __init__(self):
        super().__init__(
                name = 'Swiftcast Buff',
                duration = 10,
                charge = 1,
                )

    def deduct_charge_for_skill(self, skill_name):
        if skill_name in GCD_dict:
            self.deduct_charge()
            return True
        return False

    def buff(self, target):
        target.buffed['cast_time_multiplier'] *= 0

