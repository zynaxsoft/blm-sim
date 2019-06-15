from blmsim.util.time import Clock, Time
from blmsim.buffs import DurationBuff
from blmsim.skills import *
from blmsim.util.skilldict import GCD_dict, OGCD_dict

class Player:
    def __init__(self, name, clock):
        self.name = name
        # stats
        self.base = {
                'gcd': 2.5,
                'cast_time_multiplier': 1,
                }
        self.buffed = dict(self.base)
        self.buffs = []
        # cooldown attribute
        self.gcd = Clock(0, default=self.base['gcd'])
        self.casting_time = Clock(0)
        self.casting = ''
        self.clock = clock
        self.clock.hook(self)
        # skills
        self.skills = {}
        for k, v in GCD_dict.items():
            self.skills[k] = v(self.gcd)
        for k, v in OGCD_dict.items():
            self.skills[k] = v()
        self.on_cd_ogcds = []
        self.charge_buffs = []

    def calc_cast_time(self, cast_time):
        return cast_time*self.buffed['cast_time_multiplier']

    def cast(self, skill_name, target=None):
        skill = self.skills[skill_name]
        if not self.casting:
            self.casting = skill_name
            if isinstance(skill, OGCD):
                self.on_cd_ogcds.append(skill)
            self.me(f"begins to cast {self.casting}.")
            self.casting_time.set_time(self.calc_cast_time(skill.cast_time))
            self.gcd.default = self.buffed['gcd']
            return skill.execute(target)
        return False

    def on_casted(self):
        self.me(f"casted {self.casting} !")
        if len(self.charge_buffs) > 0:
            for buff in self.charge_buffs:
                if buff.deduct_charge_for_skill(self.casting):
                    if buff.is_exhausted():
                        self.remove_buff(buff)
                    break
        if self.casting in GCD_dict:
            self.gcd.reset()
        self.casting = ''

    def tock(self):
        for ogcd in self.on_cd_ogcds:
            if ogcd.clock.is_zero():
                self.on_cd_ogcds.remove(ogcd)
            ogcd.clock.tock()
        for buff in self.buffs:
            if buff.is_exhausted():
                self.remove_buff(buff)
        if self.casting_time.is_zero() and self.casting:
            self.on_casted()
        self.gcd.tock()
        self.casting_time.tock()

    def receive_buff(self, buff):
        self.me(f"received {buff.name} !")
        if isinstance(buff, ChargeBuff):
            self.charge_buffs.append(buff)
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
