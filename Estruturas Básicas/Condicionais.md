#código 
# Condicionais

Condicionais são estruturas que possibilitam a execução do código de tomar mais de um caminho.

Declaração

```python
if <condição>:
	<bloco de código>
elif <condição>:
	<bloco de código>
else:
	<bloco de código>
```

Exemplos:

```python
if corote == "Pêssego" or corote == "Menta":
	print("Triste")
elif corote == "Azul":
	print("Muito triste")
else:
	print("Feliz")
```

Operadores Lógicos:

And: Cria uma condição onde um numero é verdadeiro apenas quando cumpre duas ou mais regras.

Or: Se pelo menos uma das condições for verdadeira o resultado será verdadeiro.

Not: Inverte o resultado. Se o resultado da expressão for True,
o operador retorna false, e vice-versa.