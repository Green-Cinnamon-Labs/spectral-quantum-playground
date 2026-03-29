# spectral-quantum-playground

Este repositório é um caderno de pesquisa reproduzível sobre um problema central da computação quântica: como traduzir problemas para a linguagem que um QPU consegue processar.

## Tese

A hipótese que guia este projeto é que o principal desafio de engenharia não está apenas em executar circuitos, mas em **formular corretamente estados, operadores e medições** para que a computação quântica tenha significado algorítmico.

Um QPU não é uma "CPU mais rápida". É uma unidade especializada que opera sobre estados quânticos por meio de transformações muito restritas. O gargalo não é só executar circuitos: é formular o problema na linguagem correta — operadores, estados, unitários, observáveis, espectro, preparação e medição.

O trabalho do engenheiro é entender quando e como um problema pode ser preparado para o QPU.

## Pergunta-mãe

> Quais estruturas matemáticas um problema precisa ter para ser processado por um circuito quântico de forma significativa?

Essa pergunta se desdobra em quatro trilhas. Ver [QUESTIONS.md](QUESTIONS.md) para as perguntas completas.

## O que este repositório é

- Um caderno de pesquisa reproduzível
- Guiado por perguntas explícitas
- Construído com pequenos experimentos verificáveis
- Com conclusões honestas sobre o que foi e o que não foi aprendido
- Uma trilha do básico até a borda de temas como phase estimation, Hamiltonian simulation e QSP/QSVT

## O que este repositório não é

- Não é um curso resumido
- Não é uma coleção de demos de SDK
- Não é um projeto dependente de hardware real
- Não é uma promessa de vantagem quântica prática

## Estrutura

```
spectral-quantum-playground/
│
├── QUESTIONS.md              # Coração do projeto — perguntas e critérios de resposta
├── ROADMAP.md                # Milestones e trilha de progresso
├── references/
│   ├── papers.md             # Referências bibliográficas comentadas
│   └── notes/                # Notas de leitura
│
├── notebooks/
│   ├── 00_states_operators_measurements.ipynb
│   ├── 01_unitaries_spectrum_and_dynamics.ipynb
│   ├── 02_phase_kickback.ipynb
│   ├── 03_phase_estimation_toy_models.ipynb
│   ├── 04_hamiltonian_simulation_small_cases.ipynb
│   ├── 05_problem_to_operator_translation.ipynb
│   ├── 06_singular_values_vs_eigenvalues.ipynb
│   └── 07_qsp_qsvt_entry_point.ipynb
│
├── src/
│   ├── linear_algebra/       # Utilitários de álgebra linear
│   ├── circuits/             # Construtores de circuitos
│   ├── visualization/        # Plots e diagramas
│   └── utils/                # Funções auxiliares gerais
│
├── experiments/
│   ├── toy_operators/        # Operadores de teste
│   └── logs/                 # Registro de experimentos
│
└── assets/                   # Figuras e recursos estáticos
```

## Formato dos notebooks

Cada notebook segue a mesma estrutura:

1. **Pergunta** — a questão concreta que o notebook tenta responder
2. **Modelo matemático mínimo** — o menor modelo que captura a essência da pergunta
3. **Experimento** — lado clássico (álgebra linear direta) + circuito quântico equivalente
4. **Conclusão** — o que foi realmente aprendido, e os limites do que foi mostrado

## Trilhas

| Trilha | Foco |
|--------|------|
| 1. Fundamentos operacionais | Estado, operação, unitaridade, medição, interferência |
| 2. Pensamento espectral | Espectro, autovalores, phase estimation |
| 3. Tradução de problemas | Problema clássico → operador + estado + medição |
| 4. Ponte para a fronteira | QSP/QSVT, block-encoding, singular vs. eigenvalues |

## Ambiente

Apenas simulador. Nenhuma dependência de hardware real.
Separação explícita entre limitação de hardware, limitação de SDK e limitação conceitual do algoritmo.

```bash
pip install -r requirements.txt
jupyter lab
```

## Progresso

Ver [ROADMAP.md](ROADMAP.md) para os milestones e o estado atual.
