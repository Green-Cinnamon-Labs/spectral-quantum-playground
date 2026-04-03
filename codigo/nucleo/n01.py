"""Recursos auxiliares do notebook N-01."""

from __future__ import annotations

import base64
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display


def _display_figure_centered(fig) -> None:
    """Renderiza uma figura matplotlib centralizada no notebook."""
    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight", dpi=160)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    html = f"""
    <div style="display: flex; justify-content: center; margin: 0.75rem 0;">
      <img
        src="data:image/png;base64,{encoded}"
        style="max-width: 100%; height: auto; display: block;"
      />
    </div>
    """
    display(HTML(html))
    plt.close(fig)


def _create_bloch_axes(figsize=(7.2, 6.4)):
    """Cria uma esfera de Bloch com eixos base."""
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_wireframe(x, y, z, color="#d1d5db", alpha=0.18, linewidth=0.7)

    ax.plot([-1.1, 1.1], [0, 0], [0, 0], color="0.45", lw=1)
    ax.plot([0, 0], [-1.1, 1.1], [0, 0], color="0.45", lw=1)
    ax.plot([0, 0], [0, 0], [-1.1, 1.1], color="0.45", lw=1)
    ax.text(1.15, 0, 0, "X", color="0.35")
    ax.text(0, 1.15, 0, "Y", color="0.35")
    ax.text(0, 0, 1.15, "Z", color="0.35")

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.set_box_aspect((1, 1, 1))
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    ax.view_init(elev=22, azim=35)

    return fig, ax


def _normalize_qubit_state(alpha: complex, beta: complex):
    """Normaliza um estado de qubit."""
    norm = np.sqrt(np.abs(alpha) ** 2 + np.abs(beta) ** 2)
    if np.isclose(norm, 0):
        raise ValueError("alpha e beta não podem ser ambos zero.")
    return alpha / norm, beta / norm


def _bloch_vector_from_state(alpha: complex, beta: complex):
    """Converte |psi> = alpha|0> + beta|1> em coordenadas de Bloch."""
    alpha, beta = _normalize_qubit_state(alpha, beta)
    produto = np.conjugate(alpha) * beta
    x = 2 * np.real(produto)
    y = 2 * np.imag(produto)
    z = np.abs(alpha) ** 2 - np.abs(beta) ** 2
    return np.array([x, y, z], dtype=float), alpha, beta


def plot_vetor_45_graus(
    modulo: float = 1.0,
    mostrar_texto: bool = True,
    ax=None,
    centralizar: bool = False,
):
    """Desenha um vetor a 45 graus com projecoes em x e y."""
    theta = np.deg2rad(45)
    vx = modulo * np.cos(theta)
    vy = modulo * np.sin(theta)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    else:
        fig = ax.figure

    ax.set_aspect("equal")
    ax.axhline(0, color="0.35", lw=1)
    ax.axvline(0, color="0.35", lw=1)

    ax.arrow(
        0,
        0,
        vx,
        vy,
        length_includes_head=True,
        head_width=0.045 * modulo,
        head_length=0.06 * modulo,
        linewidth=2.5,
        color="#2563eb",
    )

    ax.plot([vx, vx], [0, vy], "--", color="#f59e0b", lw=1.8)
    ax.plot([0, vx], [vy, vy], "--", color="#10b981", lw=1.8)
    ax.scatter([vx], [vy], color="#2563eb", s=45)

    phi = np.linspace(0, theta, 100)
    ax.plot(0.18 * np.cos(phi), 0.18 * np.sin(phi), color="0.45")
    ax.text(0.21, 0.08, r"$45^\circ$", color="0.35")

    ax.text(vx / 2 - 0.02, vy / 2 + 0.06, r"$|\vec{v}| = 1$", color="#2563eb")
    ax.text(
        vx / 2,
        -0.12,
        r"$v_x = \cos 45^\circ = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$",
        ha="center",
        color="#f59e0b",
    )
    ax.text(
        vx + 0.08,
        vy / 2,
        r"$v_y = \sin 45^\circ = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$",
        va="center",
        color="#10b981",
    )
    ax.text(
        vx + 0.02,
        vy + 0.03,
        r"$\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$",
        color="#1d4ed8",
    )

    ax.set_xlim(-0.15, 1.15)
    ax.set_ylim(-0.18, 1.15)
    ax.set_xticks([0, vx, 1])
    ax.set_yticks([0, vy, 1])
    ax.set_xticklabels(["0", r"$\frac{1}{\sqrt{2}}$", "1"])
    ax.set_yticklabels(["0", r"$\frac{1}{\sqrt{2}}$", "1"])
    ax.set_xlabel("eixo x")
    ax.set_ylabel("eixo y")
    ax.set_title("Vetor unitario a 45 graus e suas projecoes")
    ax.grid(alpha=0.2)

    if mostrar_texto:
        print(f"vx = {vx:.4f}  |  vy = {vy:.4f}")
        print("Para um vetor unitario em 45 graus:")
        print("cos(45) = sin(45) = 1/sqrt(2) = sqrt(2)/2")

    if centralizar and ax is None:
        _display_figure_centered(fig)

    return fig, ax


def plot_vetor_projecoes_desiguais(
    prob_x: float = 0.75,
    prob_y: float = 0.25,
    mostrar_texto: bool = True,
    ax=None,
    centralizar: bool = False,
):
    """Desenha um vetor unitario cujas projecoes ao quadrado sao 75% e 25%."""
    if not np.isclose(prob_x + prob_y, 1.0):
        raise ValueError("prob_x + prob_y deve somar 1 para formar um vetor unitario.")

    vx = np.sqrt(prob_x)
    vy = np.sqrt(prob_y)
    theta = np.arctan2(vy, vx)
    theta_deg = np.degrees(theta)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6.4, 6))
    else:
        fig = ax.figure

    ax.set_aspect("equal")
    ax.axhline(0, color="0.35", lw=1)
    ax.axvline(0, color="0.35", lw=1)

    ax.arrow(
        0,
        0,
        vx,
        vy,
        length_includes_head=True,
        head_width=0.04,
        head_length=0.055,
        linewidth=2.5,
        color="#2563eb",
    )

    ax.plot([vx, vx], [0, vy], "--", color="#f59e0b", lw=1.8)
    ax.plot([0, vx], [vy, vy], "--", color="#10b981", lw=1.8)
    ax.scatter([vx], [vy], color="#2563eb", s=45)

    phi = np.linspace(0, theta, 100)
    ax.plot(0.18 * np.cos(phi), 0.18 * np.sin(phi), color="0.45")
    ax.text(0.2, 0.06, rf"${theta_deg:.0f}^\circ$", color="0.35")

    ax.text(vx / 2 - 0.03, vy / 2 + 0.04, r"$|\vec{v}| = 1$", color="#2563eb")
    ax.text(
        vx / 2,
        -0.12,
        r"$v_x^2 = 0.75 \;\Rightarrow\; v_x = \sqrt{0.75} = \frac{\sqrt{3}}{2}$",
        ha="center",
        color="#f59e0b",
    )
    ax.text(
        vx + 0.05,
        vy / 2,
        r"$v_y^2 = 0.25 \;\Rightarrow\; v_y = \sqrt{0.25} = \frac{1}{2}$",
        va="center",
        color="#10b981",
    )
    ax.text(
        vx + 0.02,
        vy + 0.025,
        r"$\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$",
        color="#1d4ed8",
    )
    ax.text(
        0.53,
        1.02,
        "Mesmo vetor unitario,\nmas com inclinacao diferente de 45 graus",
        color="#6b7280",
        fontsize=9,
        ha="center",
    )

    ax.set_xlim(-0.12, 1.15)
    ax.set_ylim(-0.18, 1.18)
    ax.set_xticks([0, 0.5, vx, 1])
    ax.set_yticks([0, vy, 1])
    ax.set_xticklabels(["0", r"$\frac{1}{2}$", r"$\frac{\sqrt{3}}{2}$", "1"])
    ax.set_yticklabels(["0", r"$\frac{1}{2}$", "1"])
    ax.set_xlabel("eixo x")
    ax.set_ylabel("eixo y")
    ax.set_title("Vetor unitario com projecoes 75% em x e 25% em y")
    ax.grid(alpha=0.2)

    if mostrar_texto:
        print(f"vx = {vx:.4f}  |  vy = {vy:.4f}")
        print("Para um vetor unitario com projeções desiguais:")
        print("vx² = 75%  e  vy² = 25%")
        print(f"Isso inclina o vetor para {theta_deg:.0f} graus, e não 45 graus.")

    if centralizar and ax is None:
        _display_figure_centered(fig)

    return fig, ax


def plot_numero_complexo_como_vetor(
    x: float = np.sqrt(3) / 2,
    y: float = 1 / 2,
    mostrar_texto: bool = True,
    centralizar: bool = False,
):
    """
    Mostra que um único número complexo z = x + iy já pode ser visto
    como um vetor no plano complexo.

    A ideia central é contrastar:
    - em R, um número -> reta
    - em C, um número -> plano (porque tem parte real e imaginária)
    """

    z = x + 1j * y
    modulo = np.abs(z)
    fase = np.angle(z)
    fase_graus = np.degrees(fase)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    ax1, ax2 = axes

    # ----------------------------
    # Painel 1: z como vetor no plano
    # ----------------------------
    ax1.set_aspect("equal")
    ax1.axhline(0, color="0.35", lw=1)
    ax1.axvline(0, color="0.35", lw=1)

    ax1.arrow(
        0,
        0,
        x,
        y,
        length_includes_head=True,
        head_width=0.04,
        head_length=0.055,
        linewidth=2.5,
        color="#2563eb",
    )

    ax1.plot([x, x], [0, y], "--", color="#f59e0b", lw=1.8)
    ax1.plot([0, x], [y, y], "--", color="#10b981", lw=1.8)
    ax1.scatter([x], [y], color="#2563eb", s=45)

    arco = np.linspace(0, fase, 120)
    raio_arco = 0.18
    ax1.plot(raio_arco * np.cos(arco), raio_arco * np.sin(arco), color="0.45")
    ax1.text(0.21, 0.05, rf"${fase_graus:.0f}^\circ$", color="0.35")

    ax1.text(x / 2, -0.12, rf"$\Re(z) = {x:.2f}$", ha="center", color="#f59e0b")
    ax1.text(x + 0.05, y / 2, rf"$\Im(z) = {y:.2f}$", va="center", color="#10b981")
    ax1.text(x / 2 - 0.02, y / 2 + 0.05, rf"$|z| = {modulo:.2f}$", color="#2563eb")

    ax1.set_xlim(-0.12, 1.12)
    ax1.set_ylim(-0.18, 1.12)
    ax1.set_xticks([0, 0.5, 1.0])
    ax1.set_yticks([0, 0.5, 1.0])
    ax1.set_xlabel("parte real")
    ax1.set_ylabel("parte imaginária")
    ax1.set_title("Um número complexo já é um vetor no plano")
    ax1.grid(alpha=0.2)

    # ----------------------------
    # Painel 2: mesmo módulo, fases diferentes
    # ----------------------------
    ax2.set_aspect("equal")
    theta = np.linspace(0, 2 * np.pi, 400)
    ax2.plot(modulo * np.cos(theta), modulo * np.sin(theta), "--", color="#9ca3af", lw=1.5)

    angulos = np.deg2rad([30, 75, 150, 300])
    cores = ["#2563eb", "#10b981", "#f59e0b", "#ef4444"]

    for idx, (ang, cor) in enumerate(zip(angulos, cores), start=1):
        zx = modulo * np.cos(ang)
        zy = modulo * np.sin(ang)

        ax2.arrow(
            0,
            0,
            zx,
            zy,
            length_includes_head=True,
            head_width=0.035,
            head_length=0.05,
            linewidth=2,
            color=cor,
        )
        ax2.scatter([zx], [zy], color=cor, s=35)
        ax2.text(
            zx + 0.05 * np.sign(zx if zx != 0 else 1),
            zy + 0.05 * np.sign(zy if zy != 0 else 1),
            rf"$z_{idx}$",
            color=cor,
        )

    ax2.axhline(0, color="0.35", lw=1)
    ax2.axvline(0, color="0.35", lw=1)

    ax2.text(
        0,
        -1.15,
        r"$z = |z| e^{i\phi}$",
        ha="center",
        color="#374151",
    )
    ax2.text(
        0,
        1.12,
        "O módulo fica fixo; o que muda é a fase",
        ha="center",
        color="#6b7280",
        fontsize=9,
    )

    lim = max(1.2, modulo + 0.25)
    ax2.set_xlim(-lim, lim)
    ax2.set_ylim(-lim, lim)
    ax2.set_xticks([-1, 0, 1])
    ax2.set_yticks([-1, 0, 1])
    ax2.set_xlabel("parte real")
    ax2.set_ylabel("parte imaginária")
    ax2.set_title("Um número complexo tem módulo e fase")
    ax2.grid(alpha=0.2)

    plt.suptitle("Um único número complexo carrega dois graus de liberdade reais", y=0.98)
    plt.tight_layout()

    if mostrar_texto:
        print(f"z = {x:.3f} + {y:.3f}i")
        print(f"|z| = {modulo:.3f}")
        print(f"fase(z) = {fase_graus:.1f}°")
        print("Em R, um número ocupa uma reta.")
        print("Em C, um número já ocupa o plano porque tem parte real e imaginária.")

    if centralizar:
        _display_figure_centered(fig)

    return fig, axes

# depreciado, mas mantido para referência histórica
def plot_estado_complexo_fase_livre(
    prob_alpha: float = 0.75,
    prob_beta: float = 0.25,
    mostrar_texto: bool = True,
    centralizar: bool = False,
):
    """Mostra a liberdade de fase em um estado complexo com probabilidades fixas."""
    if not np.isclose(prob_alpha + prob_beta, 1.0):
        raise ValueError("prob_alpha + prob_beta deve somar 1.")

    alpha = np.sqrt(prob_alpha)
    beta_mag = np.sqrt(prob_beta)
    vetor_theta = np.degrees(np.arctan2(beta_mag, alpha))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    ax1, ax2 = axes

    ax1.set_aspect("equal")
    ax1.axhline(0, color="0.35", lw=1)
    ax1.axvline(0, color="0.35", lw=1)
    ax1.arrow(
        0,
        0,
        alpha,
        beta_mag,
        length_includes_head=True,
        head_width=0.04,
        head_length=0.055,
        linewidth=2.5,
        color="#2563eb",
    )
    ax1.plot([alpha, alpha], [0, beta_mag], "--", color="#f59e0b", lw=1.8)
    ax1.plot([0, alpha], [beta_mag, beta_mag], "--", color="#10b981", lw=1.8)
    ax1.scatter([alpha], [beta_mag], color="#2563eb", s=45)
    phi_arc = np.linspace(0, np.arctan2(beta_mag, alpha), 100)
    ax1.plot(0.18 * np.cos(phi_arc), 0.18 * np.sin(phi_arc), color="0.45")
    ax1.text(0.2, 0.05, rf"${vetor_theta:.0f}^\circ$", color="0.35")
    ax1.text(alpha / 2, -0.12, r"$|\alpha|^2 = 0.75 \Rightarrow |\alpha| = \frac{\sqrt{3}}{2}$", ha="center", color="#f59e0b")
    ax1.text(alpha + 0.05, beta_mag / 2, r"$|\beta|^2 = 0.25 \Rightarrow |\beta| = \frac{1}{2}$", va="center", color="#10b981")
    ax1.text(alpha / 2 - 0.05, beta_mag / 2 + 0.05, r"$\|\psi\| = 1$", color="#2563eb")
    ax1.set_xlim(-0.12, 1.12)
    ax1.set_ylim(-0.18, 1.12)
    ax1.set_xticks([0, beta_mag, alpha, 1])
    ax1.set_yticks([0, beta_mag, 1])
    ax1.set_xticklabels(["0", r"$\frac{1}{2}$", r"$\frac{\sqrt{3}}{2}$", "1"])
    ax1.set_yticklabels(["0", r"$\frac{1}{2}$", "1"])
    ax1.set_xlabel("parte de |0⟩")
    ax1.set_ylabel("tamanho de |1⟩")
    ax1.set_title("Mesmas probabilidades, inclinação diferente")
    ax1.grid(alpha=0.2)

    ax2.set_aspect("equal")
    theta = np.linspace(0, 2 * np.pi, 400)
    ax2.plot(np.cos(theta), np.sin(theta), "--", color="#9ca3af", lw=1.2, label=r"$|e^{i\phi}| = 1$")
    ax2.plot(beta_mag * np.cos(theta), beta_mag * np.sin(theta), color="#2563eb", lw=2, label=r"$|\beta| = \frac{1}{2}$")
    quadrantes = np.deg2rad([45, 135, 225, 315])
    cores = ["#2563eb", "#10b981", "#f59e0b", "#ef4444"]
    for idx, (ang, cor) in enumerate(zip(quadrantes, cores), start=1):
        bx = beta_mag * np.cos(ang)
        by = beta_mag * np.sin(ang)
        ax2.arrow(0, 0, bx, by, length_includes_head=True, head_width=0.035, head_length=0.05, linewidth=2, color=cor)
        ax2.scatter([bx], [by], color=cor, s=35)
        ax2.text(bx + 0.05 * np.sign(bx if bx != 0 else 1), by + 0.05 * np.sign(by if by != 0 else 1), rf"$\phi_{idx}$", color=cor)
    ax2.axhline(0, color="0.35", lw=1)
    ax2.axvline(0, color="0.35", lw=1)
    ax2.text(
        0,
        -1.15,
        r"$|\psi(\phi)\rangle = \frac{\sqrt{3}}{2}|0\rangle + \frac{1}{2}e^{i\phi}|1\rangle$",
        ha="center",
        color="#374151",
    )
    ax2.text(0, 1.12, "A fase gira por todos os quadrantes\nsem mudar 75/25", ha="center", color="#6b7280", fontsize=9)
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.25, 1.2)
    ax2.set_xticks([-1, 0, 1])
    ax2.set_yticks([-1, 0, 1])
    ax2.set_xlabel("parte real")
    ax2.set_ylabel("parte imaginária")
    ax2.set_title("Um grau de liberdade: a fase relativa φ")
    ax2.legend(loc="upper right", fontsize=8)
    ax2.grid(alpha=0.2)

    plt.suptitle("Estado complexo com norma 1 e probabilidades fixas em 75% / 25%", y=0.98)
    plt.tight_layout()

    if mostrar_texto:
        print(r"|ψ(φ)⟩ = (√3/2)|0⟩ + (1/2)e^{iφ}|1⟩")
        print("Quando φ muda, a fase gira pelo plano complexo.")
        print("Mas |α|² = 75% e |β|² = 25% continuam iguais.")

    if centralizar:
        _display_figure_centered(fig)

    return fig, axes


def plot_esfera_bloch_probabilidades_fixas(
    prob_alpha: float = 0.75,
    prob_beta: float = 0.25,
):
    import numpy as np
    import matplotlib.pyplot as plt

    if not np.isclose(prob_alpha + prob_beta, 1.0):
        raise ValueError("prob_alpha + prob_beta deve somar 1.")

    alpha = np.sqrt(prob_alpha)

    theta = 2 * np.arccos(alpha)
    z_lat = np.cos(theta)
    r_lat = np.sin(theta)

    fig = plt.figure(figsize=(7.2, 6.2))
    ax = fig.add_subplot(111, projection="3d")

    # ----------------------------
    # Esfera (bem leve, fundo)
    # ----------------------------
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)

    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    ax.plot_wireframe(
        x, y, z,
        color="#9ca3af",
        alpha=0.12,
        linewidth=0.6
    )

    # ----------------------------
    # Linha vertical (fixo)
    # ----------------------------
    ax.plot([0, 0], [0, 0], [0, z_lat], color="#ef4444", lw=2)
    ax.scatter(0, 0, z_lat, color="#ef4444", s=55)
    ax.text(0, 0, z_lat + 0.08, "altura fixa", ha="center", color="#ef4444")

    # ----------------------------
    # Latitude (principal)
    # ----------------------------
    ax.plot(
        r_lat * np.cos(u),
        r_lat * np.sin(u),
        np.full_like(u, z_lat),
        color="#2563eb",
        lw=3.2,
    )

    # ----------------------------
    # Vetores (φ variando)
    # ----------------------------
    phis = np.linspace(0, 2*np.pi, 5, endpoint=False)

    for phi in phis:
        px = r_lat * np.cos(phi)
        py = r_lat * np.sin(phi)
        pz = z_lat

        # vetor suave (menos dominante)
        ax.plot(
            [0, px], [0, py], [0, pz],
            color="#2563eb",
            alpha=0.45,
            lw=1.8
        )

        ax.scatter(px, py, pz, color="#2563eb", s=35)

    # ----------------------------
    # Eixos simples
    # ----------------------------
    ax.plot([-1, 1], [0, 0], [0, 0], color="0.4", lw=1)
    ax.plot([0, 0], [-1, 1], [0, 0], color="0.4", lw=1)
    ax.plot([0, 0], [0, 0], [-1, 1], color="0.4", lw=1)

    ax.text(1.05, 0, 0, "X")
    ax.text(0, 1.05, 0, "Y")
    ax.text(0, 0, 1.05, "Z")

    # ----------------------------
    # Limpeza visual (IMPORTANTE)
    # ----------------------------
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)

    ax.set_box_aspect((1, 1, 1))

    # REMOVE o warning (não usar tight_layout em 3D)
    plt.subplots_adjust(top=0.88)

    ax.set_title("Fixar probabilidade → fixa altura | φ gira ao redor")

    return fig, ax

# depreciado, mas mantido para referência histórica
def plot_esfera_bloch_probabilidades_fixas_v1(
    prob_alpha: float = 0.75,
    prob_beta: float = 0.25,
    mostrar_texto: bool = True,
    centralizar: bool = False,
):
    """Mostra na esfera de Bloch a latitude de estados que preservam 75/25 na base Z."""
    if not np.isclose(prob_alpha + prob_beta, 1.0):
        raise ValueError("prob_alpha + prob_beta deve somar 1.")

    theta = 2 * np.arccos(np.sqrt(prob_alpha))
    z_lat = np.cos(theta)
    r_lat = np.sin(theta)

    fig = plt.figure(figsize=(7.2, 6.4))
    ax = fig.add_subplot(111, projection="3d")

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_wireframe(x, y, z, color="#d1d5db", alpha=0.18, linewidth=0.7)

    ax.plot(
        r_lat * np.cos(u),
        r_lat * np.sin(u),
        np.full_like(u, z_lat),
        color="#2563eb",
        lw=2.6,
        label="latitude com 75% / 25%",
    )

    amostras = np.deg2rad([45, 135, 225, 315])
    cores = ["#2563eb", "#10b981", "#f59e0b", "#ef4444"]
    for idx, (phi, cor) in enumerate(zip(amostras, cores), start=1):
        px = r_lat * np.cos(phi)
        py = r_lat * np.sin(phi)
        pz = z_lat
        ax.scatter([px], [py], [pz], color=cor, s=40)
        ax.plot([0, px], [0, py], [0, pz], color=cor, alpha=0.8, lw=1.5)
        ax.text(px * 1.08, py * 1.08, pz + 0.03, rf"$\phi_{idx}$", color=cor)

    ax.plot([-1.1, 1.1], [0, 0], [0, 0], color="0.45", lw=1)
    ax.plot([0, 0], [-1.1, 1.1], [0, 0], color="0.45", lw=1)
    ax.plot([0, 0], [0, 0], [-1.1, 1.1], color="0.45", lw=1)
    ax.text(1.15, 0, 0, "X", color="0.35")
    ax.text(0, 1.15, 0, "Y", color="0.35")
    ax.text(0, 0, 1.15, "Z", color="0.35")
    ax.text(0, 0, z_lat + 0.08, "mesma latitude\nmesmas probabilidades em Z", ha="center", color="#2563eb")

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_zlim(-1.1, 1.1)
    ax.set_box_aspect((1, 1, 1))
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, z_lat, 1])
    ax.set_zticklabels(["-1", "0", f"{z_lat:.1f}", "1"])
    ax.view_init(elev=22, azim=35)
    ax.set_title("Dois graus de liberdade: a esfera de Bloch")
    ax.legend(loc="upper left", fontsize=8)

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.94)

    if mostrar_texto:
        print("Na esfera de Bloch, um estado puro precisa de dois parâmetros: θ e φ.")
        print("Fixar 75% em |0⟩ e 25% em |1⟩ prende o estado a uma latitude.")
        print("Ao variar φ, surgem infinitas configurações diferentes com a mesma estatística em Z.")

    if centralizar:
        _display_figure_centered(fig)

    return fig, ax


def plot_esfera_bloch_estados_base(
    mostrar_texto: bool = True,
    centralizar: bool = False,
):
    """Mostra |0> e |1> como os polos da esfera de Bloch."""
    fig, ax = _create_bloch_axes()

    ax.quiver(0, 0, 0, 0, 0, 1, color="#2563eb", linewidth=2.6, arrow_length_ratio=0.12)
    ax.quiver(0, 0, 0, 0, 0, -1, color="#ef4444", linewidth=2.6, arrow_length_ratio=0.12)
    ax.scatter([0, 0], [0, 0], [1, -1], color=["#2563eb", "#ef4444"], s=45)

    ax.text(0, 0, 1.08, r"$|0\rangle$", color="#2563eb", ha="center")
    ax.text(0, 0, -1.16, r"$|1\rangle$", color="#ef4444", ha="center")
    ax.text(0.05, 0.05, 0.62, r"$|0\rangle \rightarrow (0,0,1)$", color="#2563eb")
    ax.text(0.05, 0.05, -0.78, r"$|1\rangle \rightarrow (0,0,-1)$", color="#ef4444")
    ax.set_title("Na esfera de Bloch, |0⟩ e |1⟩ são os polos")

    if mostrar_texto:
        print("|0⟩ fica no polo norte da esfera de Bloch.")
        print("|1⟩ fica no polo sul da esfera de Bloch.")
        print("Eles são os estados-base da base computacional.")

    if centralizar:
        _display_figure_centered(fig)

    return fig, ax


def plot_esfera_bloch_estado_superposto(
    alpha: complex = np.sqrt(0.75),
    beta: complex = 0.5,
    mostrar_texto: bool = True,
    centralizar: bool = False,
):
    """Mostra |psi> = alpha|0> + beta|1> como vetor na esfera de Bloch."""
    bloch, alpha, beta = _bloch_vector_from_state(alpha, beta)
    x, y, z = bloch

    fig, ax = _create_bloch_axes()

    ax.quiver(0, 0, 0, x, y, z, color="#7c3aed", linewidth=2.8, arrow_length_ratio=0.12)
    ax.scatter([x], [y], [z], color="#7c3aed", s=50)
    ax.scatter([0, 0], [0, 0], [1, -1], color=["#2563eb", "#ef4444"], s=25, alpha=0.55)
    ax.text(0, 0, 1.08, r"$|0\rangle$", color="#2563eb", ha="center", alpha=0.8)
    ax.text(0, 0, -1.16, r"$|1\rangle$", color="#ef4444", ha="center", alpha=0.8)
    ax.text(x * 1.08, y * 1.08, z + 0.05, r"$|\psi\rangle$", color="#7c3aed")

    ax.text(
        0,
        -1.28,
        -1.18,
        rf"$|\psi\rangle = ({alpha.real:.3f}{alpha.imag:+.3f}i)|0\rangle + ({beta.real:.3f}{beta.imag:+.3f}i)|1\rangle$",
        color="#374151",
        ha="center",
    )
    ax.text(
        0,
        0,
        z + 0.16,
        rf"$|α|^2 = {np.abs(alpha)**2:.2f}$" "\n" rf"$|β|^2 = {np.abs(beta)**2:.2f}$",
        ha="center",
        color="#6b7280",
    )
    ax.set_title("O estado |ψ⟩ é a composição de α|0⟩ + β|1⟩")

    if mostrar_texto:
        print(
            f"|ψ⟩ = ({alpha.real:.4f}{alpha.imag:+.4f}i)|0⟩ + "
            f"({beta.real:.4f}{beta.imag:+.4f}i)|1⟩"
        )
        print(f"|α|² = {np.abs(alpha)**2:.2f}  |  |β|² = {np.abs(beta)**2:.2f}")
        print(f"Vetor de Bloch: ({x:.3f}, {y:.3f}, {z:.3f})")

    if centralizar:
        _display_figure_centered(fig)

    return fig, ax
