from src.main.engine.data.model import Model

class Unit:
    def __init__(self, modeltype: Model, number: int, width: int):

        if not number > 0: raise ValueError("number of models in a unit cannot be 0 or less")
        if not width <= number: raise ValueError("width (%s) must be less than or equal to the number of models (%s)" % (width, number))

        self.modeltype = modeltype
        self.number = number
        self.width = width

    def __repr__(self):
        return "\n" + str(self.number) + " x " + str(self.modeltype.modelname) + ", " + str(self.width) + " wide"


