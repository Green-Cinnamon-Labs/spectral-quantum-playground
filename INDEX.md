# ÍNDICE

Mapa de navegação do repositório. Atualizar sempre que um notebook for criado ou concluído.

---

## Trilha Núcleo

Linha narrativa principal. Cada notebook responde perguntas explícitas do [QUESTIONS.md](QUESTIONS.md).
Leitura sequencial recomendada — pré-requisitos indicados no header de cada notebook.

| ID | Título | Perguntas | Digressões | Matemática | Status |
|---|---|---|---|---|---|
| [C-00](nucleo/C-00_porque_qubit.ipynb) | Por que o qubit computa? | Q-F0 | D-00 | — | rascunho |
| [C-01](nucleo/C-01_estados_operadores_medidas.ipynb) | Estados, Operadores e Medidas | Q-F1, Q-F3 | D-01, D-02 | M-00 | rascunho |
| [C-02](nucleo/C-02_unitarios_espectro_dinamica.ipynb) | Unitários, Espectro e Dinâmica | Q-F2, Q-S1 | — | M-00, M-01 | rascunho |
| [C-03](nucleo/C-03_kickback_de_fase.ipynb) | Kickback de Fase | Q-F4 | D-02 | — | rascunho |
| [C-04](nucleo/C-04_estimacao_de_fase.ipynb) | Estimação de Fase | Q-C1, Q-C2, Q-S3 | D-03 | M-01 | rascunho |
| [C-05](nucleo/C-05_simulacao_hamiltoniana.ipynb) | Simulação Hamiltoniana | Q-T2 | D-03 | M-01 | rascunho ⚠️ provisional |
| [C-06](nucleo/C-06_traducao_de_problemas.ipynb) | Tradução de Problemas | Q-C3, Q-T1, Q-T4, Q-T5 | — | — | rascunho |
| [C-07](nucleo/C-07_valores_singulares_vs_autovalores.ipynb) | Valores Singulares vs. Autovalores | Q-S2, Q-T3 | D-04 | M-03 | rascunho |
| [C-08](nucleo/C-08_qsp_qsvt_entrada.ipynb) | QSP / QSVT — Entrada | Q-B1, Q-B2, Q-B3 | D-04 | M-02, M-03 | rascunho |

> ⚠️ **C-05 — decisão aberta:** Simulação hamiltoniana pode migrar para digressão D-05 dependendo de como C-06 se desenvolver. Reavaliar ao fechar C-06.

---

## Digressões

Notebooks curtos e instrumentais. Destravem dependências conceituais sem tentar esgotar o tema.
Estrutura obrigatória: definição mínima → por que importa aqui → exemplo pequeno.

| ID | Título | Referenciado por | Status |
|---|---|---|---|
| [D-00](digressoes/D-00_o_que_e_um_qubit.ipynb) | O que é um qubit? | C-00 | rascunho |
| [D-01](digressoes/D-01_regra_de_born_e_colapso.ipynb) | Regra de Born e Colapso | C-01 | esqueleto |
| [D-02](digressoes/D-02_produtos_tensoriais.ipynb) | Produtos Tensoriais | C-01, C-03 | esqueleto |
| [D-03](digressoes/D-03_comutadores_e_erro_de_trotter.ipynb) | Comutadores e Erro de Trotter | C-04, C-05 | esqueleto |
| [D-04](digressoes/D-04_block_encoding_minimal.ipynb) | Block-Encoding Minimal | C-07, C-08 | esqueleto |

---

## Matemática

Exploração matemática com vínculo explícito com algoritmos quânticos.
Não é pré-requisito bloqueante por padrão — exceto quando marcado como estrutural em um C-notebook.
Última seção obrigatória: **"Por que isso importa para algoritmos quânticos?"**

| ID | Título | Vínculo com núcleo | Status |
|---|---|---|---|
| [M-00](matematica/M-00_vetores_espaco_de_hilbert.ipynb) | Vetores, Espaços e o Espaço de Hilbert | C-01 em diante, D-00 | rascunho |
| [M-01](matematica/M-01_teoria_espectral_operadores.ipynb) | Teoria Espectral de Operadores | C-02, C-04, C-05 | esqueleto |
| [M-02](matematica/M-02_aproximacao_polinomial.ipynb) | Aproximação Polinomial | C-08 (QSP) | esqueleto |
| [M-03](matematica/M-03_svd_geometria.ipynb) | SVD — Geometria e Interpretação | C-07, C-08 | esqueleto |

---

## Mapa de perguntas → notebooks

| Pergunta | Notebook |
|---|---|
| Q-F0 | C-00 |
| Q-F1 | C-01 |
| Q-F2 | C-02 |
| Q-F3 | C-01 |
| Q-F4 | C-03 |
| Q-C1 | C-04 |
| Q-C2 | C-04 |
| Q-C3 | C-06 |
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
