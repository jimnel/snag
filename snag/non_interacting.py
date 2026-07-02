import numpy as np
from itertools import combinations

class NonInt1D:
    def __init__(self, n_sites):
        self.n_sites = n_sites
    
    def ks(self):
        ns = np.arange(self.n_sites)-self.n_sites//2
        return 2*np.pi*(ns) / self.n_sites
    
    def single_particle_spectrum(self):
        return -2*np.cos(self.ks())

    def many_body_spectrum(self, n_part):
        one_part_spec = self.single_particle_spectrum()
        spec = [one_part_spec[[comb]][0] for comb in combinations(range(self.n_sites), n_part)]
        spec = np.array(spec).sum(1)
        return np.sort(spec)