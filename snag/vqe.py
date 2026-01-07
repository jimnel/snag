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
    x0 = 2 * np.pi * np.random.rand(ansatz.num_parameters)

    cost_hist = []
    opt_result = minimize(
        energy_func, x0, args=(ansatz, hamiltonian), method=method, 
        callback=lambda intermediate_result: cost_hist.append(intermediate_result.fun)
        )

    return OptResult(opt_result.fun, np.array(cost_hist), opt_result.x)


def compute_expectation(params, ansatz, operator):
    pub = (ansatz, [operator], [params])

    # Get the expected value of X
    estimator = StatevectorEstimator()
    job = estimator.run([pub])
    result = job.result()[0]

    return result.data.evs.item()