print("Você é um parasito e deve encontrar a proteína de membrana para escapar da célula")
#print('Você está em uma parte vazia da célula')

tipo_parte = 'proteína'
if tipo_parte == 'vazia':
    print('Você está em uma parte vazia da célula')
elif tipo_parte == 'proteína':
    print('Você está em uma parte proteíca')
elif tipo_parte == 'saida':
    print('Você está na saída da célula')

comandos = input("O que vc quer fazer? ")
if comandos == 'Pegar a proteína':
    if  tipo_parte == 'proteína':
        print('Você pegou a proteína')
    else:
        print('Não há proteína aqui')
else:
    print('Comando inválido')