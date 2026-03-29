# Perguntas de Pesquisa

Este é o arquivo central do projeto. Cada pergunta deve ter: por que ela importa, qual notebook tenta respondê-la, e qual evidência mínima conta como "respondida".

Regra de crescimento: um notebook novo só existe depois que a pergunta que ele responde existe aqui.

---

## Fundamentos

- [ ] **Q-F0** — Por que um qubit é um substrato computacional?
  - **Por que importa:** Antes de definir estados e operadores, vale estabelecer o que torna o qubit interessante: não é ter "dois estados", é ter amplitudes complexas cuja fase sobrevive até a interferência. Sem essa intuição, o formalismo do C-01 em diante parece arbitrário.
  - **Notebook:** [C-00](core/C-00_why_qubit_computes.ipynb)
  - **Respondida quando:** Demonstro um exemplo minimal onde fase + superposição + interferência produzem um resultado determinístico que não seria possível sem a estrutura complexa das amplitudes.

- [ ] **Q-F1** — O que exatamente é um estado quântico?
  - **Por que importa:** Confundir estado com vetor de probabilidades ou com string de bits é a fonte de mais mal-entendidos em computação quântica.
  - **Notebook:** [C-01](core/C-01_states_operators_measurements.ipynb)
  - **Respondida quando:** Consigo distinguir estado puro, misto e ensemble, e mostrar concretamente onde interferência aparece e onde não aparece.

- [ ] **Q-F2** — Por que a evolução precisa ser unitária?
  - **Por que importa:** Unitaridade não é uma restrição arbitrária — ela garante preservação de norma, reversibilidade e coerência. Entender isso é entender o que diferencia computação quântica de computação estocástica.
  - **Notebook:** [C-02](core/C-02_unitaries_spectrum_dynamics.ipynb)
  - **Respondida quando:** Mostro o que quebra quando uma "evolução" não é unitária (norma, reversibilidade) e por que isso fecha a porta para certas classes de operação.

- [ ] **Q-F3** — O que medição devolve, e o que ela destrói?
  - **Por que importa:** Medição é onde a computação quântica colapsa para um resultado clássico. Entender o custo do colapso é essencial para qualquer protocolo.
  - **Notebook:** [C-01](core/C-01_states_operators_measurements.ipynb)
  - **Respondida quando:** Demonstro projeção, colapso de estado e a diferença entre informação extraível antes e depois da medição.

- [ ] **Q-F4** — Onde entra a interferência de fato?
  - **Por que importa:** Interferência é o mecanismo central que separa computação quântica de computação probabilística clássica. Localizá-la concretamente é fundamental.
  - **Notebook:** [C-03](core/C-03_phase_kickback.ipynb)
  - **Respondida quando:** Mostro um caso onde interferência construtiva/destrutiva muda o resultado de uma computação de forma não reproduzível classicamente sem enumeração explícita.

---

## Core

- [ ] **Q-C1** — O que exatamente um circuito quântico extrai de um operador?
  - **Por que importa:** Define o que computação quântica realmente faz, além de "aplicar portas".
  - **Notebook:** [C-04](core/C-04_phase_estimation.ipynb)
  - **Respondida quando:** Consigo demonstrar que um circuito extrai informação espectral (fase) que não é diretamente acessível por leitura clássica simples, e identificar as hipóteses necessárias.

- [ ] **Q-C2** — Por que phase estimation pode ser vista como processamento espectral?
  - **Por que importa:** Phase estimation é o arquétipo de algoritmo quântico útil. Entender por que é "espectral" desmonta a ideia de que circuitos quânticos apenas "calculam coisas mais rápido".
  - **Notebook:** [C-04](core/C-04_phase_estimation.ipynb)
  - **Respondida quando:** Consigo ligar diretamente a distribuição de medição ao espectro do unitário, com um exemplo numérico verificado classicamente.

- [ ] **Q-C3** — Quais propriedades de um problema sobrevivem à tradução para circuito?
  - **Por que importa:** A tradução nunca é gratuita. Perder de vista o que se preserva e o que se perde é o principal motivo de ilusão de vantagem quântica.
  - **Notebook:** [C-06](core/C-06_problem_translation.ipynb)
  - **Respondida quando:** Tenho pelo menos dois exemplos de tradução com análise explícita do que foi preservado e do que foi sacrificado.

---

## Pensamento Espectral

- [ ] **Q-S1** — O que o espectro de um operador diz sobre a computação?
  - **Por que importa:** O espectro determina dinâmica, estabilidade, e o que um algoritmo quântico pode extrair. Sem isso, phase estimation e Hamiltonian simulation são caixas pretas.
  - **Notebook:** [C-02](core/C-02_unitaries_spectrum_dynamics.ipynb)
  - **Respondida quando:** Ligo concretamente autovalores de um unitário à sua dinâmica temporal com pelo menos um exemplo de 2x2 e um de 4x4.

- [ ] **Q-S2** — Qual a diferença entre autovalores e valores singulares?
  - **Por que importa:** É a distinção que separa phase estimation de QSVT. Confundi-los é confundir os regimes em que cada algoritmo opera.
  - **Notebook:** [C-07](core/C-07_singular_values_vs_eigenvalues.ipynb)
  - **Respondida quando:** Tenho um exemplo onde os dois divergem e consigo articular qual algoritmo usa qual estrutura e por quê.

- [ ] **Q-S3** — Por que phase estimation é um algoritmo "espectral"?
  - **Por que importa:** Nomear corretamente o que phase estimation faz clarifica o que outros algoritmos quânticos estão tentando fazer por extensão.
  - **Notebook:** [C-04](core/C-04_phase_estimation.ipynb)
  - **Respondida quando:** Consigo derivar a distribuição de saída do QPE a partir do espectro do operador de entrada, para um caso 2x2 ou 4x4.

---

## Tradução de Problemas

- [ ] **Q-T1** — Como um problema clássico vira operador, estado inicial e medição?
  - **Por que importa:** Esse é o coração da tese. Sem uma tradução explícita, computação quântica é um conjunto de experimentos sem aplicabilidade.
  - **Notebook:** [C-06](core/C-06_problem_translation.ipynb)
  - **Respondida quando:** Traduzo um problema simples (busca, fatoração de fase, ou estimativa de valor médio) nos três componentes, com análise de custo.

- [ ] **Q-T2** — Como uma dinâmica contínua vira circuito?
  - **Por que importa:** Hamiltonian simulation é a ponte mais direta entre física e computação quântica — e o lugar onde o custo da aproximação (Trotter) aparece de forma concreta.
  - **Notebook:** [C-05](core/C-05_hamiltonian_simulation.ipynb) *(status: provisional — ver nota no notebook)*
  - **Respondida quando:** Mostro Trotter vs. exato com análise de erro, e ligo os autovalores de H às fases extraíveis por QPE.

- [ ] **Q-T3** — Toda formulação útil precisa passar por um unitário?
  - **Por que importa:** Block-encoding, QSVT e outros avanços recentes mostram que a resposta não é óbvia.
  - **Notebook:** [C-07](core/C-07_singular_values_vs_eigenvalues.ipynb)
  - **Respondida quando:** Mostro pelo menos um caso onde a formulação natural do problema não é unitária e explico como contornar isso (ou por que não vale a pena).

- [ ] **Q-T4** — O custo de preparação do estado mata a vantagem em quais casos?
  - **Por que importa:** Preparação de estado é muitas vezes ignorada em análises de complexidade quântica. Ela pode cancelar qualquer ganho.
  - **Notebook:** [C-06](core/C-06_problem_translation.ipynb)
  - **Respondida quando:** Tenho pelo menos um exemplo concreto onde o custo de preparação cresce tão rápido quanto o ganho do algoritmo.

- [ ] **Q-T5** — Quais classes de problema admitem uma tradução limpa?
  - **Por que importa:** Entender as classes é entender os limites reais da computação quântica — não os limites de hardware, mas os limites estruturais.
  - **Notebook:** [C-06](core/C-06_problem_translation.ipynb), [C-08](core/C-08_qsp_qsvt_entry_point.ipynb)
  - **Respondida quando:** Consigo categorizar pelo menos três problemas distintos quanto à qualidade e custo da tradução.

---

## Ponte para a Fronteira

- [ ] **Q-B1** — O que QSP transforma: autovalores ou valores singulares?
  - **Por que importa:** A resposta determina em qual regime QSP opera e por que QSVT é uma generalização necessária.
  - **Notebook:** [C-08](core/C-08_qsp_qsvt_entry_point.ipynb)
  - **Respondida quando:** Consigo descrever o mapa polinomial de QSP/QSVT em termos de qual estrutura espectral ele processa.

- [ ] **Q-B2** — Por que QSVT exige block-encoding?
  - **Por que importa:** Block-encoding é o mecanismo que permite processar operadores não-unitários dentro do formalismo unitário do circuito quântico.
  - **Notebook:** [C-08](core/C-08_qsp_qsvt_entry_point.ipynb)
  - **Respondida quando:** Consigo construir um block-encoding trivial de uma matriz 2x2 e verificar que o processamento espectral funciona sobre ela.

- [ ] **Q-B3** — Em que sentido eigenvalue processing amplia o quadro do QSVT?
  - **Por que importa:** Papers recentes (Dong, Lin, Tong 2022+) ampliam o QSVT para eigenvalues. Entender por que isso é necessário é entender o limite do framework anterior.
  - **Notebook:** [C-08](core/C-08_qsp_qsvt_entry_point.ipynb)
  - **Respondida quando:** Consigo articular a diferença entre o que QSVT pode fazer e o que eigenvalue processing adiciona, com um exemplo minimal.

---

## Registro de Perguntas Respondidas

*(vazio — projeto em início)*
