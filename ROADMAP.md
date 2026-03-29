# Roadmap

## Milestone 1 — Linguagem mínima do problema quântico

**Estado de entrada:** curiosidade real formada, mas vocabulário básico ainda sendo consolidado. Estado, operador, unitário, observável e medição ainda se confundem às vezes.

**O que este milestone introduz:** um núcleo mínimo de álgebra linear e circuito quântico suficiente para formular perguntas sem confusão conceitual.

**Goal:** move from "portas e qubits como objetos soltos" to "problemas formulados como estados + operadores + medição".

**Notebooks:**
- [ ] `00_states_operators_measurements.ipynb` — linguagem fundamental
- [ ] `01_unitaries_spectrum_and_dynamics.ipynb` — por que unitário importa

**Perguntas cobertas:**
- O que exatamente é um estado quântico?
- Por que a evolução precisa ser unitária?
- O que medição devolve, e o que ela destrói?

**Critério de conclusão:** Consigo formular qualquer experimento dos milestones seguintes sem precisar voltar à definição de estado ou operador.

---

## Milestone 2 — Computação quântica como processamento espectral

**Estado de entrada:** linguagem mínima fixada, mas ainda não existe uma noção clara do que o circuito está tentando extrair do operador.

**O que este milestone introduz:** a visão espectral — autovalores, autovetores, fase, dinâmica unitária e phase estimation em casos pequenos.

**Goal:** move from "circuito como sequência de portas" to "circuito como mecanismo de extração de informação espectral".

**Notebooks:**
- [ ] `02_phase_kickback.ipynb` — onde interferência começa a "dizer algo" sobre o operador
- [ ] `03_phase_estimation_toy_models.ipynb` — primeiro marco real do projeto

**Perguntas cobertas:**
- Onde entra a interferência de fato?
- O que o espectro de um operador diz sobre a computação?
- Por que phase estimation é um algoritmo "espectral"?
- Por que phase estimation pode ser vista como processamento espectral?

**Critério de conclusão:** Consigo ligar diretamente a distribuição de saída do QPE ao espectro do operador de entrada, verificado classicamente.

---

## Milestone 3 — Tradução de problemas clássicos para operadores

**Estado de entrada:** linguagem matemática formada e primeira noção espectral. Falta a ponte para casos de uso.

**O que este milestone introduz:** padrões de tradução de problemas simples para operador + preparação + medição, com análise explícita do que se perde e do que se ganha.

**Goal:** move from "entender experimentos quânticos isolados" to "saber formular problemas pequenos para a linguagem do QPU".

**Notebooks:**
- [ ] `04_hamiltonian_simulation_small_cases.ipynb` — Hamiltoniano como caso de uso central
- [ ] `05_problem_to_operator_translation.ipynb` — notebook explicitamente sobre a tese

**Perguntas cobertas:**
- Como um problema clássico vira operador, estado inicial e medição?
- O custo de preparação do estado mata a vantagem em quais casos?
- Quais propriedades de um problema sobrevivem à tradução para circuito?
- Quais classes de problema admitem uma tradução limpa?

**Critério de conclusão:** Tenho pelo menos dois exemplos completos de tradução (problema → operador → circuito → medição) com análise de custo honesta.

---

## Milestone 4 — Ponte honesta para a fronteira

**Estado de entrada:** capacidade de formular e testar casos pequenos, mas sem musculatura para ler trabalhos modernos sem se perder em formalismo.

**O que este milestone introduz:** uma entrada controlada em QSP/QSVT e na distinção entre processamento de singular values e de eigenvalues.

**Goal:** move from "intuição local sobre algoritmos" to "vocabulário e estrutura para ler a fronteira com criticidade".

**Notebooks:**
- [ ] `06_singular_values_vs_eigenvalues.ipynb` — distinção estrutural fundamental
- [ ] `07_qsp_qsvt_entry_point.ipynb` — entrada na fronteira

**Perguntas cobertas:**
- Qual a diferença entre autovalores e valores singulares?
- Toda formulação útil precisa passar por um unitário?
- O que QSP transforma: autovalores ou valores singulares?
- Por que QSVT exige block-encoding?
- Em que sentido eigenvalue processing amplia o quadro do QSVT?

**Critério de conclusão:** Consigo ler um paper recente de QSP/QSVT e identificar qual estrutura espectral ele processa, por quê, e onde block-encoding entra.

---

## Estado atual

- [x] Repositório criado e estrutura base definida
- [ ] **Milestone 1** — em andamento
- [ ] Milestone 2
- [ ] Milestone 3
- [ ] Milestone 4
