from engine.data.constants import ALL_STAT_NAMES

class Stat:

    def __init__(self, name, val):
        self.name = name
        self.val = val

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        if not name in ALL_STAT_NAMES:
            raise ValueError("Name %s must be one of the defined stat names: %s" % (name, ALL_STAT_NAMES ))

        if not isinstance(val, int):
            raise ValueError("Val must be an integer")


    def __repr__(self):
        return "%s: %s" % (self.name, self.val)
