from Atividade2F import calcular_triangulo
from atividade3F import calcular_trapezio


while True:
    tipo_operacao = input("O que voce deseja calcular, area ou perimetro?")

    if tipo_operacao == 'area':
        lado_area = int(input('Qual a medida do lado do quadrado?'))
        resultado_area = lado_area * lado_area
        print('seu quadrado tem uma área de ' + str(resultado_area) + 'cm')
        break
    elif  tipo_operacao ==  'perimetro':
        lado_perimetro = int(input('Qual a medida do lado do quadrado?'))
        resultado_perimetro = 4 * lado_perimetro
        print('seu quadrado tem um perímetro de ' + str(resultado_perimetro) + 'cm')
        break
    elif tipo_operacao == "triangulo":
        calcular_triangulo()
        break
    elif tipo_operacao == "trapezio":
        calcular_trapezio()
        break
    else:
        print('Comando inválido T-T, insira (area) ou (perimetro)')