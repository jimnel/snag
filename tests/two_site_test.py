import qse
import numpy as np
import snag
import pytest


@pytest.mark.parametrize("u", [0.0, 1.0, 2.0])
def test_two_site(u):

    qbits = qse.Qbits(np.array([[0.0], [1.0]]))
    t_mat = qbits.get_adjacency_matrix(1.0)

    calc = snag.Hubbard(1, 1, qbits.nqbits)

    ham = calc.hopping(t_mat) + u * np.diag(calc.doubles())
    gs = np.linalg.eigvalsh(ham)[0]

    e_gs = 0.5 * (u - np.sqrt(u * u + 16))

    assert np.allclose(gs, e_gs)
