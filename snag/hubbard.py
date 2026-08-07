from itertools import combinations, product

import numpy as np


class Hubbard:
    def __init__(self, n_up, n_dn, n_sites):
        self.n_up = n_up
        self.n_dn = n_dn
        self.n_sites = n_sites

        self.n_total = self.n_up + self.n_dn
        self.spin_z = self.n_up - self.n_dn

        assert self.n_total <= 2 * n_sites

        self.basis = self.generate()

    def generate(self):
        b_up = self.generate_sector(self.n_up)
        b_dn = self.generate_sector(self.n_dn)
        full_basis = list(product(b_up, b_dn))
        return np.array(full_basis, dtype=int)

    def generate_sector(self, n):
        basis = []
        for i in combinations(range(self.n_sites), n):
            b = [0] * self.n_sites
            for p in i:
                b[p] = 1
            basis.append(b)
        return basis

    @property
    def dim(self):
        return len(self.basis)

    def __repr__(self):
        return f"spin_z={self.spin_z}, dim={self.dim}"

    def doubles(self):
        return (self.basis[:, 0] * self.basis[:, 1]).sum(1)

    def hopping(self, t_mat):
        assert t_mat.shape == (self.n_sites,) * 2
        hopping_mat = np.zeros((self.dim,) * 2)

        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                s = (self.basis[i] + self.basis[j]) % 2
                if s.sum() == 2:
                    site_1, site_2 = np.where(s.sum(0))[0]
                    hopping_mat[i, j] = hopping_mat[j, i] = -t_mat[site_1, site_2]

        return hopping_mat
