# ÍNDICE

Mapa de navegação do repositório. Atualizar sempre que um notebook for criado ou concluído.

---

## Trilha Núcleo

Ordem cronológica de entendimento. Cada notebook parte de uma pergunta explícita.

| Código | Título | Digressões | Matemática | Status |
|---|---|---|---|---|
| [N-00](nucleo/N-00.ipynb) | Por que é possível computar com um qubit? | D-00 | — | rascunho |
| [N-01](nucleo/N-01.ipynb) | Estados, Operadores e Medições | D-01, D-02 | M-00 | rascunho |
| [N-02](nucleo/N-02.ipynb) | Unitários, Espectro e Dinâmica | — | M-00, M-01 | rascunho |
| [N-03](nucleo/N-03.ipynb) | Kickback de Fase | D-02 | — | rascunho |
| [N-04](nucleo/N-04.ipynb) | Estimação de Fase | D-03 | M-01, M-02 | rascunho |
| [N-05](nucleo/N-05.ipynb) | Simulação Hamiltoniana | D-03 | M-01 | rascunho |
| [N-06](nucleo/N-06.ipynb) | Tradução de Problemas | D-04 | M-02 | rascunho |
| [N-07](nucleo/N-07.ipynb) | Valores Singulares vs. Autovalores | D-05 | M-04 | rascunho |
| [N-08](nucleo/N-08.ipynb) | QSP / QSVT — Entrada | D-05 | M-03, M-04 | rascunho |

---

## Digressões

Desvios instrumentais curtos. Estrutura: definição mínima → por que importa aqui → exemplo pequeno.

| Código | Título | Referenciado por | Status |
|---|---|---|---|
| [D-00](digressoes/D-00.ipynb) | O que é um qubit? | N-00 | rascunho |
| [D-01](digressoes/D-01.ipynb) | Regra de Born e Colapso | N-01 | esqueleto |
| [D-02](digressoes/D-02.ipynb) | Produtos Tensoriais | N-01, N-03 | esqueleto |
| [D-03](digressoes/D-03.ipynb) | Comutadores e Erro de Trotter | N-04, N-05 | esqueleto |
| [D-04](digressoes/D-04.ipynb) | O Problema de Simon | N-06 | esqueleto |
| [D-05](digressoes/D-05.ipynb) | Block-Encoding Minimal | N-07, N-08 | esqueleto |

---

## Matemática

Exploração matemática com vínculo explícito com os notebooks do núcleo.
Última seção obrigatória: **"Por que isso importa para algoritmos quânticos?"**

| Código | Título | Vínculo com núcleo | Status |
|---|---|---|---|
| [M-00](matematica/M-00.ipynb) | Vetores, Espaços e o Espaço de Hilbert | N-01 em diante | rascunho |
| [M-01](matematica/M-01.ipynb) | Teoria Espectral de Operadores | N-02, N-04, N-05 | esqueleto |
| [M-02](matematica/M-02.ipynb) | A Transformada de Fourier — da decomposição espectral à QFT | N-04, N-06 | esqueleto |
| [M-03](matematica/M-03.ipynb) | Aproximação Polinomial | N-08 | esqueleto |
| [M-04](matematica/M-04.ipynb) | SVD — Geometria e Interpretação | N-07, N-08 | esqueleto |

---

## Convenções de status

| Status | Significado |
|---|---|
| `esqueleto` | Arquivo criado, estrutura definida, sem conteúdo real |
| `rascunho` | Conteúdo escrito, não revisado |
| `revisado` | Conteúdo revisado e pergunta verificada como respondida |
| `fechado` | Pergunta marcada como respondida em QUESTIONS.md |
