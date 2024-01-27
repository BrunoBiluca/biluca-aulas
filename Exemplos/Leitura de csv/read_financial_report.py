def abrir_arquivo(caminho_arquivo) -> list[str]:
    modo_abertura = "r"
    texto_arquivo = open(caminho_arquivo, modo_abertura)

    # Leitura do arquivo em linhas
    linhas_arquivo = texto_arquivo.readlines()
    print("Arquivo", caminho_arquivo, "aberto com", len(linhas_arquivo), "linhas")
    return linhas_arquivo


linhas_arquivo = abrir_arquivo("controle_financeiro.csv")
linhas_valores = linhas_arquivo[1:] # Pula o cabeçalho

print("\n- Todos os valores")
soma = 0
# Iterar sobre as linhas do arquivo
for linha_pura in linhas_valores:
    # Transformação da linha pura em uma linha sem a quebra de linha
    linha_sem_quebra = linha_pura.replace("\n", "")

    # Transformação da linha com os valores de despesas e valor quebrados
    valores = linha_sem_quebra.split(sep=",")
    print(valores[0], valores[1])

    # Conversão do valor em string para um inteiro para poder somar
    valor = int(valores[1])
    soma += valor

print(f'''\nTotal gasto com firulagens: R$ {str(soma)},00''')