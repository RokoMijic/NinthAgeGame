import numpy as np


def n_d6_oversix(n: int, X: int):
    # Roll n binary variables with probability X/6 of succeeding
    return 1*(np.random.randint(1,6+1,n) <= X)

