"""Recursos auxiliares do notebook N-02."""

from __future__ import annotations

from math import gcd

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def _periodo_modular(x: int, N: int) -> int:
    """Retorna o menor r > 0 tal que x^r mod N = 1."""
    for r in range(1, N + 1):
        if pow(x, r, N) == 1:
            return r
    raise ValueError(f"Não foi possível encontrar o período de x={x} mod N={N}.")


def _caixa(ax, x: float, y: float, w: float, h: float, texto: str, facecolor: str, edgecolor: str) -> None:
    """Desenha uma caixa arredondada com texto centralizado."""
    patch = FancyBboxPatch(
        (x, y - h / 2),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y, texto, ha="center", va="center", fontsize=10, family="monospace")


def mostrar_registradores_shor(
    N: int = 15,
    x: int = 2,
    q: int = 8,
    mostrar: bool = True,
):
    """Mostra os dois registradores antes e depois da exponenciação modular."""
    if N <= 1:
        raise ValueError("N deve ser maior que 1.")
    if q <= 0:
        raise ValueError("q deve ser maior que 0.")
    if gcd(x, N) != 1:
        raise ValueError(f"x={x} deve ser coprimo com N={N}.")

    a_vals = list(range(q))
    f_vals = [pow(x, a, N) for a in a_vals]
    bits_a = max(1, (q - 1).bit_length())
    bits_f = max(1, (N - 1).bit_length())

    palette = ["#dbeafe", "#dcfce7", "#fef3c7", "#fee2e2", "#ede9fe", "#cffafe"]
    color_map = {valor: palette[i % len(palette)] for i, valor in enumerate(dict.fromkeys(f_vals))}

    fig_h = max(7.2, 1.25 + 0.9 * q)
    fig, ax = plt.subplots(figsize=(14, fig_h))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, q + 4.1)
    ax.axis("off")

    panel_y = 0.6
    panel_h = q + 2.7
    left_panel = FancyBboxPatch(
        (0.03, panel_y),
        0.42,
        panel_h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.3,
        edgecolor="#94a3b8",
        facecolor="#f8fafc",
    )
    right_panel = FancyBboxPatch(
        (0.55, panel_y),
        0.42,
        panel_h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.3,
        edgecolor="#94a3b8",
        facecolor="#f8fafc",
    )
    ax.add_patch(left_panel)
    ax.add_patch(right_panel)

    top = q + 1.8
    step = 0.82
    box_w = 0.12
    box_h = 0.5
    x1_left, x2_left = 0.09, 0.25
    x1_right, x2_right = 0.61, 0.77

    ax.text(0.24, q + 3.55, "Antes da exponenciacao modular", ha="center", va="center", fontsize=14, weight="bold")
    ax.text(0.76, q + 3.55, "Depois da exponenciacao modular", ha="center", va="center", fontsize=14, weight="bold")
    ax.text(0.24, q + 3.08, rf"$\frac{{1}}{{\sqrt{{{q}}}}}\sum_{{a=0}}^{{{q-1}}}|a\rangle|0\rangle$", ha="center", fontsize=12.5)
    ax.text(
        0.76,
        q + 3.08,
        rf"$\frac{{1}}{{\sqrt{{{q}}}}}\sum_{{a=0}}^{{{q-1}}}|a\rangle|{x}^a\ \mathrm{{mod}}\ {N}\rangle$",
        ha="center",
        fontsize=12.5,
    )

    ax.text(x1_left + box_w / 2, q + 2.35, "Registro 1\nindice a", ha="center", va="center", fontsize=11, weight="bold")
    ax.text(x2_left + box_w / 2, q + 2.35, "Registro 2\ninicial", ha="center", va="center", fontsize=11, weight="bold")
    ax.text(x1_right + box_w / 2, q + 2.35, "Registro 1\nindice a", ha="center", va="center", fontsize=11, weight="bold")
    ax.text(x2_right + box_w / 2, q + 2.35, "Registro 2\nf(a) = x^a mod N", ha="center", va="center", fontsize=11, weight="bold")

    for i, (a, f_a) in enumerate(zip(a_vals, f_vals)):
        y = top - i * step
        a_text = f"a={a}\n{a:0{bits_a}b}"
        zero_text = f"0\n{0:0{bits_f}b}"
        f_text = f"{f_a}\n{f_a:0{bits_f}b}"

        _caixa(ax, x1_left, y, box_w, box_h, a_text, "#e0f2fe", "#0284c7")
        _caixa(ax, x2_left, y, box_w, box_h, zero_text, "#f1f5f9", "#64748b")
        _caixa(ax, x1_right, y, box_w, box_h, a_text, "#e0f2fe", "#0284c7")
        _caixa(ax, x2_right, y, box_w, box_h, f_text, color_map[f_a], "#475569")

        ax.annotate(
            "",
            xy=(x1_right - 0.02, y),
            xytext=(x2_left + box_w + 0.02, y),
            arrowprops=dict(arrowstyle="->", lw=1.25, color="#64748b"),
        )
        ax.text(
            0.5,
            y,
            rf"$|{a}\rangle|0\rangle \rightarrow |{a}\rangle|{f_a}\rangle$",
            ha="center",
            va="center",
            fontsize=9.5,
            color="#334155",
            bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.9),
        )

    legenda_x = 0.58
    legenda_y = 0.85
    ax.text(legenda_x, legenda_y + 0.35, "Repeticoes no Registro 2", fontsize=11, weight="bold", color="#334155")
    for i, valor in enumerate(dict.fromkeys(f_vals)):
        x_pos = legenda_x + i * 0.085
        patch = FancyBboxPatch(
            (x_pos, legenda_y - 0.02),
            0.06,
            0.26,
            boxstyle="round,pad=0.02,rounding_size=0.02",
            linewidth=1,
            edgecolor="#475569",
            facecolor=color_map[valor],
        )
        ax.add_patch(patch)
        ax.text(x_pos + 0.03, legenda_y + 0.11, str(valor), ha="center", va="center", fontsize=10, family="monospace")

    padrao = ",".join(str(v) for v in f_vals)
    ax.text(0.76, 0.45, f"padrao no Registro 2: {padrao}", ha="center", fontsize=10.5, color="#475569")
    ax.text(0.24, 0.45, f"q = {q}  |  N = {N}  |  x = {x}", ha="center", fontsize=10.5, color="#475569")

    fig.tight_layout()
    if mostrar:
        plt.show()

    return {
        "fig": fig,
        "ax": ax,
        "N": N,
        "x": x,
        "q": q,
        "a_vals": a_vals,
        "f_vals": f_vals,
        "bits_a": bits_a,
        "bits_f": bits_f,
    }


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
