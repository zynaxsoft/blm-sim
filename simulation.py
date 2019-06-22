""" BLM Simulation """
from blmsim.player import Player
from blmsim.skillmeta import GCD_DICT
from blmsim.util.rotation import Rotation
from blmsim.util.time import Clock, Time


def main():
    """ main """
    clock = Clock()
    player = Player('Tomoyo', clock)
    rotation = Rotation(['b1', 'Enochian'], ['b1', 'sc', 'b1'])
    while clock < Time(20):
        if not player.casting:
            next_skill = rotation.next()
            if next_skill in GCD_DICT:
                while not player.gcd.is_zero():
                    clock.tick()
                player.cast(next_skill, player)
            else:
                if player.skills[next_skill].clock.is_zero():
                    player.cast(next_skill, player)
        clock.tick()


if __name__ == '__main__':
    main()
