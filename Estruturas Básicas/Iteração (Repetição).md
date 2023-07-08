#código 
# Iteração (Repetição)

Iteração são estruturas que possibilita iterar sobre listas e outros tipos de coleções.

Declaração

```python
for element in collection:
	<bloco de código>
```

Exemplo:

```python
for numero in [1,2,3,4,5]:
	print(numero)

# 1
# 2
# 3
# 4
# 5
```

### Acumulação de valores

É utilizar uma variável para acumular um valor enquanto estamos iterando sobre uma coleção de valores.

Exemplo

```python
soma = 0
for numero in [1,2,3,4,5]:
	soma = soma + numero # soma += numero

print(soma)
# result....
# 15
```

### Contador de valores por índice

Uma forma de contar valores dentro de uma coleção da um índice específico.

```python
name = "Priscilayne Campos de Resende"
letras = {}
for letra in name:
    if not(letra in letras):
        letras[letra] = 1
    else:
        letras[letra] += 1
        
print(letras)    

	
```

# Iteração (Repetição)

Iteração são estruturas que possibilita iterar sobre listas e outros tipos de coleções.

Declaração

```python
for element in collection:
	<bloco de código>
```

Exemplo:

```python
for numero in [1,2,3,4,5]:
	print(numero)

# 1
# 2
# 3
# 4
# 5
```

### Acumulação de valores

É utilizar uma variável para acumular um valor enquanto estamos iterando sobre uma coleção de valores.

Exemplo

```python
soma = 0
for numero in [1,2,3,4,5]:
	soma = soma + numero # soma += numero

print(soma)
# result....
# 15
```

### Contador de valores por índice

Uma forma de contar valores dentro de uma coleção da um índice específico.

```python
name = "Priscilayne Campos de Resende"
letras = {}
for letra in name:
    if not(letra in letras):
        letras[letra] = 1
    else:
        letras[letra] += 1
        
print(letras)    

	
```