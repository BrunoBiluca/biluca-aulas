import sys


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
contador_produtos = 0
valor_max = 0
valor_min = 1000000
maior_nome_produto = ""
menor_nome_produto = ""

for linha_pura in linhas_valores:
    contador_produtos += 1
    linha_sem_quebra = linha_pura.replace("\n", "")
    valores = linha_sem_quebra.split(sep=",")
    print(valores[0], valores[1])
    nome = valores[0]
    valor = int(valores[1])
    soma += valor
    valor_medio = soma / contador_produtos

    if valor > valor_max:
         valor_max = valor
         maior_nome_produto = nome

    if valor < valor_min:
         valor_min = valor
         menor_nome_produto = nome

print(f'''\nTotal gasto com firulagens: R$ {str(soma)},00''')
print("A média de preços é de R$" + str(valor_medio) + ",00.")
print("o Produto de maior valor foi o " + str(maior_nome_produto) + " custando R$" + str(valor_max) + ",00")
print("o Produto de menor valor foi o " + str(menor_nome_produto) + " custando R$" + str(valor_min) + ",00")