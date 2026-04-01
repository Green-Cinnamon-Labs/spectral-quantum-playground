# Roteiro

O projeto segue uma ordem cronológica de entendimento: cada etapa dá ao leitor a definição útil do conceito antes de usá-lo na etapa seguinte.

---

## Etapa 0 — Intuição antes do formalismo

**Ponto de partida:** nenhum conhecimento formal de mecânica quântica assumido.

**O que esta etapa introduz:** por que o qubit é um substrato computacional diferente — não pela quantidade de estados, mas pela estrutura das amplitudes complexas e pelo que interferência torna possível.

**Notebooks:**
- [ ] N-00 — Por que é possível computar com um qubit?
- [ ] D-00 — O que é um qubit? *(digressão de apoio)*

**Critério de conclusão:** consigo demonstrar um resultado determinístico via interferência que seria impossível com probabilidades clássicas.

---

## Etapa 1 — Linguagem mínima

**Ponto de partida:** intuição do qubit formada, mas formalismo ainda nebuloso.

**O que esta etapa introduz:** estado, operador, observável, unitário, medição — o vocabulário mínimo para formular qualquer experimento quântico sem ambiguidade.

**Notebooks:**
- [ ] N-01 — Estados, Operadores e Medições
- [ ] N-02 — Unitários, Espectro e Dinâmica
- [ ] M-00 — Vetores, Espaços e o Espaço de Hilbert *(matemática de apoio)*

**Critério de conclusão:** consigo descrever qualquer experimento dos milestones seguintes em termos de estado inicial, operador e medição, sem precisar recorrer à definição dos termos.

---

## Etapa 2 — Computação como processamento espectral

**Ponto de partida:** linguagem mínima fixada, mas sem noção clara do que o circuito está extraindo do operador.

**O que esta etapa introduz:** a visão espectral — autovalores, fase, dinâmica, e o mecanismo pelo qual um circuito extrai informação espectral de um operador.

**Notebooks:**
- [ ] N-03 — Kickback de Fase
- [ ] N-04 — Estimação de Fase
- [ ] M-01 — Teoria Espectral de Operadores *(matemática de apoio)*
- [ ] M-02 — A Transformada de Fourier *(matemática de apoio)*

**Critério de conclusão:** consigo ligar diretamente a distribuição de saída do QPE ao espectro do operador de entrada, verificado classicamente.

---

## Etapa 3 — Tradução de problemas

**Ponto de partida:** visão espectral formada; falta a ponte entre problemas concretos e a linguagem do QPU.

**O que esta etapa introduz:** o padrão operador + preparação + medição aplicado a problemas reais, com análise honesta do custo de cada parte — em particular o custo de preparação do estado.

**Notebooks:**
- [ ] N-05 — Simulação Hamiltoniana
- [ ] N-06 — Tradução de Problemas

**Critério de conclusão:** tenho pelo menos dois exemplos completos de tradução (problema → operador → circuito → medição) com análise explícita do que se preserva e do que se perde.

---

## Etapa 4 — Ponte para a fronteira

**Ponto de partida:** capaz de formular e testar casos pequenos; sem musculatura para ler trabalhos modernos.

**O que esta etapa introduz:** a distinção entre autovalores e valores singulares, block-encoding, e uma entrada controlada em QSP/QSVT.

**Notebooks:**
- [ ] N-07 — Valores Singulares vs. Autovalores
- [ ] N-08 — QSP / QSVT — Entrada
- [ ] M-03 — Aproximação Polinomial *(matemática de apoio)*
- [ ] M-04 — SVD — Geometria e Interpretação *(matemática de apoio)*

**Critério de conclusão:** consigo ler um paper recente de QSP/QSVT, identificar qual estrutura espectral ele processa e onde block-encoding entra.

---

## Estado atual

- [x] Estrutura do repositório definida
- [x] Etapa 0 — conteúdo escrito
- [x] Etapa 1 — conteúdo escrito
- [x] Etapa 2 — conteúdo escrito
- [ ] Etapa 3 — em andamento
- [ ] Etapa 4 — rascunhos iniciais
