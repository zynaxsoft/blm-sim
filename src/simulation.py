from blmsim.util.time import Clock, Time
from blmsim.player import Player

clock = Clock()
player = Player('Tomoyo', clock)
player.leyline()
while clock < Time(20):
#   if not player.casting:
    player.fire4()
    clock.tick()
