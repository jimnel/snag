from itertools import combinations, product

import numpy as np

from .sector import Sector


class Hubbard:
    def __init__(self, sector: Sector):
        self.sector = sector
        self.basis = self.generate()
        self.basis_flat = np.column_stack((self.basis[:, 0], self.basis[:, 1]))

    def generate(self):
        b_up = self.generate_sector(self.sector.n_up)
        b_dn = self.generate_sector(self.sector.n_dn)
        return np.array(list(product(b_up, b_dn)), dtype=int)

    def generate_sector(self, n):
        basis = []
        for i in combinations(range(self.sector.n_sites), n):
            b = [0] * self.sector.n_sites
            for p in i:
                b[p] = 1
            basis.append(b)
        return basis

    @property
    def dim(self):
        return len(self.basis)

    def doubles(self):
        return (self.basis[:, 0] * self.basis[:, 1]).sum(1)

    def hopping(self, t_mat):
        assert t_mat.shape == (self.sector.n_sites,) * 2
        hopping_mat = np.zeros((self.dim,) * 2)

        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                s = (self.basis_flat[i] + self.basis_flat[j]) % 2
                if sum(s) == 2:
                    ind_1, ind_2 = np.where(s)[0]
                    n_s = sum(self.basis_flat[i][ind_1 + 1 : ind_2])
                    sgn = -((-1) ** n_s)

                    site_1 = ind_1 % self.sector.n_sites
                    site_2 = ind_2 % self.sector.n_sites

                    hopping_mat[i, j] = hopping_mat[j, i] = sgn * t_mat[site_1, site_2]

        return hopping_mat
