import numpy as np
import pytest

import snag


@pytest.mark.parametrize("n_sites", [3, 4, 10, 11, 12, 21])
def test_ring_spectrum(n_sites):
    t_mat = snag.get_hopping(n_sites, "ring")
    calc = snag.NonInteracting(t_mat)

    # theory
    ks = np.arange(n_sites) * 2 * np.pi / n_sites
    es = np.sort(-2 * np.cos(ks))
    assert np.allclose(calc.levels, es)


@pytest.mark.parametrize("topology", ["chain", "ring"])
@pytest.mark.parametrize("n_sites", [2, 3, 4, 5])
def test_argreement(topology, n_sites):
    t_mat = snag.get_hopping(n_sites, topology)
    calc_ni = snag.NonInteracting(t_mat)

    for n_up in range(1, n_sites + 1):
        for n_dn in range(1, n_sites + 1):
            sector = snag.Sector(n_up, n_dn, n_sites)
            spectrum_ni = calc_ni.full_spectrum(n_up, n_dn)

            assert sector.size == len(spectrum_ni)

            calc = snag.Hubbard(sector)
            spectrum = np.linalg.eigvalsh(calc.hopping(t_mat))

            assert np.allclose(spectrum, spectrum_ni)
