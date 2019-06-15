from blmsim.util.time import Clock

class DurationBuff:
    def __init__(self, name, duration, clock):
        self.name = name
        self.duration = Clock(duration)
        self.clock = clock
        self.clock.hook(self)
        self.player = None

    def reduces_cast_time_by(self, percent):
        self.cast_time_ratio = 1-percent/100.0

    def reduces_gcd_by(self, percent):
        self.gcd_ratio = 1-percent/100.0

    def tock(self):
        self.duration.tock()
        if self.duration.is_zero():
            self.player.remove_buff(self)
            self.clock.unhook(self)
            print(f'[{self.clock}] {self.player.name} lost {self.name} buff.')

    def buff(self):
        self.player.cast_time_ratio *= self.cast_time_ratio
        self.player.gcd_ratio *= self.gcd_ratio

    def bind(self, player):
        self.player = player
        print(f'{[self.clock]} {player.name} received {self.name} buff!')
