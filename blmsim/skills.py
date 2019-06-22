""" skills related classes """
from blmsim import skillmeta, buffs

@skillmeta.gcd
class FireIV(skillmeta.GCD, skillmeta.DamageSkill):

    def __init__(self, gcd_clock):
        super().__init__(
            name='Fire IV',
            gcd_clock=gcd_clock,
            cast_time=2.8,
            )

    def is_castable(self, caster):
        if 'Enochian' in caster.buffs:
            return True
        return False

    def process(self):
        self.do_damage(300)

@skillmeta.gcd
class BlizzardI(skillmeta.GCD, skillmeta.DamageSkill):

    def __init__(self, gcd_clock):
        super().__init__(
            name='Blizzard I',
            gcd_clock=gcd_clock,
            cast_time=2.5,
            )

    def process(self):
        buff = buffs.UmbralIce(1)
        self.caster.receive_buff(buff)
        self.do_damage(120)

@skillmeta.ogcd
class Enochian(skillmeta.OGCD, skillmeta.BuffSkill):

    def __init__(self):
        super().__init__(
            name='Enochian',
            cooldown=30,
            )

    def is_castable(self, caster):
        if 'Astral or Umbral' in caster.buffs:
            return True
        return False

    def process(self):
        buff = buffs.EnochianBuff()
        self.give_buffs(buff)

@skillmeta.ogcd
class LeyLine(skillmeta.OGCD, skillmeta.BuffSkill):

    def __init__(self):
        super().__init__(
            name='Ley Line',
            cooldown=90,
            )

    def process(self):
        buff = buffs.LeyLineBuff()
        self.give_buffs(buff)

@skillmeta.ogcd
class Swiftcast(skillmeta.OGCD, skillmeta.BuffSkill):

    def __init__(self):
        super().__init__(
            name='Swiftcast',
            cooldown=60,
            )

    def process(self):
        buff = buffs.SwiftcastBuff()
        self.give_buffs(buff)
