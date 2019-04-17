from src.main.engine.data.model import Model

import math


class Unit:
    def __init__(self, models: Model, number: int, numwide: int):

        if not number > 0: raise ValueError("number of models in a unit cannot be 0 or less")
        if not numwide <= number: raise ValueError("width (%s) must be less than or equal to the number of models (%s)" % (numwide, number))

        self.models = models
        self.number = number
        self.numfiles = numwide
        self.width_inches = self.models.basewidth*self.numfiles

        self.numfullranks = self.number // self.numfiles
        self.numsupportingfullranks = max(self.numfullranks - 1 , 0)

        self.lastranknumber = self.number % self.numfiles

        self.numranks = self.numfullranks + 0 if self.lastranknumber == 0 else 1

        self.depth_inches = self.numranks*self.models.basedepth


    def __repr__(self):
        return "\n" + str(self.number) + " x " + str(self.models.modelname) + ", " + str(self.numfiles) + " wide"


