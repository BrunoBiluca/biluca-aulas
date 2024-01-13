def area_triangulo():
    base = float(input('Qual o valor da base do triângulo?\n'))
    altura = float(input('Qual o valor da altura do triângulo?\n'))
    resultado = base*altura/2
    print('O valor da área é ' + str(resultado) + 'cm^2')


if __name__ == "__main__":
    area_triangulo()
