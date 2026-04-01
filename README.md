# spectral-quantum-playground

Caderno de pesquisa reproduzível sobre um problema central da computação quântica: como traduzir problemas para a linguagem que um QPU consegue processar.

## Tese

O principal desafio de engenharia não está só em executar circuitos — está em **formular corretamente estados, operadores e medições** para que a computação quântica tenha significado algorítmico.

Um QPU não é uma CPU mais rápida. É uma unidade especializada que opera sobre estados quânticos por meio de transformações restritas. O gargalo é formular o problema na linguagem correta: operadores, estados, unitários, observáveis, espectro, preparação e medição.

## Pergunta central

> Quais estruturas matemáticas um problema precisa ter para ser processado por um circuito quântico de forma significativa?

## O que este repositório é

- Caderno de pesquisa reproduzível
- Guiado por perguntas que emergem dos experimentos
- Construído com ordem cronológica de entendimento: cada notebook dá ao leitor a definição útil do conceito antes de usá-lo
- Honesto sobre o que foi e o que não foi aprendido
- Sem dependência de hardware real — apenas simulador

## O que não é

- Não é um curso introdutório genérico
- Não é uma coleção de demos de SDK
- Não é uma promessa de vantagem quântica prática

## Estrutura

```
spectral-quantum-playground/
│
├── ÍNDICE.md                 # Mapa de navegação central
├── QUESTIONS.md              # Índice de perguntas por notebook
├── ROADMAP.md                # Milestones e estado atual
│
├── nucleo/                   # Trilha principal (N-00 a N-08)
├── digressoes/               # Desvios instrumentais curtos (D-00 a D-05)
├── matematica/               # Exploração matemática com vínculo ao projeto (M-00 a M-04)
│
├── codigo/
│   ├── algebra_linear/
│   ├── circuitos/
│   ├── visualizacao/
│   └── utilitarios/
│
├── experimentos/
└── recursos/
```

## Ambiente

```bash
poetry install
poetry run jupyter lab
```

## Progresso

Ver [ROADMAP.md](ROADMAP.md).
