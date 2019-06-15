from blmsim.util.time import Clock, Time
from blmsim.player import Player

clock = Clock(tick_value=0.001)
player = Player('Tomoyo', clock)
while clock < Time(20):
    player.cast('FireIV')
    clock.tick()
