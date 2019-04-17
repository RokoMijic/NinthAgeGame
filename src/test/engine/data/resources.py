from src.main.engine.data.unit import Unit
from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart


# Test models

# GENERAL_STAT_NAMES = ["Adv", "Mar", "Dis"]
# DEFENSIVE_STAT_NAMES = ["HP", "Def", "Res", "Arm"]
# OFFENSIVE_STAT_NAMES = [ "Att", "Off", "Str", "AP", "Agi" ]

swordmodelpart = ModelPart("swordattack", [1, 3, 3, 0, 3], ["HATRED"])
swordsmanmodel = Model("swordsman", 0.8, 0.8, "INFANTRY", "STANDARD", [4, 8, 7, 1, 3, 3, 2],  ["PARRY"], [ swordmodelpart ] )

zombiemodelpart = ModelPart("zombieslap", [1, 1, 3, 0, 1], ["POISON"])
zombiemodel = Model("zombie", 0.8, 0.8, "INFANTRY", "STANDARD", [4, 8, 7, 1, 1, 4, 0],  ["FEARLESS"], [ zombiemodelpart ] )

knightmodelpart = ModelPart("knightattck", [1, 4, 4, 1, 4],[])
horsemodelpart = ModelPart("horsekick", [1, 3, 3, 0, 3], ["HARNESSED"])
knightmodel = Model("knight", 1,2, "CAVALRY", "STANDARD" , [8, 16, 8, 1, 4, 3, 5],  [], [ knightmodelpart , horsemodelpart ] )

swordsmen_unit = Unit(swordsmanmodel,20,6)
zombie_unit = Unit(zombiemodel,35,5)

