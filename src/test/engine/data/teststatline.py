from src.main.engine.data.statline import Statline
from src.main.engine.constants import DEFENSIVE_STAT_NAMES

import unittest

class TestStatline(unittest.TestCase):

    def test_instantiation(self):

        tstatnames = DEFENSIVE_STAT_NAMES
        tstatvals = [1, 3, 3, 0]

        mystatline = Statline(tstatnames, tstatvals)

        print(mystatline)


    def test_valueselect(self):

        tstatnames = DEFENSIVE_STAT_NAMES
        tstatvals = [1, 3, 3, 0]

        mystatline = Statline(tstatnames, tstatvals)

        print(mystatline.v("HP") )

        assert mystatline.v("HP") == 1



if __name__ == '__main__':
    unittest.main()