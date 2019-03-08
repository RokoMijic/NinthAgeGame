from src.main.engine.data.statline import Statline
from engine.constants import GENERAL_AND_DEFENSIVE_STAT_NAMES

class StatlineGeneral(Statline):

    def __init__(self, statvalues):
        Statline.__init__(self, GENERAL_AND_DEFENSIVE_STAT_NAMES, statvalues)

    def __repr__(self):
        return Statline.__repr__(self)
