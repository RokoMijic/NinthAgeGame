from src.main.engine.data.statlineoffensive import StatlineOffensive

import unittest

class TestStatlineOffensive(unittest.TestCase):

    def test_instantiation(self):

        tstatvals = [4, 8, 7, 1, 3]
        mystatline = StatlineOffensive(tstatvals)
        print(mystatline)

if __name__ == '__main__':
    unittest.main()