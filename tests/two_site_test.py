import numpy as np
import pytest

import snag


@pytest.mark.parametrize("u", [0.0, 1.0, 2.0])
def test_two_site(u):

    t_mat = np.array([[0.0, 1.0], [1.0, 0.0]])

    calc = snag.Hubbard(1, 1, 2)

    ham = calc.hopping(t_mat) + u * np.diag(calc.doubles())
    gs = np.linalg.eigvalsh(ham)[0]

    e_gs = 0.5 * (u - np.sqrt(u * u + 16))

    assert np.allclose(gs, e_gs)


def test_doubles_zero():
    calc = snag.Hubbard(2, 0, 4)
    assert calc.doubles().sum() == 0
