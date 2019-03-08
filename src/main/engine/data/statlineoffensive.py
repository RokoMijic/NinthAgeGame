from src.main.engine.data.statline import Statline
from engine.constants import OFFENSIVE_STAT_NAMES

class StatlineOffensive(Statline):

    def __init__(self, statvalues):
        Statline.__init__(self, OFFENSIVE_STAT_NAMES, statvalues)