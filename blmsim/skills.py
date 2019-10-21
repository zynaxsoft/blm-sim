""" skills related classes """
from blmsim import skillmeta, buffs

@skillmeta.gcd
class FireIV(skillmeta.GCD):

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
        skillmeta.do_damage(self, 300)

@skillmeta.gcd
class Foul(skillmeta.GCD):

    def __init__(self, gcd_clock):
        super().__init__(
            name='Foul',
            gcd_clock=gcd_clock,
            )

    def is_castable(self, caster):
        if 'Polyglot' in caster.buffs:
            if caster.buffs['Polyglot'].charge > 0:
                return True
        return False

    def process(self):
        skillmeta.do_damage(self, 500)

@skillmeta.gcd
class BlizzardI(skillmeta.GCD):

    def __init__(self, gcd_clock):
        super().__init__(
            name='Blizzard I',
            gcd_clock=gcd_clock,
            )

    def process(self):
        self.caster.receive_buff(buffs.UmbralIceBuff(1))
        skillmeta.do_damage(self, 120)


@skillmeta.ogcd
class Enochian(skillmeta.OGCD):

    def __init__(self):
        super().__init__(
            name='Enochian',
            cooldown=30,
            )

    def is_castable(self, caster):
        if 'Astral or Umbral' in caster.buffs.values():
            return True
        return False

    def process(self):
        self.caster.receive_buff(buffs.EnochianBuff())
        self.caster.receive_buff(buffs.PolyglotBuff())

@skillmeta.ogcd
class LeyLine(skillmeta.OGCD):

    def __init__(self):
        super().__init__(
            name='Ley Line',
            cooldown=90,
            )

    def process(self):
        self.caster.receive_buff(buffs.LeyLineBuff())

@skillmeta.ogcd
class Swiftcast(skillmeta.OGCD):

    def __init__(self):
        super().__init__(
            name='Swiftcast',
            cooldown=60,
            )

    def process(self):
        self.caster.receive_buff(buffs.SwiftcastBuff())

