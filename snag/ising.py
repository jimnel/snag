from qiskit.quantum_info import SparsePauliOp

def gen_hamiltonian_op(field, coupling, n_qubits, pbc=True):
    r"""
    Create the Hamiltonian for the Transverse Field Ising Model:

    $$
        H = -H \sum_i X_i - J sum_<i,j> Z_i Z_j
    $$

    Parameters
    ----------
    field : float
        The field strength, H.
    coupling : float
        The coupling strength, J.
    n_qubits : int
        The number of qubits.
    pbc : bool, optional
        Whether to use periodic Boundary Conitions.
        Defaults to True.

    Returns
    -------
    SparsePauliOp
        The Hamiltonian.
    """
    ops_field = ["I"*i + "X" + "I" * (n_qubits-i-1) for i in range(n_qubits)]
    coefs_field = [-field] * n_qubits

    ops_int = ["I"*i + "ZZ" + "I" * (n_qubits-i-2) for i in range(n_qubits-1)]
    if pbc:
        ops_int.append("Z" + "I"*(n_qubits-2) + "Z")
    coefs_int = [-coupling] * len(ops_int)

    return SparsePauliOp(ops_field + ops_int, coefs_field + coefs_int)


def gen_magnetization_op(n_qubits):
    r"""
    Create the magnetization:

    $$
        M = \sum_i Z_i
    $$

    Parameters
    ----------
    n_qubits : int
        The number of qubits.

    Returns
    -------
    SparsePauliOp
        The magnetization.
    """
    ops = ["I"*i + "Z" + "I" * (n_qubits-i-1) for i in range(n_qubits)]
    coefs = [1] * n_qubits

    return SparsePauliOp(ops, coefs)
