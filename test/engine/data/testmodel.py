from engine.data.model import Model

import unittest

class TestModel(unittest.TestCase):

    def test_instantiation(self):

        tmodel_name     = "swordsman"
        tmodel_statvals = [4, 8, 7, 1, 3, 3, 0]
        tmodel_specialrules = ["DISTRACTING", "UNBREAKABLE"]

        tmodelpartname      =  "sword attack"
        tmodelpart_statvals = [1, 3, 3, 0, 3]
        tmodelpart_specialrules = ["HATRED"]

        mymodel = Model(tmodel_name, tmodel_statvals, tmodel_specialrules, tmodelpartname, tmodelpart_statvals, tmodelpart_specialrules )
        print(mymodel)

if __name__ == '__main__':
    unittest.main()