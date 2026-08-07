from dataclasses import dataclass

import numpy as np


@dataclass
class Result:
    energy_hist: np.ndarray
    e0: float
    state: np.ndarray


def run_lanczos(hamiltonian, max_iter=20):
    dim = len(hamiltonian)
    psi0 = np.random.rand(dim, 1) + 1j * np.random.rand(dim, 1)
    psi0 /= np.linalg.norm(psi0)

    print("Initial State:", psi0)

    e0 = _compute_energy(hamiltonian, psi0)
    print("Initial Energy: ", e0)

    print("Begining Loop:\nIteration, Energy\n")

    results = np.zeros(max_iter + 1)
    results[0] = e0

    for i in range(max_iter):
        shifted_hamiltonian = hamiltonian.copy()
        np.fill_diagonal(
            shifted_hamiltonian, np.diag(shifted_hamiltonian) - np.real(e0)
        )

        psi1 = shifted_hamiltonian @ psi0
        psi1 /= np.linalg.norm(psi1)

        e1 = _compute_energy(hamiltonian, psi1)
        gamma = _hamiltonian_element(hamiltonian, psi0, psi1)

        coef2, e0 = _solve_2x2_matrix(e0, e1, gamma)

        psi0 += psi1 * coef2
        psi0 /= np.linalg.norm(psi0)

        print(i + 1, e0)
        results[i + 1] = np.real(e0)

    return Result(results, e0, psi0)


def _hamiltonian_element(h, psi1, psi2):
    return (np.conj(psi1.T) @ (h @ psi2)).item()


def _compute_energy(h, psi):
    return _hamiltonian_element(h, psi, psi).real


def _solve_2x2_matrix(a, b, c):
    """
    M = [ a  c
          c* b ]

    (a-l)(b-l) - |c|^2 = 0
    l^2 -l(a+b) + ab - |c|^2 = 0
    l = {(a+b) pm sqrt[(a+b)^2-4ab+4|c|^2]} / 2 = {a+b pm sqrt[(a-b)^2+4|c|^2]} / 2
    let delta = sqrt[ (a-b)^2+4|c|^2 ]

    l = {a+b pm delta} / 2

    M (x, y)^T = l (x, y)^T
    ax + cy = {a+b pm delta}x / 2
    y = {b -a pm delta}x / 2c
    """
    delta = np.sqrt((a - b) ** 2 + 4.0 * c * np.conj(c))
    eig_lower = (a + b - delta) * 0.5
    coef2 = (b - a - delta) / (2.0 * c)
    return coef2, eig_lower
