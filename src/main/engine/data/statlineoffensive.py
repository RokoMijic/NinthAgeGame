from engine.data.statline import Statline as Statline
from engine.data.constants import OFFENSIVE_STAT_NAMES

class StatlineOffensive(Statline):

    def __init__(self, statvalues):
        Statline.__init__(self, OFFENSIVE_STAT_NAMES, statvalues)