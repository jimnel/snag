import numpy as np
import pytest

import snag


@pytest.mark.parametrize("n_sites", [3, 4, 10, 11, 12, 21])
def test_ring_spectrum(n_sites):

    t_mat = np.diag(np.ones(n_sites - 1), 1) + np.diag(np.ones(n_sites - 1), -1)
    t_mat[0, -1] = 1.0
    t_mat[-1, 0] = 1.0

    calc = snag.NonInteracting(t_mat)

    # theory
    ks = np.arange(n_sites) * 2 * np.pi / n_sites
    es = np.sort(-2 * np.cos(ks))

    assert np.allclose(calc.levels, es)


@pytest.mark.parametrize("topology", ["chain", "ring"])
@pytest.mark.parametrize("n_sites", [3, 4, 5])
def test_argreement(topology, n_sites):
    n_up = 1
    n_dn = 1

    t_mat = np.diag(np.ones(n_sites - 1), 1) + np.diag(np.ones(n_sites - 1), -1)

    if topology == "ring":
        t_mat[0, -1] = 1.0
        t_mat[-1, 0] = 1.0

    calc = snag.Hubbard(n_up=n_up, n_dn=n_dn, n_sites=n_sites)
    spectrum = np.linalg.eigvalsh(calc.hopping(t_mat))

    calc_ni = snag.NonInteracting(t_mat)
    spectrum_ni = calc_ni.full_spectrum(n_up, n_dn)

    assert np.allclose(spectrum, spectrum_ni)
