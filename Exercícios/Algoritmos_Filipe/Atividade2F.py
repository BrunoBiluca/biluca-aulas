def calcular_triangulo():
    base = float(input("Digite o valor da base do seu triangulo."))
    altura = float(input("Digite o valor da altura do seu triangulo."))

    area = base * altura / 2
    print("Seu triangulo tem uma area de " + str(area) + "cm")


if __name__ == "__main__":
    calcular_triangulo()