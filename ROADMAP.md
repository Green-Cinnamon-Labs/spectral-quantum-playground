# Roadmap

## Milestone 1 — Linguagem mínima do problema quântico

**Estado de entrada:** curiosidade real formada, mas vocabulário básico ainda sendo consolidado. Estado, operador, unitário, observável e medição ainda se confundem às vezes.

**O que este milestone introduz:** um núcleo mínimo de álgebra linear e circuito quântico suficiente para formular perguntas sem confusão conceitual.

**Goal:** move from "portas e qubits como objetos soltos" to "problemas formulados como estados + operadores + medição".

**Notebooks:**
- [ ] [C-01](core/C-01_states_operators_measurements.ipynb) — linguagem fundamental
- [ ] [C-02](core/C-02_unitaries_spectrum_dynamics.ipynb) — por que unitário importa

**Perguntas cobertas:** Q-F1, Q-F2, Q-F3

**Critério de conclusão:** Consigo formular qualquer experimento dos milestones seguintes sem precisar voltar à definição de estado ou operador.

---

## Milestone 2 — Computação quântica como processamento espectral

**Estado de entrada:** linguagem mínima fixada, mas ainda não existe uma noção clara do que o circuito está tentando extrair do operador.

**O que este milestone introduz:** a visão espectral — autovalores, autovetores, fase, dinâmica unitária e phase estimation em casos pequenos.

**Goal:** move from "circuito como sequência de portas" to "circuito como mecanismo de extração de informação espectral".

**Notebooks:**
- [ ] [C-03](core/C-03_phase_kickback.ipynb) — onde interferência começa a "dizer algo" sobre o operador
- [ ] [C-04](core/C-04_phase_estimation.ipynb) — primeiro marco real do projeto

**Perguntas cobertas:** Q-F4, Q-S1, Q-S3, Q-C1, Q-C2

**Critério de conclusão:** Consigo ligar diretamente a distribuição de saída do QPE ao espectro do operador de entrada, verificado classicamente.

---

## Milestone 3 — Tradução de problemas clássicos para operadores

**Estado de entrada:** linguagem matemática formada e primeira noção espectral. Falta a ponte para casos de uso.

**O que este milestone introduz:** padrões de tradução de problemas simples para operador + preparação + medição, com análise explícita do que se perde e do que se ganha.

**Goal:** move from "entender experimentos quânticos isolados" to "saber formular problemas pequenos para a linguagem do QPU".

**Notebooks:**
- [ ] [C-05](core/C-05_hamiltonian_simulation.ipynb) — dinâmica contínua como circuito *(status provisional — ver INDEX.md)*
- [ ] [C-06](core/C-06_problem_translation.ipynb) — notebook explicitamente sobre a tese

**Perguntas cobertas:** Q-T1, Q-T2, Q-T4, Q-T5, Q-C3

**Critério de conclusão:** Tenho pelo menos dois exemplos completos de tradução (problema → operador → circuito → medição) com análise de custo honesta.

---

## Milestone 4 — Ponte honesta para a fronteira

**Estado de entrada:** capacidade de formular e testar casos pequenos, mas sem musculatura para ler trabalhos modernos sem se perder em formalismo.

**O que este milestone introduz:** uma entrada controlada em QSP/QSVT e na distinção entre processamento de singular values e de eigenvalues.

**Goal:** move from "intuição local sobre algoritmos" to "vocabulário e estrutura para ler a fronteira com criticidade".

**Notebooks:**
- [ ] [C-07](core/C-07_singular_values_vs_eigenvalues.ipynb) — distinção estrutural fundamental
- [ ] [C-08](core/C-08_qsp_qsvt_entry_point.ipynb) — entrada na fronteira

**Perguntas cobertas:** Q-S2, Q-T3, Q-B1, Q-B2, Q-B3

**Critério de conclusão:** Consigo ler um paper recente de QSP/QSVT e identificar qual estrutura espectral ele processa, por quê, e onde block-encoding entra.

---

## Estado atual

- [x] Repositório criado e estrutura base definida
- [ ] **Milestone 1** — em andamento
- [ ] Milestone 2
- [ ] Milestone 3
- [ ] Milestone 4
