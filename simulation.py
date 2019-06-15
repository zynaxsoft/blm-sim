from blmsim.util.time import Clock, Time
from blmsim.player import Player
from blmsim.util.rotation import Rotation

clock = Clock()
player = Player('Tomoyo', clock)
rotation = Rotation(['b1', 'Enochian'], ['b1','sc','b1'])
while clock < Time(20):
    if not player.casting:
        player.cast(rotation.next(), player)
    clock.tick()
