from blmsim.util.time import Clock, Time
from blmsim.skills import *
from blmsim.util.skillmeta import GCD_dict, OGCD_dict

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
        self.charge_buffs = []
        # cooldown attribute
        self.gcd = Clock(0, default=self.base['gcd'])
        self.casting_time = Clock(0)
        self.casting = False
        self.clock = clock
        self.clock.hook(self)
        # skills
        self.skills = {}
        for k, v in GCD_dict.items():
            self.skills[k] = v(self.gcd)
        for k, v in OGCD_dict.items():
            self.skills[k] = v()
        self.on_cd_ogcds = []

    def calc_cast_time(self, cast_time):
        return cast_time*self.buffed['cast_time_multiplier']

    def cast(self, skill_name, target=None):
        skill = self.skills[skill_name]
        if not self.casting and skill.is_ready():
            self.casting = skill
            if isinstance(skill, OGCD):
                self.on_cd_ogcds.append(skill)
            print("-----------------------")
            self.me(f"begins to cast {self.casting}.")
            self.casting_time.set_time(self.calc_cast_time(skill.cast_time))
            self.gcd.default = self.buffed['gcd']
            return skill.execute(self, target)
        return False

    def on_casted(self):
        self.me(f"casted {self.casting} !")
        if isinstance(self.casting, GCD):
            self.casting.process()
        if len(self.charge_buffs) > 0:
            for buff in self.charge_buffs:
                if buff.deduct_charge_for_skill(self.casting):
                    if buff.is_exhausted():
                        self.charge_buffs.remove(buff)
                        self.remove_buff(buff)
                    break
        self.casting = False

    def tock(self):
        for ogcd in self.on_cd_ogcds:
            if ogcd.clock.is_zero():
                self.on_cd_ogcds.remove(ogcd)
            ogcd.clock.tock()
        for buff in self.buffs:
            if buff.is_exhausted():
                self.remove_buff(buff)
            buff.duration.tock()
        self.check_enochian()
        if self.casting_time.is_zero() and self.casting:
            self.on_casted()
        self.gcd.tock()
        self.casting_time.tock()

    def receive_buff(self, buff):
        self.me(f"received {buff} !")
        if isinstance(buff, ChargeBuff):
            self.charge_buffs.append(buff)
        for b in self.buffs:
            if isinstance(b, type(buff)):
                self.me(f"already has {b.name}. The buff's duration is renewed")
                self.buffs.remove(b)
        self.buffs.append(buff)
        self.apply_buffs()

    def check_enochian(self):
        if 'Enochian' in self.buffs:
            if 'Astral or Umbral' in self.buffs:
                return True
            self.buffs.remove('Enochian')
        return False

    def remove_buff(self, buff):
        self.buffs.remove(buff)
        self.apply_buffs()

    def apply_buffs(self):
        self.buffed = dict(self.base)
        for b in self.buffs:
            b.buff(self)

    def me(self, text):
        print(f"[{self.clock}] {self.name} {text}")
