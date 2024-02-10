def abrir_arquivo(caminho_arquivo) -> list[str]:
    modo_abertura = "r"
    texto_arquivo = open(caminho_arquivo, modo_abertura)
    linhas_arquivo = texto_arquivo.readlines()
    print("Arquivo", caminho_arquivo, "aberto com", len(linhas_arquivo), "linhas")
    return linhas_arquivo

linhas_arquivo = abrir_arquivo("controle_financeiro.csv")
linhas_valores = linhas_arquivo[1:] 


def quebra_linha(linhas_arquivo):
    lista_controle = []
    for linha_pura in linhas_arquivo:
        linha_sem_quebra = linha_pura.replace("\n", "")
        valores = linha_sem_quebra.split(sep=",")
        lista_controle.append(valores)
    return lista_controle

print("\n- Todos os valores")
soma = 0
contador = 0
for linha_pura in linhas_valores:
    linha_sem_quebra = linha_pura.replace("\n", "")
    valores = linha_sem_quebra.split(sep=",")
    print(valores[0], valores[1])
    valor = int(valores[1])
    soma += valor
    contador += 1
   
    
print(f'\nA soma total dos gastos foi de {soma} reais')
print(f'''\nA média dos gastos foi de  {str((soma)/(contador))} reais''')

maior_valor = 0
nome_maior = ''

for linha_pura in linhas_valores:
    linha_sem_quebra = linha_pura.replace("\n", "")
    valores = linha_sem_quebra.split(sep=",")
    nome = valores[0]
    valor = int(valores[1])
    if valor > maior_valor:
        maior_valor = valor
        nome_maior = nome

print(f'\nO ítem de maior valor é {nome_maior} : {maior_valor} reais')

menor_valor = maior_valor
nome_menor = ''    

for linha_pura in linhas_valores:
    linha_sem_quebra = linha_pura.replace("\n", "")
    valores = linha_sem_quebra.split(sep=",")
    nome = valores[0]
    valor = int(valores[1])
    if valor < menor_valor:
        menor_valor = valor
        nome_menor = nome

print(f'\nO ítem de menor valor é {nome_menor} : {menor_valor} reais')

nome_igual_maior = ''
nome_igual_menor = ''

for linha_pura in linhas_valores:
    linha_sem_quebra = linha_pura.replace("\n", "")
    valores = linha_sem_quebra.split(sep=",")
    nome = valores[0]
    valor = int(valores[1])
    if menor_valor == valor and nome != nome_menor:
        nome_igual_menor = nome
    if maior_valor == valor and nome != nome_maior:
        nome_igual_maior = nome


if nome_igual_maior == '':
    print(f'\nNão há ítens máximos iguais')
else:
    print(f'\n{nome_igual_maior} possui mesmo valor que {nome_maior}')

if nome_igual_menor == '':
    print(f"\nNão há ítens mínimos iguais")
else:
    print(f'\n{nome_igual_menor} possui mesmo valor que {nome_menor}')