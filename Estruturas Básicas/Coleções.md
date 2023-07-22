#código 
# Coleções

## Listas

```python

lista = ["a", "b", "c"]

print(lista[0]) # "a"
print(lista[1]) # "b"
print(lista[2]) # "c"
```

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