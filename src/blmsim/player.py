from blmsim.util.time import Clock, Time
from blmsim.buff import DurationBuff

class Player:
    def __init__(self, name, clock):
        self.name = name
        # cooldown attribute
        self.base_gcd = 2.5
        self.gcd = Clock(0)
        self.casting_time = Clock(0)
        self.casting = False
        self.clock = clock
        clock.hook(self)
        # buffs
        self.buffs = []
        self.cast_time_ratio = 1
        self.gcd_ratio = 1

    def gcd(skill_name):
        def gcdd(func):
            def decorated(self):
                message = 'what'
                if self.gcd+self.casting_time == Time(0) and not self.casting:
                    print(f'[{self.clock}]: {self.name} begins to cast {skill_name}!')
                    self.casting = True
                    func(self)
                elif self.casting_time == Time(0) and self.casting:
                    print(f'[{self.clock}]: {self.name} casted {skill_name}!')
                    self.casting = False

            return decorated
        return gcdd

    def receive_buff(self, *buff):
        for b in buff:
            b.bind(self)
            self.buffs.append(b)
        self.apply_buffs()

    def remove_buff(self, buff):
        self.buffs.remove(buff)
        self.apply_buffs()

    def apply_buffs(self):
        for b in self.buffs:
            b.buff()

    def tock(self):
        self.gcd.tock()
        self.casting_time.tock()

    @gcd('Fire IV')
    def fire4(self):
        cast_time = 2.8 * self.cast_time_ratio
        gcd = self.base_gcd * self.gcd_ratio
        self.casting_time.set_time(cast_time)
        self.gcd.set_time(gcd)

    def leyline(self):
        buff = DurationBuff('Leyline', 5, self.clock)
        buff.reduces_cast_time_by(15)
        buff.reduces_gcd_by(15)
        self.receive_buff(buff)

    def swiftcast(self):
        buff = DurationBuff('Swiftcast', 10, self.clock)
        buff.reduces_cast_time_by(100)
        self.receive_buff(buff)
