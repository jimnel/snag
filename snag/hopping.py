import numpy as np


def get_hopping(n_sites, topology="chain"):
    t_mat = np.diag(np.ones(n_sites - 1), 1) + np.diag(np.ones(n_sites - 1), -1)

    if topology == "ring":
        t_mat[0, -1] = 1.0
        t_mat[-1, 0] = 1.0

    return t_mat
