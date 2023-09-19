#Elaborar um algoritmo que calcule a área e o perímetro de um quadrado (ok)
#Fazer um algoritmo que calcule a área de um triângulo (ok)
#Fazer um algoritmo que calcule a área de um trapézio (ok)
#Fazer um programa onde o usuário escolhe qual a área que ele quer calcular (ok)

def area_triangulo(a,b):
    return(a*b/2)

def area_trapezio(a,b,c):
    return((a+b)*c/2)

def quadrado(a):
    if tipo_quadrado == 1:
        return (4*a)
    else:
        return (a*a)

def resposta_perimetro(b):
    return('O valor do perímetro é ' + str(b) + 'cm')

def resposta_area(b):
    return('O valor da área é ' + str(b) + 'cm^2')

while True:
    print('Qual dessas operações você gostaria de calcular?(em centímetros)\n')
    operação= int(input('1: Área e/ou perímetro do quadrado\n2: Área de um triângulo\n3: Área do trapézio\n'))

    if operação == 1:
        print('Escolha uma opção\n')
        tipo_quadrado= int(input('1: perímetro\n2: área\n'))
        if tipo_quadrado == 1 or tipo_quadrado == 2:
            valor_lado = float(input('Qual o valor do lado do quadrado?\n'))
            resultado_quadrado = quadrado(valor_lado)
            if tipo_quadrado == 1:
                print(resposta_perimetro(resultado_quadrado))
            else:
                print(resposta_area(resultado_quadrado))
        else:
            print('Operação não válida, digite o número correspondente')
    
    elif operação == 2:
        base = float(input('Qual o valor da base do triângulo?\n'))
        altura = float(input('Qual o valor da altura do triângulo?\n'))
        resultado_triangulo = area_triangulo(base,altura)  
        print(resposta_area(resultado_triangulo))

    elif operação == 3:
        base_maior = float(input('Qual o valor da base maior?\n'))
        base_menor = float(input('Qual o valor da base menor?\n'))
        altura_trapezio = float(input('Qual o valor da altura?\n'))
        resultado_trapezio = area_trapezio(base_maior,base_menor,altura_trapezio)
        print(resposta_area(resultado_trapezio))
        
    else:
        print('Operação não válida, digite o número correspondente\n')
    
    retornar = int(input('Deseja retornar?Se sim, digite 1\n'))
    if retornar != 1:
        break
    
