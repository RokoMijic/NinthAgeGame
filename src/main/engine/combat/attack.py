from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart
from src.main.engine.data.unit import Unit
from src.main.engine.constants import TO_HIT_TABLE
from src.main.engine.utility.utiliy import n_d6_oversix

class Attack:

    @staticmethod
    def attack_unit(attacker: Unit, defender: Unit, facing: str = "FRONT"):
        pass

    @staticmethod
    def attack_single(attackingmp: ModelPart, defender: Model):
        pass

    @staticmethod
    def roll_to_hit(attackingmp: ModelPart, defender: Model, numattacks: int):
        off_def_diff = attackingmp.v("Off") - defender.v("Def")
        hit_oversix = TO_HIT_TABLE[np.clip(off_def_diff, a_min=-10, a_max=10)]
        return sum( n_d6_oversix(hit_oversix,numattacks) )






