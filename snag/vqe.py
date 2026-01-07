import numpy as np
from scipy.optimize import minimize
from dataclasses import dataclass
from qiskit.primitives import StatevectorEstimator

@dataclass
class OptResult:
    energy : float
    cost_hist : np.ndarray
    params : np.ndarray


def run_vqe(ansatz, hamiltonian, energy_func, method="BFGS"):
    """
    Run the Variational Quantum Eigensolver (VQE) algorithm
    to find the minimum energy of a given Hamiltonian.

    Parameters
    ----------
    ansatz : object
        The quantum ansatz circuit used for the VQE optimization.
    hamiltonian : object
        The Hamiltonian whose ground state energy is to be estimated.
    energy_func : callable
        A function that computes the expectation value of the Hamiltonian
        for a given set of parameters.
        Signature: `energy_func(params, ansatz, hamiltonian) -> float`.
    method : str, optional
        The classical optimization method to use (default is "BFGS").
        Must be compatible with `scipy.optimize.minimize`.

    Returns
    -------
    OptResult
        An object containing the optimization results, with the following attributes:
        - energy : float
            The final optimized energy value.
        - cost_hist : np.ndarray
            Array of energy values recorded during the optimization.
        - params : np.ndarray
            The optimized parameters that minimize the energy.
    """
    x0 = 2 * np.pi * np.random.rand(ansatz.num_parameters)

    cost_hist = []
    opt_result = minimize(
        energy_func, x0, args=(ansatz, hamiltonian), method=method, 
        callback=lambda intermediate_result: cost_hist.append(intermediate_result.fun)
        )

    return OptResult(opt_result.fun, np.array(cost_hist), opt_result.x)


def compute_expectation(params, ansatz, operator):
    """
    Compute the expectation value of a quantum operator using a statevector simulator.

    Parameters
    ----------
    params : np.ndarray
        The parameters for the ansatz circuit.
    ansatz : QuantumCircuit
        The parameterized quantum circuit (ansatz) to evaluate.
    operator : BaseOperator
        The quantum operator whose expectation value is to be computed.

    Returns
    -------
    float
        The expectation value of the operator with respect to the state prepared by the ansatz.
    """
    pub = (ansatz, [operator], [params])

    # Get the expected value of X
    estimator = StatevectorEstimator()
    job = estimator.run([pub])
    result = job.result()[0]

    return result.data.evs.item()
