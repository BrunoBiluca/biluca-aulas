print("Você é um gato que está entediado de ficar no quarto e deve encontrar o humano para que ele possa abrir a porta e você sair")
#print('Você está em uma parte vazia do quarto')

tipo_parte = 'humano'
if tipo_parte == 'vazia':
    print('Você está em uma parte vazia do quarto')
elif tipo_parte == 'humano':
    print('Você está em uma parte com o humano')
elif tipo_parte == 'saida':
    print('Você está na saída do quarto')

comandos = input("O que vc quer fazer? ")
if comandos == 'encontrar o humano':
    if  tipo_parte == 'humano':
        print('Você encontrou o humano')
    else:
        print('O humano não está aqui')
else:
    print('Comando inválido')