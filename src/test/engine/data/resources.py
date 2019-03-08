from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart


# Test models

swordmodelpart = ModelPart("swordattack", [1, 3, 3, 0, 3], ["HATRED"])
swordsmanmodel = Model("swordsman", [4, 8, 7, 1, 3, 3, 0],  ["PARRY"], [ModelPart("swordattack", [1, 3, 3, 0, 3], ["HATRED"])] )

zombiemodelpart = ModelPart("zombieslap", [1, 1, 3, 0, 2], ["POISON"])
zombiemodel = Model("zombie", [4, 8, 7, 1, 1, 4, 0],  ["FEARLESS"], [ModelPart("zombieslap", [1, 1, 3, 0, 2], ["POISON"])] )

