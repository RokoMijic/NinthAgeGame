from src.main.engine.combat.combatfight import CombatFightTwoUnits
from src.test.engine.data.resources import *
from src.main.engine.constants import FACING

import unittest

class TestCombatFight(unittest.TestCase):

    def test_basic_fight(self):
        swordsmen_zombie_combat = CombatFightTwoUnits(swordsmen_unit,False,zombie_unit, FACING.FRONT)

        print(swordsmen_zombie_combat)

        swordsmen_zombie_combat.fight()
