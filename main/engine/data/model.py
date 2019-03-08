from engine.data.statlinegeneral import StatlineGeneral
from engine.data.modelpart import ModelPart
from engine.data.constants import GENERAL_AND_DEFENSIVE_SPECIAL_RULES

class Model(StatlineGeneral):

    def __init__(self, modelname, gendefstatvalues, gendefspecialrules, modelpartname1, modelpartstatvalues1, modelpartspecialrules1):

        StatlineGeneral.__init__(self,gendefstatvalues)

        if not set(gendefspecialrules) <= set(GENERAL_AND_DEFENSIVE_SPECIAL_RULES):
            raise ValueError("At least one provided special rule is not valid: %s" % gendefspecialrules)

        self.modelname = str(modelname)
        self.specialrules = gendefspecialrules
        self.modelparts = []
        self.add_modelpart(modelpartname1, modelpartstatvalues1, modelpartspecialrules1 )


    # def __init__(self, gendefstatvalues, gendefspecialrules, modelpartstatvalues1, modelpartspecialrules1, *args):
    #
    #     if not len(args % 3 == 0): raise ValueError("wrong number of arguments")
    #
    #     self.__init__(gendefstatvalues, gendefspecialrules, modelpartstatvalues1, modelpartspecialrules1)
    #     self.add_modelpart()
    #  TODO: finish this


    def add_modelpart(self, modelpartname, modelpartstatvalues, modelpartspecialrules):
        self.modelparts.append(ModelPart(modelpartname, modelpartstatvalues,modelpartspecialrules))

    def __repr__(self):
        return "\n" + str(self.modelname) + "\n" + StatlineGeneral.__repr__(self) + "  |  " + ", ".join(self.specialrules) + "\n" +  "\n".join( [str(mp) for mp in self.modelparts ] )

