from src.main.engine.combat.attack import Attack
from src.test.engine.data.resources import *
import unittest

class TestAttack(unittest.TestCase):

    def test_to_hit(self):
        Attack.roll_to_hit(swordmodelpart, zombiemodel )



if __name__ == '__main__':
    unittest.main()