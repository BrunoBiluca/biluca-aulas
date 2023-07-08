#código


> [!info] Documentação do Python
> https://docs.python.org/pt-br/3/tutorial/index.html

> [!info] Aprenda a programar do Luciano Ramalho
> https://wiki.python.org.br/DocumentacaoPython?action=AttachFile&do=view&target=Aprenda_a_Programar-Luciano_Ramalho.pdf


# Variáveis

Variáveis são estruturas que armazenam valores. São um nome que damos para uma posição de memória.

Exemplos de declarações de variáveis:

```python
# Variáveis primitivas
texto = "Brunin é top demais, melhor professor!"
numero = 13091992
bruno_eh_bonito = True
filipe_nao_sabe_as_variaveis = False
```

# Coleções

## Listas

> [!warning] Fazer a descrição

## Dicionários

Dicionários são coleções que organização seus elementos por **chave e valor**.

Declaração

```python
dict = {
  "key": value
}
```

Exemplos

```python
classe_de_pogamacao = {
	"bruno": 30,
	"pryscylayne": 32,
	"filipe": 28
}

print(classe_de_pogamacao["bruno"])
# 30
print(classe_de_pogamacao["pryscylayne"])
# 32
```

```python
classe_de_pogamacao = {
	31: ["pryscylayne"],
	21: ["bruno", "filipe"]
}

print(classe_de_pogamacao[31])
# ["pryscylayne"]
print(classe_de_pogamacao[21])
# ["bruno", "filipe"]
```

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