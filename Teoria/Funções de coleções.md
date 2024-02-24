# Funções de coleções

## sum(coleção)

- [Documentação](https://www.w3schools.com/python/ref_func_sum.asp)

```python
valores = [3, 5, 6, 9]
soma = sum(valores)
# 23
```

Utilizando objetos complexos para a soma

```python
valores = [('Bruno', 23), ('Layne', 22), ('Filipe', 78)]
sum([valor[1] for valor in valores]) 
# 123

sum([valor[1] for valor in valores if v[1] > 30])
# 78
```

# filter(função, coleção)

Filter retorna um iterador onde os itens são filtrados de acordo com a função passada no primeiro argumento

- [Documentação filter](https://www.w3schools.com/python/ref_func_filter.asp)
- [Documentação de lambda function](https://www.w3schools.com/python/python_lambda.asp)

```python
valores = [('Bruno', 23), ('Layne', 22), ('Filipe', 78)]
list(filter(lambda valor: valor[1] > 30, valores))
# [('Filipe', 78)]
```

# map(função, coleção)

O map executa uma função específica para cada um dos itens da coleção.

- [Documentação map](https://www.w3schools.com/python/ref_func_map.asp)

```python
valores = [1, 2, 3, 4]
map(lambda x: x*x, valores)
# [1, 4, 9, 16]


def muito_melhor_que_o_teu(pessoa):
    if pessoa[0] == 'Filipe':
        pessoa.append("Não tem microfone")
    return pessoa

pessoas = [['Bruno', 23], ['Layne', 22], ['Filipe', 78]]
map(muito_melhor_que_o_teu, pessoas)
# ['Bruno', 23], ['Layne', 22], ['Filipe', 78, 'Não tem microfone']
```
