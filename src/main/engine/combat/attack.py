from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart
from src.main.engine.constants import TO_HIT_TABLE, TO_WOUND_TABLE
from src.main.engine.utility.utiliy import n_d6_oversix
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class Attack:


    @staticmethod
    def roll_to_hit(attackingmp: ModelPart, defender: Model, numattacks: int ):
        off = attackingmp.v("Off")
        defence = defender.v("Def")
        off_def_diff = off - defence
        success_prob_oversix = TO_HIT_TABLE[np.clip(off_def_diff, a_min=-10, a_max=10)]
        total_successes = sum(n_d6_oversix(numattacks, success_prob_oversix))
        logger.debug("%s with Off %s attacking %s with Def %s, %s times with probability %s/6, hit %s times" %
                     (attackingmp.modelpartname, off, defender.modelname, defence, numattacks, success_prob_oversix, total_successes))
        return total_successes


    @staticmethod
    def roll_to_wound(attackingmp: ModelPart, defender: Model, numhits: int ):
        str = attackingmp.v("Str")
        res = defender.v("Res")
        str_res_diff = str - res
        success_prob_oversix = TO_WOUND_TABLE[np.clip(str_res_diff, a_min=-10, a_max=10)]
        total_successes = sum(n_d6_oversix(numhits, success_prob_oversix))
        logger.debug("%s with Str %s hits %s with Res %s, %s times with probability %s/6, wounds %s times" %
                     (attackingmp.modelpartname, str, defender.modelname, res, numhits, success_prob_oversix, total_successes))
        return total_successes

    @staticmethod
    def roll_to_penetrate(attackingmp: ModelPart, defender: Model, numwounds: int ):
        ap = attackingmp.v("AP")
        arm = defender.v("Arm")
        arm_pen_diff = arm-ap
        success_prob_oversix = 6-np.clip(arm_pen_diff, a_min=0, a_max=5)
        total_successes = sum(n_d6_oversix(numwounds, success_prob_oversix))
        logger.debug("%s with AP %s wounds %s with Arm %s, %s times with probability %s/6, total of %s unsaved wounds" %
                     (attackingmp.modelpartname, ap, defender.modelname, arm, numwounds, success_prob_oversix, total_successes))
        return total_successes

    @staticmethod
    def roll_against_special_save(attackingmp: ModelPart, defender: Model, num_unsaved_wounds: int ):

        # TODO: make special saves work
        total_successes = num_unsaved_wounds

        logger.debug("%s gets unsaved wounds against %s, %s get through the special save TODO THESE SAVES ARE NOT BEING IMPLEMENTED" %
                     (attackingmp.modelpartname, defender.modelname, total_successes ))
        return total_successes


    @staticmethod
    def full_attack_roll(attackingmp: ModelPart, defender: Model, numattacks: int):
        # attack a certain number of times with a particular model part against a specific defending model

        total_successes = Attack.roll_against_special_save(attackingmp, defender,
                                    Attack.roll_to_penetrate(attackingmp, defender,
                                                Attack.roll_to_wound(attackingmp, defender,
                                                                Attack.roll_to_hit(attackingmp, defender,numattacks)
                                                                    )
                                                            )
                                                          )

        logger.debug("%s attacks %s, %s times, total of %s unsaved wounds" %
                     (attackingmp.modelpartname, defender.modelname, numattacks, total_successes))
        return total_successes



    def attack_roll_all_modelparts(attacker: Model, defender: Model, numattacks: int):
        # Note: this attack function ignores the agility of model parts and possibility of return attacks. Use with caution.

        total_successes = sum([Attack.full_attack_roll(attackingmp, defender, numattacks=numattacks ) for attackingmp in attacker.modelparts])

        logger.debug("%s attacks %s, %s times, total of %s unsaved wounds" %
                     (attacker.modelname, defender.modelname, numattacks, total_successes))

        return total_successes

