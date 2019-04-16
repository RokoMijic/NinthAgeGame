from src.main.engine.combat.attack import Attack
from src.test.engine.data.resources import *
import unittest
import logging

class TestAttack(unittest.TestCase):


    # Test to hit

    def test_to_hit(self):
        Attack.roll_to_hit(swordmodelpart, zombiemodel )

    def test_to_hit_1000(self):
        Attack.roll_to_hit(swordmodelpart, zombiemodel , numattacks=10000)

    def test_to_hit_1000_zombine_attacks_swordsman(self):
        Attack.roll_to_hit(zombiemodelpart, swordsmanmodel, numattacks=10000)

    #     test to wound

    def test_to_wound_1000(self):
        Attack.roll_to_wound(swordmodelpart, zombiemodel, numhits=10000)

    def test_to_wound_1000_zombine_attacks_swordsman(self):
        Attack.roll_to_wound(zombiemodelpart, swordsmanmodel, numhits=10000)

    #     test armour penetration

    def test_to_penetrate_1000(self):
        Attack.roll_to_penetrate(swordmodelpart, zombiemodel, numwounds=10000)

    def test_to_penetrate_1000_zombine_attacks_swordsman(self):
        Attack.roll_to_penetrate(zombiemodelpart, swordsmanmodel, numwounds=10000)


    #     test full attack roll

    def test_full_attack_1000(self):
        Attack.full_attack_roll(swordmodelpart, zombiemodel, numattacks=10000)

    def test_full_attack_1000_zombine_attacks_swordsman(self):
        Attack.full_attack_roll(zombiemodelpart, swordsmanmodel, numattacks=10000)

    def test_full_attack_1000_zombine_attacks_knight(self):
        Attack.full_attack_roll(zombiemodelpart, knightmodel, numattacks=10000)

    def test_full_attack_1000_knight_attacks_zombie(self):
        Attack.attack_roll_all_modelparts(knightmodel, zombiemodel, numattacks=10000)



if __name__ == '__main__':
    unittest.main()