"""Recursos auxiliares do notebook N-00."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def _style_dark_axis(ax) -> None:
    ax.set_facecolor("#111")
    ax.tick_params(colors="#9ca3af")
    for spine in ax.spines.values():
        spine.set_edgecolor("#374151")


def mostrar_moeda_superposicao(n: int = 2000, seed: int = 42, mostrar: bool = True):
    """Mostra amplitudes, probabilidades e frequencia acumulada da moeda."""
    alpha = np.sqrt(0.75)
    beta = np.sqrt(0.25)

    assert np.isclose(alpha**2 + beta**2, 1.0), "estado invalido"

    print("── Estado no ar (superposição) ──────────────────────────────")
    print("  |moeda⟩ = α·|cara⟩ + β·|coroa⟩")
    print(f"  |moeda⟩ = {alpha:.4f}·|cara⟩ + {beta:.4f}·|coroa⟩")
    print(f"  |α|² + |β|² = {alpha**2:.2f} + {beta**2:.2f} = {alpha**2 + beta**2:.2f}  ✓")
    print()
    print("── Probabilidades (após medir — a moeda cai) ─────────────────")
    print(f"  P(cara)  = |α|² = {alpha**2:.0%}")
    print(f"  P(coroa) = |β|² = {beta**2:.0%}")

    rng = np.random.default_rng(seed)
    resultados = rng.choice([0, 1], size=n, p=[alpha**2, beta**2])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4), facecolor="#111")
    fig.patch.set_facecolor("#111")

    for ax in axes:
        _style_dark_axis(ax)

    ax1 = axes[0]
    labels = ["cara", "coroa"]
    amps = [alpha, beta]
    probs = [alpha**2, beta**2]
    x = np.array([0, 1])

    bars_amp = ax1.bar(
        x - 0.2,
        amps,
        width=0.35,
        color="steelblue",
        alpha=0.9,
        label="amplitude (α, β)",
    )
    bars_prob = ax1.bar(
        x + 0.2,
        probs,
        width=0.35,
        color="tomato",
        alpha=0.9,
        label="probabilidade = |amp|²",
    )

    for bar, value in zip(bars_amp, amps):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.02,
            f"{value:.3f}",
            ha="center",
            color="steelblue",
            fontsize=9,
        )
    for bar, value in zip(bars_prob, probs):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.02,
            f"{value:.0%}",
            ha="center",
            color="tomato",
            fontsize=9,
        )

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, color="#d1d5db")
    ax1.set_ylim(0, 1.15)
    ax1.set_title("Amplitude ≠ Probabilidade", color="white", pad=10)
    ax1.legend(fontsize=8, labelcolor="#d1d5db", facecolor="#1f2937", edgecolor="#374151")

    ax2 = axes[1]
    freq_acum = np.cumsum(resultados == 0) / np.arange(1, n + 1)
    ax2.plot(freq_acum, color="steelblue", lw=1.2, alpha=0.9)
    ax2.axhline(alpha**2, color="tomato", linestyle="--", lw=1.5, label=f"P(cara) = {alpha**2:.0%}")
    ax2.set_xlabel("número de lances", color="#9ca3af")
    ax2.set_ylabel("freq. de cara", color="#9ca3af")
    ax2.set_ylim(0, 1)
    ax2.set_xlim(0, n)
    ax2.set_title("A frequência converge para |α|²", color="white", pad=10)
    ax2.legend(fontsize=9, labelcolor="#d1d5db", facecolor="#1f2937", edgecolor="#374151")

    plt.suptitle(
        "Superposição → medição → resultado   |   a amplitude dita a probabilidade, não a probabilidade em si",
        color="#9ca3af",
        fontsize=10,
        y=1.02,
    )
    plt.tight_layout()

    if mostrar:
        plt.show()

    return fig, axes


def mostrar_superposicao_como_onda(mostrar: bool = True):
    """Mostra os componentes separados e a onda superposta."""
    alpha = beta = 1 / np.sqrt(2)
    f_cara, f_coroa = 3, 7

    t = np.linspace(0, 2 * np.pi, 800)
    w_cara = alpha * np.sin(f_cara * t)
    w_coroa = beta * np.sin(f_coroa * t)
    superposicao = w_cara + w_coroa

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(12, 4),
        facecolor="#111",
        gridspec_kw={"width_ratios": [1, 1.6]},
    )
    fig.patch.set_facecolor("#111")

    for ax in axes:
        _style_dark_axis(ax)
        ax.set_xlim(0, 2 * np.pi)
        ax.set_xticks([0, np.pi, 2 * np.pi])
        ax.set_xticklabels(["0", "π", "2π"], color="#9ca3af")
        ax.axhline(0, color="#374151", lw=0.8)

    ax = axes[0]
    ax.plot(t, w_cara, color="tomato", lw=2, label=f"|cara⟩   α={alpha:.2f}  f={f_cara}")
    ax.plot(t, w_coroa, color="steelblue", lw=2, label=f"|coroa⟩  β={beta:.2f}  f={f_coroa}")
    ax.set_ylim(-1.5, 1.5)
    ax.set_ylabel("amplitude", color="#9ca3af")
    ax.set_title("Os dois estados, separados", color="white", pad=10)
    ax.legend(fontsize=9, labelcolor="#d1d5db", facecolor="#1f2937", edgecolor="#374151")

    ax = axes[1]
    ax.plot(t, w_cara, color="tomato", lw=1, alpha=0.2)
    ax.plot(t, w_coroa, color="steelblue", lw=1, alpha=0.2)
    ax.plot(t, superposicao, color="white", lw=2.5, label="|moeda⟩ no ar — superposição")
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Em superposição: uma onda só\n(cara e coroa inseparáveis)", color="white", pad=10)
    ax.legend(fontsize=9, labelcolor="#d1d5db", facecolor="#1f2937", edgecolor="#374151")
    ax.text(
        np.pi,
        1.35,
        "não é cara  nem  coroa — é os dois ao mesmo tempo",
        ha="center",
        color="#6b7280",
        fontsize=8.5,
        style="italic",
    )

    plt.tight_layout()

    if mostrar:
        plt.show()

    return fig, axes


def mostrar_interferencia_recombinacao(mostrar: bool = True):
    """Mostra inversao de fase, recombinacao e redistribuicao de probabilidade."""
    f_cara, f_coroa = 3, 7
    t = np.linspace(0, 2 * np.pi, 600)

    def ondas(a, b):
        return a * np.sin(f_cara * t), b * np.sin(f_coroa * t)

    a1, b1 = 1 / np.sqrt(2), 1 / np.sqrt(2)
    a2, b2 = 1 / np.sqrt(2), -1 / np.sqrt(2)
    a3 = (a2 - b2) / np.sqrt(2)
    b3 = (a2 + b2) / np.sqrt(2)

    etapas = [
        (a1, b1, "superposição inicial\n50/50"),
        (a2, b2, "após inversão de fase\nainda 50/50"),
        (a3, b3, "após recombinação\ninterferência"),
    ]

    fig, axes = plt.subplots(
        2,
        3,
        figsize=(15, 5),
        facecolor="#111",
        gridspec_kw={"height_ratios": [3, 1], "hspace": 0.12, "wspace": 0.12},
    )
    fig.patch.set_facecolor("#111")

    for ax in axes.flat:
        _style_dark_axis(ax)

    for col, (a, b, titulo) in enumerate(etapas):
        ax = axes[0, col]
        wc, wco = ondas(a, b)
        ax.plot(t, wc, color="tomato", lw=2, label=f"|cara⟩   α={a:+.2f}")
        ax.plot(t, wco, color="steelblue", lw=2, label=f"|coroa⟩  β={b:+.2f}")
        ax.plot(t, wc + wco, color="white", lw=1.5, ls="--", alpha=0.5, label="soma")
        ax.axhline(0, color="#374151", lw=0.7)
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.8, 1.8)
        ax.set_xticks([])
        ax.set_yticks([-1, 0, 1])
        ax.set_title(titulo, color="white", fontsize=10, pad=10)
        ax.legend(
            fontsize=7.5,
            labelcolor="#d1d5db",
            facecolor="#1f2937",
            edgecolor="#374151",
            loc="lower right",
        )

    axes[0, 0].set_ylabel("amplitude", color="#9ca3af", fontsize=9)

    for i, operacao in enumerate(["inversão\nde fase", "recombinação"]):
        fig.text(
            0.365 + i * 0.305,
            0.78,
            "→",
            color="#f59e0b",
            fontsize=22,
            ha="center",
            va="center",
            fontweight="bold",
        )
        fig.text(
            0.365 + i * 0.305,
            0.72,
            operacao,
            color="#f59e0b",
            fontsize=8,
            ha="center",
            va="center",
            fontstyle="italic",
        )

    for col, (a, b, _) in enumerate(etapas):
        ax = axes[1, col]
        pc, pco = a**2, b**2
        ax.barh(["|coroa⟩", "|cara⟩"], [pco, pc], color=["steelblue", "tomato"], alpha=0.85, height=0.5)
        ax.axvline(0.5, color="#374151", lw=1, ls="--")
        ax.set_xlim(0, 1.05)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], color="#9ca3af", fontsize=8)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["|coroa⟩", "|cara⟩"], color="#9ca3af", fontsize=9)
        for value, y_pos in [(pc, 1), (pco, 0)]:
            if value > 0.08:
                ax.text(
                    value - 0.03,
                    y_pos,
                    f"{value:.0%}",
                    va="center",
                    ha="right",
                    color="white",
                    fontsize=9,
                    fontweight="bold",
                )
            else:
                ax.text(
                    value + 0.03,
                    y_pos,
                    f"{value:.0%}",
                    va="center",
                    ha="left",
                    color="#9ca3af",
                    fontsize=9,
                )

    plt.suptitle(
        "Interferência: inversão de fase + recombinação → probabilidade redistribuída",
        color="#9ca3af",
        fontsize=11,
        y=1.02,
    )
    plt.subplots_adjust(left=0.06, right=0.97, top=0.88, bottom=0.08)

    if mostrar:
        plt.show()

    return fig, axes
