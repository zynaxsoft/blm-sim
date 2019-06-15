from blmsim.util.time import Clock

class DurationBuff:
    def __init__(self, name, duration):
        self.name = name
        self.duration = Clock(duration)

    def buff(self, target):
        pass

class LeyLineBuff(DurationBuff):

    def __init__(self):
        super().__init__(
                name = 'Ley Line Buff',
                duration = 30,
                )

    def buff(self, target):
        target.buffed['cast_time_ratio'] *= 0.85
        target.buffed['gcd_ratio'] *= 0.85

class SwiftcastBuff(DurationBuff):

    def __init__(self):
        super().__init__(
                name = 'Swiftcast Buff',
                duration = 10,
                )

    def buff(self, target):
        target.buffed['cast_time_ratio'] *= 0
        target.buffed['gcd_ratio'] *= 0

