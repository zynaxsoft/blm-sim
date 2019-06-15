from blmsim.util.time import Clock, Time
from blmsim.buff import DurationBuff
from blmsim.skills import *

class Player:
    def __init__(self, name, clock):
        self.name = name
        # cooldown attribute
        self.base_gcd = 2.5
        self.gcd = Clock(0, default=self.base_gcd)
        self.casting_time = Clock(0)
        self.casting = ''
        self.clock = clock
        self.clock.hook(self)
        # buffs
        self.buffs = []
        self.cast_time_ratio = 1
        self.gcd_ratio = 1
        # skills
        self.skills = {
                'FireIV': FireIV(self.gcd)
                }

    def cast(self, skill_name):
        skill = self.skills[skill_name]
        if not self.casting:
            self.casting = skill_name
            print(f"[{self.clock}] {self.name} begins to cast {self.casting}.")
            self.casting_time.set_time(skill.cast_time)
            return skill.execute()
        return False

    def on_casted(self):
        print(f"[{self.clock}] {self.name} casted {self.casting} !")

    def tock(self):
        self.gcd.tock()
        self.casting_time.tock()
        if casting_time.is_zero():
            self.on_casted()

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

    def leyline(self):
        buff = DurationBuff('Leyline', 5, self.clock)
        buff.reduces_cast_time_by(15)
        buff.reduces_gcd_by(15)
        self.receive_buff(buff)

    def swiftcast(self):
        buff = DurationBuff('Swiftcast', 10, self.clock)
        buff.reduces_cast_time_by(100)
        self.receive_buff(buff)
