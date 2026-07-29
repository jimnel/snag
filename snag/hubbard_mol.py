import numpy as np
from .hubbard import Hubbard
from scipy.spatial.distance import squareform

def radial_hopping(r):
    return 1.0 / r**3

class HubbardMol:
    def __init__(self, hubbard_calc, u=1.0, hopping_func=None):
        self.hubbard_calc = hubbard_calc
        if hopping_func is None:
            self.hopping_func = radial_hopping
        else:
            self.hoppint_func = hopping_func

        self.u = u
        self.doubles = self.hubbard_calc.doubles()

    def solve(self, d):
        hopping = squareform(radial_hopping(d))
        ham = self.hubbard_calc.hopping(hopping) + self.u * np.diag(self.doubles)
        return np.linalg.eigvalsh(ham)[0]
