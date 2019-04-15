from src.main.engine.combat.attack import Attack
from src.test.engine.data.resources import *
import unittest
import logging

class TestAttack(unittest.TestCase):

    def test_to_hit(self):
        Attack.roll_to_hit(swordmodelpart, zombiemodel )

    def test_to_hit_1000(self):
        Attack.roll_to_hit(swordmodelpart, zombiemodel , numattacks=10000)

    def test_to_hit_1000_zombine_attacks_swordsman(self):
        Attack.roll_to_hit(zombiemodelpart, swordsmanmodel, numattacks=10000)


if __name__ == '__main__':
    unittest.main()