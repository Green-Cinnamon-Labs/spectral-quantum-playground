"""
General-purpose utilities.
"""

import numpy as np


def binary_strings(n):
    """Return all n-bit binary strings as list of strings."""
    return [format(i, f'0{n}b') for i in range(2**n)]


def state_to_dict(state, n_qubits, threshold=1e-6):
    """Convert state vector to dict of {basis_label: amplitude}."""
    result = {}
    for i, amp in enumerate(state):
        if abs(amp) > threshold:
            label = format(i, f'0{n_qubits}b')
            result[f'|{label}>'] = amp
    return result


def trotter_error_bound(H_A, H_B, t, r):
    """
    First-order Trotter error bound: ||[A,B]|| * t^2 / (2r)
    """
    comm = H_A @ H_B - H_B @ H_A
    return np.linalg.norm(comm) * t**2 / (2 * r)


def phase_from_eigenvalue(eigenvalue):
    """Extract phase φ from eigenvalue e^(2πiφ), returned in [0, 1)."""
    phi = np.angle(eigenvalue) / (2 * np.pi)
    return phi % 1.0
