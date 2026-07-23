import numpy as np
from itertools import product, combinations


class NonInteracting:
    def __init__(self, t_matrix):
        self.n_sites = t_matrix.shape[0]
        self.levels = np.linalg.eigvalsh(-t_matrix)

    def total_energy(self, n_up, n_dn):
        return self.levels[:n_up].sum() + self.levels[:n_dn].sum()

    def full_spectrum(self, n_up, n_dn):
        dim = len(self.levels)
        full_spectrum = [
            self.levels[i] + self.levels[j]
            for i, j in product(
                combinations(range(dim), n_up), combinations(range(dim), n_dn)
            )
        ]
        return np.sort(np.array(full_spectrum))
