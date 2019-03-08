from src.main.engine.data.statlinegeneral import StatlineGeneral

import unittest

class TestStatlineGeneral(unittest.TestCase):

    def test_instantiation(self):

        tstatvals = [4, 8, 7, 1, 3, 3, 0]
        mystatline = StatlineGeneral(tstatvals)
        print(mystatline)

if __name__ == '__main__':
    unittest.main()