""" Player related stuffs """
from blmsim import skills
from blmsim import skillmeta
from blmsim import buffs
from blmsim.util.time import Clock
from blmsim.util.logging import BLMLOG

class Player:
    """ Player class """
    def __init__(self, name, clock):
        self.name = name
        # stats
        self.base = {
            'gcd': 2.5,
            'cast_time_multiplier': 1,
            'damage_modifier': 1,
            }
        self.buffed = dict(self.base)
        self.buffs = {}
        self.charge_buffs = []
        # cooldown attribute
        self.gcd = Clock(0, default=self.base['gcd'])
        self.casting_time = Clock(0)
        self.casting = False
        self.clock = clock
        self.clock.hook(self)
        # skills
        self.skills = {}
        for k, skill in skillmeta.GCD_DICT.items():
            self.skills[k] = skill(self.gcd)
        for k, skill in skillmeta.OGCD_DICT.items():
            self.skills[k] = skill()
        self.on_cd_ogcds = []

    def calc_cast_time(self, cast_time):
        return cast_time*self.buffed['cast_time_multiplier']

    def cast(self, skill_name, target=None):
        skill = self.skills[skill_name]
        if not self.casting and skill.is_ready():
            self.casting = skill
            if isinstance(skill, skillmeta.OGCD):
                self.on_cd_ogcds.append(skill)
            BLMLOG.info("-----------------------")
            self.me(f"begins to cast {self.casting}.")
            self.casting_time.set_time(
                self.calc_cast_time(skill.cast_time))
            self.gcd.default = self.buffed['gcd']
            return skill.execute(self, target)
        print(f"[{self.clock}] {skill} is not yet ready !!")
        return False

    def on_casted(self):
        self.me(f"casted {self.casting} !")
        if isinstance(self.casting, skillmeta.GCD):
            self.casting.process()
        if self.charge_buffs:
            for buff in self.charge_buffs:
                if buff.deduct_charge_for_skill(self.casting):
                    self.me(f'loses 1 charge of {buff}')
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
        for buff in list(self.buffs.values()):
            if buff.is_exhausted():
                self.remove_buff(buff)
            buff.duration.tock()
        self.check_enochian()
        if self.casting_time.is_zero() and self.casting:
            self.on_casted()
        self.gcd.tock()
        self.casting_time.tock()

    def receive_buff(self, buff):
        if isinstance(buff, buffs.ChargeBuff):
            self.charge_buffs.append(buff)
        if buff.name in self.buffs:
            self.buffs[buff.name].renew(buff)
            buff = self.buffs[buff.name]
        else:
            self.buffs[buff.name] = buff
        self.apply_buffs()
        self.me(f"received {buff} !")

    def check_enochian(self):
        if 'Enochian' in self.buffs:
            if 'Polyglot' in self.buffs:
                polyglot = self.buffs['Polyglot']
                if polyglot.gain_charge_timer.is_zero():
                    polyglot.gain_charge()
                    polyglot.gain_charge_timer.reset()
                else:
                    polyglot.gain_charge_timer.tock()
            if 'Astral or Umbral' in self.buffs.values():
                return True
            self.buffs.pop('Enochian')
        return False

    def remove_buff(self, buff):
        self.me(f"loses {buff}.")
        self.buffs.pop(buff.name)
        self.apply_buffs()

    def apply_buffs(self):
        self.buffed = dict(self.base)
        for current_buff in self.buffs.values():
            current_buff.buff(self)

    def me(self, text):
        BLMLOG.info(f"[{self.clock}] {self.name} {text}")
