""" BLM Simulation """
from blmsim.player import Player
from blmsim.util.rotation import Rotation
from blmsim.util.time import Clock, Time


def main():
    """ main """
    clock = Clock()
    player = Player('Tomoyo', clock)
    rotation = Rotation(['b1', 'Enochian'], ['b1', 'sc', 'b1'])
    while clock < Time(20):
        if not player.casting:
            next_skill = player.skills[rotation.next()]
            if next_skill.properties['type'] == 'gcd':
                while not player.gcd.is_zero():
                    clock.tick()
                player.cast(next_skill.name, player)
            else:
                if next_skill.clock.is_zero():
                    player.cast(next_skill.name, player)
        clock.tick()


if __name__ == '__main__':
    main()
