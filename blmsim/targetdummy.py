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

class DummyObserver:

    def __init__(self):
        self.dummies = []

    def eyes_on(self, dummy):
        self.dummies.append(dummy)

    def observe_damage_taken(self):
        for dummy in self.dummies:
            print(dummy.damage_taken)

    def observe_potency_taken(self):
        for dummy in self.dummies:
            print(dummy.potency_taken)
