import itertools

class Rotation:

    def __init__(self, opener=None, rotation=None):
        if opener is None:
            opener = []
        self.shorthand_dict = {
                'b1': 'Blizzard I',
                'f4': 'Fire IV',
                'sc': 'Swiftcast',
                }
        for i, s in enumerate(opener):
            opener[i] = self.shorthand_dict.get(s, s)
        for i, s in enumerate(rotation):
            rotation[i] = self.shorthand_dict.get(s, s)
        self.opener = opener
        self.rotation = rotation
        self.iterator = iter(self)

    def next(self):
        return next(self.iterator)

    def __iter__(self):
        return itertools.chain(self.opener, itertools.cycle(self.rotation))
