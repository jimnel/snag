import numpy as np

def solve(hamiltonian):
    return np.linalg.eigh(hamiltonian)