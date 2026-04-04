"""Recursos auxiliares do notebook N-02."""

from __future__ import annotations

from math import gcd

import matplotlib.pyplot as plt


def _periodo_modular(x: int, N: int) -> int:
    """Retorna o menor r > 0 tal que x^r mod N = 1."""
    for r in range(1, N + 1):
        if pow(x, r, N) == 1:
            return r
    raise ValueError(f"Não foi possível encontrar o período de x={x} mod N={N}.")


def mostrar_periodicidade_shor(
    N: int = 15,
    x: int = 2,
    limite_a: int = 12,
    mostrar: bool = True,
    ax=None,
):
    """Mostra a periodicidade de x^a mod N e os gcds usados por Shor."""
    if N <= 1:
        raise ValueError("N deve ser maior que 1.")
    if limite_a <= 0:
        raise ValueError("limite_a deve ser maior que 0.")
    if gcd(x, N) != 1:
        raise ValueError(f"x={x} deve ser coprimo com N={N}.")

    a_vals = list(range(limite_a))
    x_pows = [x**a for a in a_vals]
    mods = [pow(x, a, N) for a in a_vals]

    r = _periodo_modular(x, N)
    if r % 2 != 0:
        raise ValueError(f"O período encontrado foi r={r}, mas ele precisa ser par.")

    half_power = x ** (r // 2)
    minus_1 = half_power - 1
    plus_1 = half_power + 1
    g1 = gcd(minus_1, N)
    g2 = gcd(plus_1, N)

    header = f'{"a":>2} {"x^a":>6} {"x^a mod N":>10}'
    print(header)
    print("-" * len(header))
    for a, xp, m in zip(a_vals, x_pows, mods):
        print(f"{a:>2} {xp:>6} {m:>10}")

    print()
    print(f"N = {N}, x = {x}, periodo r = {r}")
    print(f"x^(r/2) - 1 = {minus_1}")
    print(f"x^(r/2) + 1 = {plus_1}")
    print(f"gcd(x^(r/2) - 1, N) = {g1}")
    print(f"gcd(x^(r/2) + 1, N) = {g2}")

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=(8, 4))
    else:
        fig = ax.figure

    ax.plot(a_vals, mods, "-o", color="tab:blue", lw=1.8, ms=7)
    for k in range(0, a_vals[-1] // r + 1):
        ax.axvline(k * r, color="tab:green", ls="--", lw=1, alpha=0.65)

    ax.axvspan(0, r, color="tab:green", alpha=0.08)
    indices_periodicos = [i for i, a in enumerate(a_vals) if a % r == 0]
    ax.scatter(
        [a_vals[i] for i in indices_periodicos],
        [mods[i] for i in indices_periodicos],
        color="tab:red",
        s=80,
        zorder=4,
    )

    y_level = max(mods) + 1
    ax.annotate(
        "",
        xy=(0, y_level),
        xytext=(r, y_level),
        arrowprops=dict(arrowstyle="<->", color="tab:green", lw=1.8),
    )
    ax.text(r / 2, y_level + 0.3, f"r = {r}", ha="center", color="tab:green", weight="bold")
    ax.set(
        title=f"f(a) = {x}^a mod {N}",
        xlabel="a",
        ylabel=f"f(a) = {x}^a mod {N}",
        xticks=a_vals,
    )
    ax.set_ylim(-0.5, y_level + 1)
    ax.grid(alpha=0.3)

    if created_fig and mostrar:
        plt.show()

    return {
        "N": N,
        "x": x,
        "a_vals": a_vals,
        "x_pows": x_pows,
        "mods": mods,
        "r": r,
        "x_half_minus_1": minus_1,
        "x_half_plus_1": plus_1,
        "gcd_minus": g1,
        "gcd_plus": g2,
        "fig": fig,
        "ax": ax,
    }
