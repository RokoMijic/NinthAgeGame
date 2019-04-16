from src.main.engine.data.model import Model

import math


class Unit:
    def __init__(self, modeltype: Model, number: int, numwide: int):

        if not number > 0: raise ValueError("number of models in a unit cannot be 0 or less")
        if not numwide <= number: raise ValueError("width (%s) must be less than or equal to the number of models (%s)" % (numwide, number))

        self.modeltype = modeltype
        self.number = number
        self.numwide = numwide
        self.width_inches = self.modeltype.basewidth*self.numwide
        self.numfullranks = self.number // self.numwide
        self.lastranknumber = self.number % self.numwide
        self.numranks = self.numfullranks + 0 if self.lastranknumber == 0 else 1


    def __repr__(self):
        return "\n" + str(self.number) + " x " + str(self.modeltype.modelname) + ", " + str(self.numwide) + " wide"


