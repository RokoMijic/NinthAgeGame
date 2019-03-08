from engine.data.constants import OFFENSIVE_STAT_NAMES, GENERAL_AND_DEFENSIVE_STAT_NAMES
from engine.data.stat import Stat

class Statline:

    def __init__(self, statnames,  statvalues):

        if not len(statvalues) == len(statnames):
            raise ValueError("Length of stat values (%s) doesn't match length of stat names (%s)" % (statvalues , statnames ))

        self.statnames = statnames
        self.statvalues = statvalues
        self.stats = [ Stat(n,v) for (n,v) in zip(self.statnames, self.statvalues )]


    def v(self, statname):

        if not statname in self.statnames:
            raise ValueError("(%s) not found in the stats here (%s)" % (statname , self.statnames ))

        return [x.val for x in self.stats if x.name == statname][0]



    def __repr__(self):

        return "   ".join([ str(s) for s in self.stats ])



