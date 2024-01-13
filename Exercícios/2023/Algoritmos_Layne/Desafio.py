from Algoritmos_Layne.Areas import area_triangulo
from Algoritmos_Layne.Areas import area_trapezio
from Algoritmos_Layne.Areas import quadrado

while True:
    print('Qual dessas operações você gostaria de calcular?(em centímetros)\n')
    operação= int(input('1: Área e/ou perímetro do quadrado\n2: Área de um triângulo\n3: Área do trapézio\n'))
    if operação ==1:
        quadrado()
    elif operação == 2:
        area_triangulo()
    elif operação == 3:
        area_trapezio()
    else:
        print('Operação não válida, digite o número correspondente\n')
    
    retornar = int(input('Deseja fazer outra operação? Se sim, digite 1\n'))
    if retornar != 1:
        break