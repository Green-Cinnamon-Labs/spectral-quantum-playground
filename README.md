# spectral-quantum-playground

Caderno de pesquisa reproduzível sobre computação quântica. O objetivo dele é explorar uma tese:

<div style="border-left: 2px solid #16a34a; padding: 0.5em 1em 0.5em 1.1em; margin: 0.8em 0 1.2em 0; background: rgba(22, 163, 74, 0.05); border-radius: 0 3px 3px 0;">
  <span style="font-size: 0.65em; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #16a34a;">TESE PRINCIPAL</span><br>
  <span style="font-size: 0.88em; line-height: 1.65;">O principal desafio para engenheiros que visam aplicar computação quântica em problemas do cotidiano é desenvolver a intuição de como formalizar um problema real matemáticamente.</span>
</div>

Um QPU não é uma CPU mais rápida. É uma unidade especializada que opera sobre estados quânticos por meio de transformações restritas. O gargalo prático, aqui, é saber formular o problema na linguagem correta: operadores, estados, unitários, observáveis, espectro, preparação, medição.

## Como é a minha abordagem?

Eu sempre faço o notebook ter uma pergunta central que é imediatamente respondida com uma afirmação que o leitor, no início da leitura, não entende. Essa afirmação guia a estruturação do notebook em questão. O objetivo é sempre explorar a afirmação que responde a pergunta do notebook. No final, exponho o que você entendeu — como uma espécie de resumo — e o que aquele notebook não te explicou — para que você perceba que alguma coisa realmente foi omitida de você.

Eu decidi seguir uma abordagem repetitiva. A cada notebook do núcleo, eu praticamente repito as mesmas ideias com cada vez mais complexidade associada. Geralmente, eu vou usar exemplos básicos e ilustrativos para explorar ideias imporatantes e depois vou usar esses mesmos exemplos para formalizar um pouco da matemática, sempre em uma crescente de complexidade.

Vou repetir e relembrar conceitos à exaustão. Uma mesma ideia será repetida dezenas de vezes ao longo dos vários núcleos. Vou usar esquemas visuais feitos com bibliotecas padrão do Python e em um estágio mais avançado, vamos usar `qiskit`. 

A melhor forma de expor como isso está sendo usado sem acomodar demais o leitor é introduzido ele aos problemas reais. É por isso que eu vou explicar usando os artigos reais que firmaram milestones dentro da computação quântica. Meu objetivo é expor o leitor à cronologia dos fatos.

Por fim, eu paralelizo com notebooks especializados em temas específicos. Achei interessante separar em dois grandes blocos: `digressões` e `matemática`. As digressões versam sobre os mesmos assuntos que você encontrará nos notebooks do núcleo. Já a matemática é focada em dar musculatura na intuição matemática e física. 

Por fim, eu considero fundamental entender a etimologia das palavras que são

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
