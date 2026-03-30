"""
Linear algebra utilities for quantum computing experiments.
"""

import numpy as np
from scipy.linalg import expm


def is_unitary(U, tol=1e-10):
    """Check if matrix U is unitary."""
    n = U.shape[0]
    return np.allclose(U @ U.conj().T, np.eye(n), atol=tol)


def is_hermitian(H, tol=1e-10):
    """Check if matrix H is Hermitian."""
    return np.allclose(H, H.conj().T, atol=tol)


def commutator(A, B):
    """Compute [A, B] = AB - BA."""
    return A @ B - B @ A


def matrix_exp_unitary(H, t):
    """Compute U(t) = exp(-iHt) for Hermitian H."""
    return expm(-1j * H * t)


def spectrum(M):
    """Return (eigenvalues, eigenvectors) sorted by eigenvalue magnitude."""
    if is_hermitian(M):
        vals, vecs = np.linalg.eigh(M)
    else:
        vals, vecs = np.linalg.eig(M)
        idx = np.argsort(np.abs(vals))[::-1]
        vals, vecs = vals[idx], vecs[:, idx]
    return vals, vecs


def singular_values(A):
    """Return singular values of A in descending order."""
    return np.linalg.svd(A, compute_uv=False)


def block_encode(A):
    """
    Construct a block-encoding of A as a unitary U such that
    U[:n, :n] = A, where n = A.shape[0].

    Requires ||A|| <= 1.
    """
    n = A.shape[0]
    I = np.eye(n, dtype=complex)

    def _mat_sqrt(M):
        vals, vecs = np.linalg.eigh(M)
        return vecs @ np.diag(np.sqrt(np.maximum(vals, 0))) @ vecs.conj().T

    B = _mat_sqrt(I - A @ A.conj().T)
    C = _mat_sqrt(I - A.conj().T @ A)
    return np.block([[A, B], [C, -A.conj().T]])


def kron(*matrices):
    """Tensor product of multiple matrices."""
    result = matrices[0]
    for M in matrices[1:]:
        result = np.kron(result, M)
    return result


# Common Pauli matrices
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
