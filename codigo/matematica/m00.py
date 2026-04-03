"""Recursos auxiliares do notebook M-00."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def testar_axiomas_r2():
    """Testa alguns axiomas de espaco vetorial em R^2."""

    def testa(nome, condicao):
        print(f"{nome}: {'funcionou' if condicao else 'NÃO funcionou'}")

    u = np.array([-4.0, 2.0])
    v = np.array([2.0, 3.0])
    w = np.array([1.0, -1.0])
    a = 2.0
    b = -0.5
    zero = np.zeros(2)

    print("=== Testando axiomas em R^2 ===\n")
    testa("Comutatividade", np.allclose(v + w, w + v))
    testa("Associatividade", np.allclose((u + v) + w, u + (v + w)))
    testa("Neutro aditivo", np.allclose(v + zero, v))
    testa("Inverso aditivo", np.allclose(v + (-v), zero))
    testa("Distributividade (vetores)", np.allclose(a * (v + w), a * v + a * w))
    testa("Distributividade (escalares)", np.allclose((a + b) * v, a * v + b * v))
    print("\nConclusão: tudo funcionou → isso é um espaço vetorial.\n")


def plotar_falha_fechamento_disco(mostrar: bool = True):
    """Mostra um conjunto fechado por norma que falha ao somar vetores."""
    v = np.array([1.5, 0.5])
    w = np.array([0.5, 1.5])
    soma = v + w

    fig, ax = plt.subplots(figsize=(5, 5))

    circle = plt.Circle((0, 0), 2, color="lightblue", alpha=0.2)
    ax.add_patch(circle)

    def seta(vetor, cor, label):
        ax.quiver(0, 0, vetor[0], vetor[1], angles="xy", scale_units="xy", scale=1, color=cor, label=label)

    seta(v, "blue", "v (válido)")
    seta(w, "green", "w (válido)")
    seta(soma, "red", "v + w (inválido)")

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.axhline(0)
    ax.axvline(0)
    ax.set_title("Falha de fechamento: soma sai do conjunto")
    ax.legend()

    if mostrar:
        plt.show()

    return fig, ax


def demonstrar_fechamento_vs_quadrante():
    """Contrasta R^2 com o quadrante positivo."""
    a = np.array([1.0, 2.0])
    b = np.array([-2.0, 1.0])
    print("a + b:", a + b)
    print("7.3a:", 7.3 * a)
    print()

    x = np.array([1.0, 2.0])
    y = np.array([-2.0, 1.0])
    result = x + y
    print(f"x + y = {result}")
    print(f"Primeiro componente {result[0]:.0f} < 0: saiu do quadrante positivo.")
    print("-> o quadrante positivo NÃO é espaço vetorial.")


def comparar_evolucao_fase_real_complexo(mostrar: bool = True):
    """Compara fase em representacao real e complexa."""
    print("=== Evolução de fase: real vs complexo ===\n")

    theta0 = np.pi / 6
    dtheta = np.pi / 8
    steps = 8

    x_real = np.array([np.cos(theta0), np.sin(theta0)])
    z = np.exp(1j * theta0)

    rotation = np.array(
        [
            [np.cos(dtheta), -np.sin(dtheta)],
            [np.sin(dtheta), np.cos(dtheta)],
        ]
    )

    real_points = [x_real.copy()]
    complex_points = [z]

    for _ in range(steps):
        x_real = rotation @ x_real
        z = np.exp(1j * dtheta) * z
        real_points.append(x_real.copy())
        complex_points.append(z)

    real_points = np.array(real_points)
    complex_points = np.array(complex_points)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(real_points[:, 0], real_points[:, 1], "o-", label="real: [cosθ, sinθ]")
    ax.plot(complex_points.real, complex_points.imag, "s--", label="complexo: e^{iθ}")
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_aspect("equal")
    ax.set_title("Mesma rotação, duas representações")
    ax.set_xlabel("x / parte real")
    ax.set_ylabel("y / parte imaginária")
    ax.legend()

    if mostrar:
        plt.show()

    print("Conclusão:")
    print("Nos reais, a fase precisa ser carregada por 2 números e atualizada por uma matriz.")
    print("Nos complexos, a fase já vem embutida em 1 número e evoluir vira uma multiplicação.")

    return fig, ax


def demonstrar_sequencia_cauchy(mostrar: bool = True):
    """Mostra uma sequencia de Cauchy simples."""
    print("=== Sequência de Cauchy ===\n")

    n = np.arange(1, 30)
    x = 1 + 1 / n
    diffs = np.abs(np.diff(x))

    print("Últimos termos da sequência:")
    print(x[-5:])
    print()

    print("Diferença entre termos consecutivos (últimos):")
    print(diffs[-5:])
    print()

    print("Conclusão: os termos ficam cada vez mais próximos → sequência de Cauchy")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(n, x, "o-", label="x_n")
    ax.axhline(1, linestyle="--", label="limite = 1")
    ax.set_title("Sequência x_n = 1 + 1/n converge para 1")
    ax.set_xlabel("n")
    ax.set_ylabel("x_n")
    ax.legend()
    ax.grid()

    if mostrar:
        plt.show()

    return fig, ax


def demonstrar_produto_interno_c2():
    """Calcula produto interno, norma e projeção em C^2."""
    print("=== Produto interno em C^2 ===\n")

    u = np.array([1 + 1j, 2 - 1j])
    v = np.array([2 - 1j, -1 + 2j])

    inner = np.dot(u.conj(), v)
    print("⟨u, v⟩ =", inner)

    norm_u = np.sqrt(np.dot(u.conj(), u))
    norm_v = np.sqrt(np.dot(v.conj(), v))
    print("\nNormas:")
    print("||u|| =", norm_u)
    print("||v|| =", norm_v)

    print("\nOrtogonalidade:")
    if np.allclose(inner, 0):
        print("u ⟂ v (ortogonais)")
    else:
        print("u e v NÃO são ortogonais")

    proj = (np.dot(u.conj(), v) / np.dot(u.conj(), u)) * u
    print("\nProjeção de v em u:")
    print("proj_u(v) =", proj)

    erro = v - proj
    print("\nParte de v fora da direção de u:")
    print("v - proj =", erro)
