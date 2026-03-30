"""
Visualization utilities for spectral and quantum circuit experiments.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_spectrum(matrix, title=None, ax=None):
    """Plot eigenvalues of a matrix in the complex plane."""
    eigvals = np.linalg.eigvals(matrix)
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))

    ax.scatter(eigvals.real, eigvals.imag, zorder=3)
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3, label='unit circle')
    ax.axhline(0, color='gray', alpha=0.3)
    ax.axvline(0, color='gray', alpha=0.3)
    ax.set_aspect('equal')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_title(title or 'Spectrum')
    return ax


def plot_qpe_distribution(probs, phi_true=None, title=None, ax=None):
    """Plot QPE outcome probability distribution."""
    N = len(probs)
    x = np.arange(N) / N

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(x, probs, width=0.8 / N, color='steelblue', alpha=0.8)
    if phi_true is not None:
        ax.axvline(phi_true % 1, color='red', linestyle='--',
                   label=f'φ = {phi_true:.4f}')
        ax.legend()
    ax.set_xlabel('Estimated φ')
    ax.set_ylabel('Probability')
    ax.set_title(title or 'QPE distribution')
    return ax


def plot_dynamics(times, expectations, label='⟨O⟩', title=None, ax=None):
    """Plot expectation value dynamics."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(times, expectations, label=label)
    ax.set_xlabel('Time')
    ax.set_ylabel('Expectation value')
    ax.set_title(title or 'Dynamics')
    ax.legend()
    return ax


def bloch_vector(state):
    """Compute Bloch vector (rx, ry, rz) for a 1-qubit state."""
    assert len(state) == 2, "Only 1-qubit states"
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    rx = np.real(state.conj() @ X @ state)
    ry = np.real(state.conj() @ Y @ state)
    rz = np.real(state.conj() @ Z @ state)
    return np.array([rx, ry, rz])
