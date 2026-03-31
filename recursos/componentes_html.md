# Componentes HTML reutilizáveis

Padrões visuais para usar nas células markdown dos notebooks.
Copiar o bloco HTML e substituir o conteúdo.

---

## Etimologia

Para introduzir a origem de um termo antes de defini-lo formalmente.
Tom: leve, lateral — não é uma definição, é contexto.

```html
<div style="border-left: 2px solid #6b7280; padding: 0.5em 1em 0.5em 1.1em; margin: 0.8em 0 1.2em 0; background: rgba(107, 114, 128, 0.05); border-radius: 0 3px 3px 0;">
  <span style="font-size: 0.65em; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #9ca3af;">etimologia</span><br>
  <span style="font-size: 0.88em; line-height: 1.65;">TEXTO AQUI</span>
</div>
```

**Exemplo — palavra única:**

```html
<div style="border-left: 2px solid #6b7280; padding: 0.5em 1em 0.5em 1.1em; margin: 0.8em 0 1.2em 0; background: rgba(107, 114, 128, 0.05); border-radius: 0 3px 3px 0;">
  <span style="font-size: 0.65em; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #9ca3af;">etimologia</span><br>
  <span style="font-size: 0.88em; line-height: 1.65;"><b>Computar</b> vem do latim <i>computare</i>: <i>com-</i> ("junto", "em conjunto") + <i>putare</i> ("calcular", "avaliar", "contar" — e originalmente "podar", no sentido de limpar para apurar). A ideia original é a de contar ou calcular reunindo elementos; depois, o termo ganhou o sentido de processar informação segundo regras.</span>
</div>
```

**Exemplo — dois termos:**

```html
<div style="border-left: 2px solid #6b7280; padding: 0.5em 1em 0.5em 1.1em; margin: 0.8em 0 1.2em 0; background: rgba(107, 114, 128, 0.05); border-radius: 0 3px 3px 0;">
  <span style="font-size: 0.65em; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #9ca3af;">etimologia</span><br>
  <span style="font-size: 0.88em; line-height: 1.65;"><b>Mecânica</b> vem do grego <i>mēkhanikḗ</i> ("máquina", "engenho"); em latim <i>mechanica</i>, sempre com a ideia de estudar movimento e forças.<br><b>Quântica</b> vem do latim <i>quantus</i> ("quanto", "quanto de quantidade") — entrou na física pela noção de <i>quantum</i>: uma quantidade discreta, um "pacote" mínimo.</span>
</div>
```

---

## Nota explicativa (após fórmula)

Aparece logo abaixo de uma expressão matemática para traduzir o formalismo em linguagem direta.
Tom: não é uma definição paralela — é "o que essa expressão está dizendo na prática".

```html
<div style="margin: -0.6em 0 1.4em 0; font-size: 0.87em; color: #6b7280; line-height: 1.65; padding-left: 1.1em; border-left: 2px solid #374151;">
  TEXTO AQUI
</div>
```

**Exemplo:**

```html
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad \alpha, \beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1$$

<div style="margin: -0.6em 0 1.4em 0; font-size: 0.87em; color: #6b7280; line-height: 1.65; padding-left: 1.1em; border-left: 2px solid #374151;">
  O estado quântico é uma combinação dos dois estados básicos |0⟩ e |1⟩. Os coeficientes α e β são amplitudes complexas — não probabilidades, mas o que as gera. Ao medir, cada amplitude vira probabilidade via |α|², e por isso a soma precisa ser 1.
</div>
```

---

## Link de digressão (inline)

Aparece no meio de uma frase para apontar para um notebook de digressão sem interromper o fluxo.
Tom: secundário, quase uma nota de rodapé — quem quiser se aprofundar segue; quem não quiser, ignora.

```html
<a href="CAMINHO" style="font-size: 0.82em; color: #6b7280; text-decoration: none; border-bottom: 1px dashed #6b7280; white-space: nowrap;">↳ LABEL</a>
```

**Exemplo — no final de uma frase:**

```html
Por que é possível computar com um qubit?
<a href="../digressoes/D-00_o_que_e_um_qubit.ipynb" style="font-size: 0.82em; color: #6b7280; text-decoration: none; border-bottom: 1px dashed #6b7280; white-space: nowrap;">↳ o que é um qubit</a>
```

**Exemplo — como item de lista ao fim de uma seção:**

```html
<a href="../digressoes/D-01_regra_de_born_e_colapso.ipynb" style="font-size: 0.82em; color: #6b7280; text-decoration: none; border-bottom: 1px dashed #6b7280; white-space: nowrap;">↳ regra de Born e colapso</a>
```

---

## Aviso / destaque

Para chamar atenção a um ponto que costuma ser mal interpretado.

```html
<div style="border-left: 2px solid #f59e0b; padding: 0.5em 1em 0.5em 1.1em; margin: 0.8em 0 1.2em 0; background: rgba(245, 158, 11, 0.05); border-radius: 0 3px 3px 0;">
  <span style="font-size: 0.65em; font-weight: 700; letter-spacing: 0.13em; text-transform: uppercase; color: #f59e0b;">atenção</span><br>
  <span style="font-size: 0.88em; line-height: 1.65;">TEXTO AQUI</span>
</div>
```
