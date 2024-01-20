def area_triangulo(base, altura):
    return base*altura/2


def entradas():
    base = float(input('Qual o valor da base do triângulo?\n'))
    altura = float(input('Qual o valor da altura do triângulo?\n'))
    return base, altura


def exibir_area(area):
    print('O valor da área é ' + str(area) + 'cm^2')


if __name__ == "__main__":
    base, altura = entradas()
    area = area_triangulo(base, altura)
    exibir_area(area)
