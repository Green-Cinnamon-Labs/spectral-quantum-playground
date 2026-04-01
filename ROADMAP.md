# Roteiro

O projeto segue uma ordem cronológica de entendimento: cada etapa dá ao leitor a definição útil do conceito antes de usá-lo na etapa seguinte.

---

## Etapa 0 — Intuição antes do formalismo

**Ponto de partida:** nenhum conhecimento formal de mecânica quântica assumido.

**O que esta etapa introduz:** por que o qubit é um substrato computacional diferente — não pela quantidade de estados, mas pela estrutura das amplitudes complexas e pelo que interferência torna possível.

**Notebooks:**
- [x] N-00 — Por que é possível computar com um qubit?
- [x] D-00 — O que é um qubit? *(digressão de apoio)*
- [x] D-06 — O Princípio da Incerteza de Heisenberg *(digressão de apoio)*
- [x] D-07 — A História da Computação Quântica *(digressão de apoio)*
- [x] D-08 — Arquiteturas Físicas do Qubit *(digressão de apoio)*

**Critério de conclusão:** consigo demonstrar um resultado determinístico via interferência que seria impossível com probabilidades clássicas.

---

## Etapa 1 — Linguagem mínima

**Ponto de partida:** intuição do qubit formada, mas formalismo ainda nebuloso.

**O que esta etapa introduz:** estado, operador, observável, unitário, medição — o vocabulário mínimo para formular qualquer experimento quântico sem ambiguidade.

**Notebooks:**
- [x] N-01 — Como descrever sem ambiguidade um estado, uma operação e uma medição?
- [ ] N-02 — Por que a evolução precisa ser unitária, e o que o espectro diz sobre a dinâmica?
- [x] M-00 — Vetores, Espaços e o Espaço de Hilbert *(matemática de apoio)*

**Critério de conclusão:** consigo descrever qualquer experimento dos milestones seguintes em termos de estado inicial, operador e medição, sem precisar recorrer à definição dos termos.

---

## Etapa 2 — Computação como processamento espectral

**Ponto de partida:** linguagem mínima fixada, mas sem noção clara do que o circuito está extraindo do operador.

**O que esta etapa introduz:** a visão espectral — autovalores, fase, dinâmica, e o mecanismo pelo qual um circuito extrai informação espectral de um operador.

**Notebooks:**
- [ ] N-03 — Como a fase de um autovalor migra para o registrador de controle?
- [ ] N-04 — Como um circuito extrai informação espectral de um operador?
- [ ] M-04 — A Transformada de Fourier *(matemática de apoio)*

**Critério de conclusão:** consigo ligar diretamente a distribuição de saída do QPE ao espectro do operador de entrada, verificado classicamente.

---

## Etapa 3 — Tradução de problemas

**Ponto de partida:** visão espectral formada; falta a ponte entre problemas concretos e a linguagem do QPU.

**O que esta etapa introduz:** o padrão operador + preparação + medição aplicado a problemas reais, com análise honesta do custo de cada parte.

**Notebooks:**
- [ ] N-05 — Como uma dinâmica contínua vira circuito, e qual o custo da aproximação?
- [ ] N-06 — Como um problema clássico se torna operador + preparação + medição?

**Critério de conclusão:** tenho pelo menos dois exemplos completos de tradução com análise explícita do que se preserva e do que se perde.

---

## Etapa 4 — Ponte para a fronteira

**Ponto de partida:** capaz de formular e testar casos pequenos; sem musculatura para ler trabalhos modernos.

**O que esta etapa introduz:** a distinção entre autovalores e valores singulares, block-encoding, e uma entrada controlada em QSP/QSVT.

**Notebooks:**
- [ ] N-07 — Qual a diferença entre autovalores e valores singulares?
- [ ] N-08 — O que QSP/QSVT realmente transforma?

**Critério de conclusão:** consigo ler um paper recente de QSP/QSVT, identificar qual estrutura espectral ele processa e onde block-encoding entra.

---

## Estado atual

- [x] Estrutura do repositório definida
- [x] Etapa 0 — N-00 escrito (rascunho), digressões D-06/D-07/D-08 estruturadas
- [x] Etapa 1 — N-01 escrito (rascunho), N-02 ainda esqueleto
- [ ] Etapa 2 — esqueletos criados
- [ ] Etapa 3 — esqueletos criados
- [ ] Etapa 4 — esqueletos criados
