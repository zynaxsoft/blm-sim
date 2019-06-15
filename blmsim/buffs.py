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

