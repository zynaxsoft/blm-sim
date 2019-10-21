""" Target dummy """


class TargetDummy:

    def __init__(self):
        self.damage_taken = 0
        self.potency_taken = 0
        self.properties = {
            }

    def take_damage(self, damage):
        self.damage_taken += damage

    def take_potency(self, potency):
        self.potency_taken += potency

class TargetObserver:

    def __init__(self):
        self.dummies = []

    def eyes_on(self, dummy):
        self.dummies.append(dummy)

    def observe_total_damage_taken(self):
        total_damage = 0
        for dummy in self.dummies:
            total_damage += dummy.damage_taken
        return total_damage

    def observe_total_potency_taken(self):
        total_potency = 0
        for dummy in self.dummies:
            total_potency += dummy.potency_taken
        return total_potency
