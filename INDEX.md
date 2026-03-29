# INDEX

Mapa de navegação do repositório. Atualizar sempre que um notebook for criado ou concluído.

---

## Trilha Core

Linha narrativa principal. Cada notebook responde perguntas explícitas do [QUESTIONS.md](QUESTIONS.md).
Leitura sequencial recomendada — pré-requisitos indicados no header de cada notebook.

| ID | Título | Perguntas | Digressões | Matemática | Status |
|---|---|---|---|---|---|
| [C-01](core/C-01_states_operators_measurements.ipynb) | States, Operators, Measurements | Q-F1, Q-F3 | D-01, D-02 | M-01 | rascunho |
| [C-02](core/C-02_unitaries_spectrum_dynamics.ipynb) | Unitaries, Spectrum, Dynamics | Q-F2, Q-S1 | — | M-01 | rascunho |
| [C-03](core/C-03_phase_kickback.ipynb) | Phase Kickback | Q-F4 | D-02 | — | rascunho |
| [C-04](core/C-04_phase_estimation.ipynb) | Phase Estimation | Q-C1, Q-C2, Q-S3 | D-03 | M-02 | rascunho |
| [C-05](core/C-05_hamiltonian_simulation.ipynb) | Hamiltonian Simulation | Q-T2 | D-03 | M-01 | rascunho ⚠️ provisional |
| [C-06](core/C-06_problem_translation.ipynb) | Problem Translation | Q-C3, Q-T1, Q-T4, Q-T5 | — | — | rascunho |
| [C-07](core/C-07_singular_values_vs_eigenvalues.ipynb) | Singular Values vs. Eigenvalues | Q-S2, Q-T3 | D-04 | M-03 | rascunho |
| [C-08](core/C-08_qsp_qsvt_entry_point.ipynb) | QSP / QSVT Entry Point | Q-B1, Q-B2, Q-B3 | D-04 | M-02, M-03 | rascunho |

> ⚠️ **C-05 — decisão aberta:** Hamiltonian simulation pode migrar para digressão D-05 dependendo de como C-06 se desenvolver. Reavaliar ao fechar C-06.

---

## Digressions

Notebooks curtos e instrumentais. Destravem dependências conceituais sem tentar esgotar o tema.
Estrutura obrigatória: definição mínima → por que importa aqui → exemplo pequeno.

| ID | Título | Referenciado por | Status |
|---|---|---|---|
| [D-01](digressions/D-01_born_rule_and_collapse.ipynb) | Born Rule e Colapso | C-01 | esqueleto |
| [D-02](digressions/D-02_tensor_products.ipynb) | Produtos Tensoriais | C-01, C-03 | esqueleto |
| [D-03](digressions/D-03_commutators_and_trotter_error.ipynb) | Comutadores e Erro de Trotter | C-04, C-05 | esqueleto |
| [D-04](digressions/D-04_block_encoding_minimal.ipynb) | Block-Encoding Minimal | C-07, C-08 | esqueleto |

---

## Mathematics

Exploração matemática com vínculo explícito com algoritmos quânticos.
Não é pré-requisito bloqueante por padrão — exceto quando explicitamente marcado como estrutural em um C-notebook.
Última seção obrigatória: **"Por que isso importa para algoritmos quânticos?"**

| ID | Título | Vínculo com core | Status |
|---|---|---|---|
| [M-01](mathematics/M-01_spectral_theory_operators.ipynb) | Spectral Theory of Operators | C-02, C-04, C-05 | esqueleto |
| [M-02](mathematics/M-02_polynomial_approximation.ipynb) | Polynomial Approximation | C-08 (QSP) | esqueleto |
| [M-03](mathematics/M-03_svd_geometry.ipynb) | SVD: Geometria e Interpretação | C-07, C-08 | esqueleto |

---

## Mapa de perguntas → notebooks

| Pergunta | Notebook |
|---|---|
| Q-C1 | C-04 |
| Q-C2 | C-04 |
| Q-C3 | C-06 |
| Q-F1 | C-01 |
| Q-F2 | C-02 |
| Q-F3 | C-01 |
| Q-F4 | C-03 |
| Q-S1 | C-02 |
| Q-S2 | C-07 |
| Q-S3 | C-04 |
| Q-T1 | C-06 |
| Q-T2 | C-05 ⚠️ |
| Q-T3 | C-07 |
| Q-T4 | C-06 |
| Q-T5 | C-06, C-08 |
| Q-B1 | C-08 |
| Q-B2 | C-08 |
| Q-B3 | C-08 |

---

## Convenções de status

| Status | Significado |
|---|---|
| `esqueleto` | Arquivo criado, estrutura definida, sem conteúdo real |
| `rascunho` | Conteúdo escrito, não revisado |
| `revisado` | Conteúdo revisado e pergunta verificada como respondida |
| `fechado` | Pergunta marcada como respondida em QUESTIONS.md |
