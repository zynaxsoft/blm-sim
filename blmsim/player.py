from blmsim.util.time import Clock, Time
from blmsim.buffs import DurationBuff
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
        # stats
        self.base = {
                'cast_time_ratio': 1,
                'gcd_ratio': 1,
                }
        self.buffed = dict(self.base)
        self.buffs = []
        # skills
        self.skills = {
                'Fire IV': FireIV(self.gcd)
                }
        self.on_cd_ogcds = []

    def cast(self, skill_name):
        skill = self.skills[skill_name]
        if isinstance(skill, OGCD):
            self.on_cd_ogcds.append(skill)
        if not self.casting:
            self.casting = skill_name
            self.me(f"begins to cast {self.casting}.")
            self.casting_time.set_time(skill.cast_time)
            return skill.execute()
        return False

    def on_casted(self):
        self.me(f"casted {self.casting} !")
        self.casting = ''

    def tock(self):
        if self.casting_time.is_zero():
            self.on_casted()
        for ogcd in self.on_cd_ogcds:
            if ogcd.clock.is_zero():
                self.on_cd_ogcds.remove(ogcd)
            ogcd.clock.tock()
        for buff in self.buffs:
            if buff.duration.is_zero():
                self.remove_buff(buff)
        self.gcd.tock()
        self.casting_time.tock()

    def receive_buff(self, buff):
        self.me(f"received {buff.name} !")
        for b in self.buffs:
            if isinstance(b, type(buff)):
                self.me(f"already has {b.name}. The buff's duration is renewed")
                self.buffs.remove(b)
        self.buffs.append(buff)
        self.apply_buffs()

    def remove_buff(self, buff):
        self.buffs.remove(buff)
        self.apply_buffs()

    def apply_buffs(self):
        self.buffed = dict(self.base)
        for b in self.buffs:
            b.buff(self)

    def me(self, text):
        print(f"[{self.clock}] {self.name} {text}")
