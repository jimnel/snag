import numpy as np

def gen_basis(n_sites, n_part):
    basis = {}
    counter = 0

    for i in range(2**n_sites):
        b_i = np.binary_repr(i, n_sites)
        if b_i.count("1") == n_part:
            basis[b_i] = counter
            counter += 1
    return basis
