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