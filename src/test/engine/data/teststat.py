from engine.data.stat import Stat
import unittest


class TestStat(unittest.TestCase):

    def test_instantiation(self):

        tstatname = "Att"
        tstatval = 1

        mystat = Stat(tstatname, tstatval)

        print(mystat)

        assert mystat.name == tstatname
        assert mystat.val == tstatval


    def test_bad_instantiation(self):
        with self.assertRaises(ValueError):
            tstatname = "Ateirgsoipt"
            tstatval = 1

            mystat = Stat(tstatname, tstatval)

            print(mystat)





if __name__ == '__main__':
    unittest.main()