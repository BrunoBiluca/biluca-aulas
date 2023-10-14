def area_triangulo():
    base = float(input('Qual o valor da base do triângulo?\n'))
    altura = float(input('Qual o valor da altura do triângulo?\n'))
    resultado = base*altura/2
    print('O valor da área é ' + str(resultado) + 'cm^2')  
    return

def area_trapezio():
    base_maior = float(input('Qual o valor da base maior?\n'))
    base_menor = float(input('Qual o valor da base menor?\n'))
    altura_trapezio = float(input('Qual o valor da altura?\n'))
    resultado = (base_maior+base_menor)*altura_trapezio/2
    print('O valor da área é ' + str(resultado) + 'cm^2')  
    return

def quadrado():
    print('Escolha uma opção\n')
    tipo_quadrado= int(input('1: perímetro\n2: área\n'))
    if tipo_quadrado == 1:
        valor_quadrado = float(input('Qual o valor do lado do quadrado?\n'))
        resultado = 4*valor_quadrado
        print ('O valor do perímetro é ' + str(resultado) + 'cm')
    elif tipo_quadrado ==2:
        valor_quadrado = float(input('Qual o valor do lado do quadrado?\n'))
        resultado = valor_quadrado*valor_quadrado
        print ('O valor da área é ' + str(resultado) + 'cm^2')
    else:
        print('Operação não válida')
    return

