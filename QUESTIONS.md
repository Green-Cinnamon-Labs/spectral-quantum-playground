# Research Questions

Este é o arquivo central do projeto. Cada pergunta deve ter: por que ela importa, qual notebook tenta respondê-la, e qual evidência mínima conta como "respondida".

---

## Core

- [ ] O que exatamente um circuito quântico extrai de um operador?
  - **Por que importa:** Define o que computação quântica realmente faz, além de "aplicar portas".
  - **Notebook:** `03_phase_estimation_toy_models.ipynb`
  - **Respondida quando:** Consigo demonstrar que um circuito extrai informação espectral (fase) que não é diretamente acessível por leitura clássica simples, e identificar as hipóteses necessárias.

- [ ] Por que phase estimation pode ser vista como processamento espectral?
  - **Por que importa:** Phase estimation é o arquétipo de algoritmo quântico útil. Entender por que é "espectral" desmonta a ideia de que circuitos quânticos apenas "calculam coisas mais rápido".
  - **Notebook:** `03_phase_estimation_toy_models.ipynb`
  - **Respondida quando:** Consigo ligar diretamente a distribuição de medição ao espectro do unitário, com um exemplo numérico verificado classicamente.

- [ ] Quais propriedades de um problema sobrevivem à tradução para circuito?
  - **Por que importa:** A tradução nunca é gratuita. Perder de vista o que se preserva e o que se perde é o principal motivo de ilusão de vantagem quântica.
  - **Notebook:** `05_problem_to_operator_translation.ipynb`
  - **Respondida quando:** Tenho pelo menos dois exemplos de tradução com análise explícita do que foi preservado e do que foi sacrificado.

---

## Fundamentos

- [ ] O que exatamente é um estado quântico?
  - **Por que importa:** Confundir estado com vetor de probabilidades ou com string de bits é a fonte de mais mal-entendidos em computação quântica.
  - **Notebook:** `00_states_operators_measurements.ipynb`
  - **Respondida quando:** Consigo distinguir estado puro, misto e ensemble, e mostrar concretamente onde interferência aparece e onde não aparece.

- [ ] Por que a evolução precisa ser unitária?
  - **Por que importa:** Unitaridade não é uma restrição arbitrária — ela garante preservação de norma, reversibilidade e coerência. Entender isso é entender o que diferencia computação quântica de computação estocástica.
  - **Notebook:** `01_unitaries_spectrum_and_dynamics.ipynb`
  - **Respondida quando:** Mostro o que quebra quando uma "evolução" não é unitária (norma, reversibilidade) e por que isso fecha a porta para certas classes de operação.

- [ ] O que medição devolve, e o que ela destrói?
  - **Por que importa:** Medição é onde a computação quântica colapsa para um resultado clássico. Entender o custo do colapso é essencial para qualquer protocolo.
  - **Notebook:** `00_states_operators_measurements.ipynb`
  - **Respondida quando:** Demonstro projeção, colapso de estado e a diferença entre informação extraível antes e depois da medição.

- [ ] Onde entra a interferência de fato?
  - **Por que importa:** Interferência é o mecanismo central que separa computação quântica de computação probabilística clássica. Localizá-la concretamente é fundamental.
  - **Notebook:** `02_phase_kickback.ipynb`
  - **Respondida quando:** Mostro um caso onde interferência construtiva/destrutiva muda o resultado de uma computação de forma não reproduzível classicamente sem enumeração explícita.

---

## Pensamento Espectral

- [ ] O que o espectro de um operador diz sobre a computação?
  - **Por que importa:** O espectro determina dinâmica, estabilidade, e o que um algoritmo quântico pode extrair. Sem isso, phase estimation e Hamiltonian simulation são caixas pretas.
  - **Notebook:** `01_unitaries_spectrum_and_dynamics.ipynb`
  - **Respondida quando:** Ligo concretamente autovalores de um unitário à sua dinâmica temporal com pelo menos um exemplo de 2x2 e um de 4x4.

- [ ] Qual a diferença entre autovalores e valores singulares?
  - **Por que importa:** É a distinção que separa phase estimation de QSVT. Confundi-los é confundir os regimes em que cada algoritmo opera.
  - **Notebook:** `06_singular_values_vs_eigenvalues.ipynb`
  - **Respondida quando:** Tenho um exemplo onde os dois divergem e consigo articular qual algoritmo usa qual estrutura e por quê.

- [ ] Por que phase estimation é um algoritmo "espectral"?
  - **Por que importa:** Nomear corretamente o que phase estimation faz clarifica o que outros algoritmos quânticos estão tentando fazer por extensão.
  - **Notebook:** `03_phase_estimation_toy_models.ipynb`
  - **Respondida quando:** Consigo derivar a distribuição de saída do QPE a partir do espectro do operador de entrada, para um caso 2x2 ou 4x4.

---

## Tradução de Problemas

- [ ] Como um problema clássico vira operador, estado inicial e medição?
  - **Por que importa:** Esse é o coração da tese. Sem uma tradução explícita, computação quântica é um conjunto de experimentos sem aplicabilidade.
  - **Notebook:** `05_problem_to_operator_translation.ipynb`
  - **Respondida quando:** Traduzo um problema simples (busca, fatoração de fase, ou estimativa de valor médio) nos três componentes, com análise de custo.

- [ ] Toda formulação útil precisa passar por um unitário?
  - **Por que importa:** Block-encoding, QSVT e outros avanços recentes mostram que a resposta não é óbvia.
  - **Notebook:** `06_singular_values_vs_eigenvalues.ipynb`
  - **Respondida quando:** Mostro pelo menos um caso onde a formulação natural do problema não é unitária e explico como contornar isso (ou por que não vale a pena).

- [ ] O custo de preparação do estado mata a vantagem em quais casos?
  - **Por que importa:** Preparação de estado é muitas vezes ignorada em análises de complexidade quântica. Ela pode cancelar qualquer ganho.
  - **Notebook:** `05_problem_to_operator_translation.ipynb`
  - **Respondida quando:** Tenho pelo menos um exemplo concreto onde o custo de preparação cresce tão rápido quanto o ganho do algoritmo.

- [ ] Quais classes de problema admitem uma tradução limpa?
  - **Por que importa:** Entender as classes é entender os limites reais da computação quântica — não os limites de hardware, mas os limites estruturais.
  - **Notebook:** `05_problem_to_operator_translation.ipynb`, `07_qsp_qsvt_entry_point.ipynb`
  - **Respondida quando:** Consigo categorizar pelo menos três problemas distintos quanto à qualidade e custo da tradução.

---

## Ponte para a Fronteira

- [ ] O que QSP transforma: autovalores ou valores singulares?
  - **Por que importa:** A resposta determina em qual regime QSP opera e por que QSVT é uma generalização necessária.
  - **Notebook:** `07_qsp_qsvt_entry_point.ipynb`
  - **Respondida quando:** Consigo descrever o mapa polinomial de QSP/QSVT em termos de qual estrutura espectral ele processa.

- [ ] Por que QSVT exige block-encoding?
  - **Por que importa:** Block-encoding é o mecanismo que permite processar operadores não-unitários dentro do formalismo unitário do circuito quântico.
  - **Notebook:** `07_qsp_qsvt_entry_point.ipynb`
  - **Respondida quando:** Consigo construir um block-encoding trivial de uma matriz 2x2 e verificar que o processamento espectral funciona sobre ela.

- [ ] Em que sentido eigenvalue processing amplia o quadro do QSVT?
  - **Por que importa:** Papers recentes (Dong, Lin, Tong 2022+) ampliam o QSVT para eigenvalues. Entender por que isso é necessário é entender o limite do framework anterior.
  - **Notebook:** `07_qsp_qsvt_entry_point.ipynb`
  - **Respondida quando:** Consigo articular a diferença entre o que QSVT pode fazer e o que eigenvalue processing adiciona, com um exemplo minimal.

---

## Registro de Perguntas Respondidas

*(vazio — projeto em início)*
