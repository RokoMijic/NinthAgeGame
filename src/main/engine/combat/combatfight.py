
from src.main.engine.data.unit import Unit
from src.main.engine.constants import FACING
from src.main.engine.data.model import Model
from src.main.engine.data.modelpart import ModelPart
from src.main.engine.constants import ALLOWED_SUPPORTING_ATTACKS

from src.main.engine.combat.attack import Attack

import math


class CombatFightTwoUnits:

    # defines a fight between two units, and assumes that they allocate all avaiable attacks against each other.
    # This class has state to do with buffs, orientation, etc.

    def __init__(self, charger: Unit, charger_charging: bool, chargereciever: Unit, in_facing: FACING):
        self.charger = charger
        self.attacker_charging = charger_charging
        self.chargereciever = chargereciever
        self.in_facing = in_facing

    def __repr__(self):
        return "\n" + str(self.charger) + "\n" + "  ....... vs ....... " + str(self.chargereciever) + "\n" \
               +  " in the " + str(self.in_facing.value) + " and " + (" not charging ", " charging ")[self.attacker_charging == True]

    def other_unit(self, unit: Unit):
        return self.chargereciever if unit == self.charger else self.charger


    def calculate_attacking_files(self, attacking_unit: Unit):
        assert attacking_unit in [self.charger, self.chargereciever]
        target_unit = self.other_unit(attacking_unit)

        if attacking_unit == self.charger:
            if self.in_facing == FACING.FRONT or FACING.REAR:
                target_frontage = target_unit.width_inches

            elif self.in_facing == FACING.FLANK:
                target_frontage = target_unit.depth_inches
            else:
                raise ValueError("Facing is not valid: %s" % self.in_facing)
        else:
            target_frontage = target_unit.width_inches

        # limit attacking to files to what you can get in contact
        return  min(attacking_unit.numfiles, math.ceil(target_frontage / attacking_unit.models.basewidth) + 1)


    def calculate_num_attacks(self, attacking_unit: Unit, attacking_mp: ModelPart):
        return self.calculate_num_direct_attacks(self, attacking_unit, attacking_mp) + \
                   self.calculate_num_supporting_attacks(self, attacking_unit, attacking_mp)


    def calculate_num_direct_attacks(self, attacking_unit: Unit, attacking_mp: ModelPart):
        return self.calculate_attacking_files(attacking_unit)*attacking_mp.v("Att")


    def calculate_num_supporting_attacks(self, attacking_unit: Unit, attacking_mp: ModelPart):

        if attacking_unit == self.chargereciever and (self.in_facing == FACING.FLANK or FACING.REAR):
            num_supporting_attacks =  0
        else:
            numfiles = self.calculate_attacking_files(attacking_unit)
            FIER_number = 0 if attacking_unit.numfiles < 8 else 1
            allowed_supporting_ranks = 1+FIER_number

            num_full_supporting_ranks = min(1+FIER_number, attacking_unit.numfullranks -1)
            last_rank_supporting = attacking_unit.numranks <= allowed_supporting_ranks + 1 and attacking_unit.numranks >= 1

            num_supporting_models = num_full_supporting_ranks*numfiles + attacking_unit.lastranknumber if last_rank_supporting else 0

            num_supporting_attacks = num_supporting_models*min(ALLOWED_SUPPORTING_ATTACKS[attacking_unit.models.size], attacking_mp.v("Att"))

        return num_supporting_attacks






    def fight(self):
    # make the units fight one round against each other

        agility_values = [mp.v("Agi") for mp in self.charger.models.modelparts + self.chargereciever.models.modelparts]

        assert len(agility_values) > 0

        for agi in agility_values:

            for attacking_unit in [self.charger, self.chargereciever]:

                attacking_unit_parts_this_agility_step = [mp for mp in (attacking_unit.models.modelparts) if mp.v("Agi") == agi]

                damage_this_agi = 0

                for ap in attacking_unit_parts_this_agility_step:

                    num_allowed_attacks = self.calculate_num__direct_attacks()

                    damage_this_ap = Attack.full_attack_roll(ap, self.other_unit(attacking_unit).models, )

                    damage_this_agi += damage_this_ap

                    print( str(ap.modelpartname) + " inflicts " +  str(damage_this_ap) + " on " + self.other_unit(attacking_unit).models.modelname )














