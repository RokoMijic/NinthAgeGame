from src.main.engine.data.modelpart import ModelPart

import unittest

class TestModelPart(unittest.TestCase):

    def test_instantiation(self):

        tstatvals = [1, 3, 3, 0, 3]
        tspecialrules = ["HATRED"]
        tmodelpartname = "Angry Peasant"
        mymodelpart = ModelPart(tmodelpartname, tstatvals, tspecialrules)
        print(mymodelpart)

if __name__ == '__main__':
    unittest.main()