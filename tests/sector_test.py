import pytest

import snag


@pytest.mark.parametrize("n_sites", [3, 4, 10])
def test_sector_fail(n_sites):
    with pytest.raises(ValueError):
        snag.Sector(n_sites + 1, 0, n_sites)
