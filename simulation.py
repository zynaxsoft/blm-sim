from blmsim.util.time import Clock, Time
from blmsim.player import Player
from blmsim.util.rotation import Rotation
from blmsim.util.skillmeta import GCD_dict, OGCD_dict

clock = Clock()
player = Player('Tomoyo', clock)
rotation = Rotation(['b1', 'Enochian'], ['b1','sc','b1'])
while clock < Time(20):
    if not player.casting:
        next_skill = rotation.next()
        if next_skill in GCD_dict:
            while not player.gcd.is_zero():
                clock.tick()
            player.cast(next_skill, player)
        else:
            if player.skills[next_skill].clock.is_zero():
                player.cast(next_skill, player)
    clock.tick()
