import numpy as np


def n_d6_oversix(X: int, n:int):
    return 1*(np.random.randint(1,6,n) <= X)