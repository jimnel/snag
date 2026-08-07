import numpy as np
import pytest
from scipy.spatial.distance import pdist

import snag


@pytest.mark.parametrize("n_sites", [3, 4, 10, 11, 12, 21])
def test_ring_spectrum(n_sites):
    thetas = np.arange(n_sites) * 2 * np.pi / n_sites
    positions = np.array([np.cos(thetas), np.sin(thetas)]).T
    dists = pdist(positions)

    calc = snag.HubbardMol(
        n_up=1,
        n_dn=1,
        n_sites=n_sites,
        u=0.0,
        hopping_func=lambda x: 1 * np.isclose(x, dists.min()),
    )

    e_gs = calc.solve(dists)

    # theory
    ks = np.arange(n_sites) * 2 * np.pi / n_sites
    es = np.sort(-2 * np.cos(ks))

    assert np.isclose(e_gs, es[0] * 2)
