from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart
from src.main.engine.data.unit import Unit
from src.main.engine.constants import TO_HIT_TABLE
from src.main.engine.utility.utiliy import n_d6_oversix
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class Attack:

    @staticmethod
    def attack_unit(attacker: Unit, defender: Unit, facing: str = "FRONT"):

        pass

    @staticmethod
    def calculate_n_attacks(attacker: Unit, defender: Unit, facing: str):
        pass


    @staticmethod
    def depth(Unit):
        n_models = Unit.number
        width = Unit.width


    @staticmethod
    def roll_to_hit(attackingmp: ModelPart, defender: Model, numattacks: int = 1):
        off = attackingmp.v("Off")
        defence = defender.v("Def")
        off_def_diff = off - defence
        hit_oversix = TO_HIT_TABLE[np.clip(off_def_diff, a_min=-10, a_max=10)]
        total_hits = sum(n_d6_oversix(numattacks, hit_oversix))
        logger.debug("%s with Off %s attacking %s with Def %s, %s times with probability %s/6, hit %s times" % (attackingmp.modelpartname, off, defender.modelname, defence, numattacks, hit_oversix, total_hits)  )
        return total_hits






