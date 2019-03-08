from engine.data.statlineoffensive import StatlineOffensive
from engine.data.constants import OFFENSIVE_SPECIAL_RULES


class ModelPart(StatlineOffensive):

    def __init__(self, modelpartname, statvalues, specialrules):
        StatlineOffensive.__init__(self, statvalues)

        if not set(specialrules) <= set(OFFENSIVE_SPECIAL_RULES):
            raise ValueError("At least one provided special rule is not valid: %s" % specialrules)

        self.specialrules = specialrules
        self.modelpartname = modelpartname

    def __repr__(self):
        return str(self.modelpartname) + "  |  " + StatlineOffensive.__repr__(self)  + "  |  " + ", ".join(self.specialrules)