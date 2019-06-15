from blmsim.util.time import Clock, Time
from blmsim.player import Player

clock = Clock()
player = Player('Tomoyo', clock)
while clock < Time(20):
    player.cast('Fire IV')
    clock.tick()
