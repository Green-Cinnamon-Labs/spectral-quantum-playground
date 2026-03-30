"""
Circuit-level utilities: state preparation, controlled operations, QFT.
"""

import numpy as np


def qft_matrix(n):
    """Return the n-dimensional QFT matrix."""
    omega = np.exp(2j * np.pi / n)
    return np.array([[omega**(j*k) for k in range(n)]
                     for j in range(n)], dtype=complex) / np.sqrt(n)


def iqft_matrix(n):
    """Return the n-dimensional inverse QFT matrix."""
    return qft_matrix(n).conj().T


def controlled_unitary(U):
    """
    Build the controlled-U operator acting on (control ⊗ target).
    ctrl=|0>: identity on target
    ctrl=|1>: apply U on target
    """
    n = U.shape[0]
    I = np.eye(n, dtype=complex)
    P0 = np.outer([1, 0], [1, 0])  # |0><0|
    P1 = np.outer([0, 1], [0, 1])  # |1><1|
    return np.kron(P0, I) + np.kron(P1, U)


def qpe_distribution(phi, n_control_bits):
    """
    Simulate QPE outcome distribution for a unitary with eigenvalue e^(2πiφ).

    Returns probability array over {0, ..., 2^n - 1}.
    """
    N = 2**n_control_bits
    state = np.array([np.exp(2j * np.pi * k * phi)
                      for k in range(N)], dtype=complex) / np.sqrt(N)
    IQFT = iqft_matrix(N)
    state_out = IQFT @ state
    return np.abs(state_out)**2


def prepare_computational_basis(index, n_qubits):
    """Prepare |index> in n_qubits computational basis."""
    state = np.zeros(2**n_qubits, dtype=complex)
    state[index] = 1.0
    return state


def prepare_uniform_superposition(n_qubits):
    """Prepare |+>^n = H^n|0>^n."""
    N = 2**n_qubits
    return np.ones(N, dtype=complex) / np.sqrt(N)
