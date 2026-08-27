from math import comb


class Sector:
    def __init__(self, n_up, n_dn, n_sites):
        check_number(n_up, n_sites)
        check_number(n_dn, n_sites)

        self.n_up = n_up
        self.n_dn = n_dn
        self.n_sites = n_sites

    @property
    def n_part(self):
        return self.n_up + self.n_dn

    @property
    def spin_z(self):
        return self.n_up - self.n_dn

    @property
    def size(self):
        return comb(self.n_sites, self.n_up) * comb(self.n_sites, self.n_dn)

    def __repr__(self):
        return f"n_up: {self.n_up}, n_dn: {self.n_dn}"


def check_number(n, l):
    if (n < 0) or (n > l):
        raise ValueError
