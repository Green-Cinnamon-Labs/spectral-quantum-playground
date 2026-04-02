# spectral-quantum-playground

Caderno de pesquisa reproduzível sobre computação quântica — construído cronologicamente, guiado por perguntas, honesto sobre o que foi e o que não foi aprendido.

## Pergunta central

> Quais estruturas matemáticas um problema precisa ter para ser processado por um circuito quântico de forma significativa?

## Tese

O principal desafio de engenharia não está só em executar circuitos — está em **formular corretamente estados, operadores e medições** para que a computação quântica tenha significado algorítmico.

Um QPU não é uma CPU mais rápida. É uma unidade especializada que opera sobre estados quânticos por meio de transformações restritas. O gargalo é saber formular o problema na linguagem correta: operadores, estados, unitários, observáveis, espectro, preparação, medição.

---

## Como os notebooks são organizados

Os notebooks do **núcleo** partem de uma **pergunta explícita** no título. O bloco de abertura traz **etimologias** dos termos-chave — não como definição, mas como contexto lateral. Em seguida, uma **afirmação introdutória** responde à pergunta diretamente, em uma ou duas frases, às vezes acompanhada de uma fórmula.

O restante do notebook elabora essa afirmação. Termos considerados centrais aparecem destacados em `backtick`. Conexões com outros notebooks aparecem como links de digressão (`↳`) ou de matemática. Ao final, sempre: **"O que este notebook te respondeu"** e **"O que este notebook não respondeu"**.

Os notebooks de **digressão** são desvios curtos e instrumentais: definição mínima → por que importa aqui → exemplo pequeno. Podem ser lidos fora de ordem.

Os notebooks de **matemática** não partem de uma pergunta — eles consolidam um conceito de ponta a ponta, com vínculo explícito ao projeto na última seção.

---

## O que este repositório é

- Caderno de pesquisa reproduzível
- Construído com ordem cronológica de entendimento: cada notebook dá ao leitor a definição útil do conceito antes de usá-lo
- Honesto sobre o que foi e o que não foi aprendido
- Sem dependência de hardware real — apenas simulador

## O que não é

- Não é um curso introdutório genérico
- Não é uma coleção de demos de SDK
- Não é uma promessa de vantagem quântica prática

---

## Trilha Núcleo

Ordem cronológica de entendimento. Cada notebook parte de uma pergunta explícita.

| Código | Pergunta | Digressões | Matemática | Status |
|---|---|---|---|---|
| [N-00](nucleo/N-00.ipynb) | Por que é possível computar com um qubit? | D-00 | — | rascunho |
| [N-01](nucleo/N-01.ipynb) | O que uma operação quântica faz ao estado — e o que a medição consegue revelar sobre ela? | D-01, D-02 | M-00, M-05 | rascunho |
| [N-02](nucleo/N-02.ipynb) | Por que a evolução precisa ser unitária, e o que o espectro diz sobre a dinâmica? | — | M-00 | esqueleto |
| [N-03](nucleo/N-03.ipynb) | Como a fase de um autovalor migra para o registrador de controle? | D-02 | — | esqueleto |
| [N-04](nucleo/N-04.ipynb) | Como um circuito extrai informação espectral de um operador? | D-03 | M-04 | esqueleto |
| [N-05](nucleo/N-05.ipynb) | Como uma dinâmica contínua vira circuito, e qual o custo da aproximação? | D-03 | — | esqueleto |
| [N-06](nucleo/N-06.ipynb) | Como um problema clássico se torna operador + preparação + medição? | D-04 | M-04 | esqueleto |
| [N-07](nucleo/N-07.ipynb) | Qual a diferença entre autovalores e valores singulares? | D-05 | — | esqueleto |
| [N-08](nucleo/N-08.ipynb) | O que QSP/QSVT realmente transforma? | D-05 | — | esqueleto |

---

## Digressões

Desvios instrumentais curtos. Podem ser lidos fora de ordem.

| Código | Título | Referenciado por | Status |
|---|---|---|---|
| [D-00](digressoes/D-00.ipynb) | O que é um qubit? | N-00 | rascunho |
| [D-01](digressoes/D-01.ipynb) | Regra de Born e Colapso | N-01 | esqueleto |
| [D-02](digressoes/D-02.ipynb) | Produtos Tensoriais | N-01, N-03 | esqueleto |
| [D-03](digressoes/D-03.ipynb) | Comutadores e Erro de Trotter | N-04, N-05 | esqueleto |
| [D-04](digressoes/D-04.ipynb) | O Problema de Simon | N-06 | esqueleto |
| [D-05](digressoes/D-05.ipynb) | Block-Encoding Minimal | N-07, N-08 | esqueleto |
| [D-06](digressoes/D-06.ipynb) | O Princípio da Incerteza de Heisenberg | D-00 | esqueleto |
| [D-07](digressoes/D-07.ipynb) | A História da Computação Quântica | D-00 | esqueleto |
| [D-08](digressoes/D-08.ipynb) | Arquiteturas Físicas do Qubit | D-00 | esqueleto |

---

## Matemática

Exploração matemática com vínculo explícito ao projeto. Última seção obrigatória: **"Por que isso importa para algoritmos quânticos?"**

| Código | Título | Vínculo | Status |
|---|---|---|---|
| [M-00](matematica/M-00.ipynb) | Vetores, Espaços e o Espaço de Hilbert | N-01 em diante | rascunho |
| [M-01](matematica/M-01.ipynb) | Mecânica Clássica: de Newton a Hamilton | D-00 | esqueleto |
| [M-02](matematica/M-02.ipynb) | Mecânica Quântica: de Planck a Dirac | D-00 | esqueleto |
| [M-03](matematica/M-03.ipynb) | A Máquina de Turing | D-00 | esqueleto |
| [M-04](matematica/M-04.ipynb) | A Transformada de Fourier — da decomposição espectral à QFT | N-04, N-06 | esqueleto |
| [M-05](matematica/M-05.ipynb) | Álgebra Linear: das Equações aos Tensores | N-01, D-02 | esqueleto |

---

## Convenções de status

| Status | Significado |
|---|---|
| `esqueleto` | Arquivo criado, estrutura definida, sem conteúdo real |
| `rascunho` | Conteúdo escrito, não revisado |
| `revisado` | Conteúdo revisado e pergunta verificada como respondida |
| `fechado` | Pergunta marcada como respondida em QUESTIONS.md |

---

## Ambiente

```bash
poetry install
poetry run jupyter lab
```

## Progresso

Ver [ROADMAP.md](ROADMAP.md).
