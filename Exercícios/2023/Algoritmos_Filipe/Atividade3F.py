def calcular_trapezio():
    base_maior = float(input("Digite o valor da menor base do seu trapézio."))
    base_menor = float(input("Digite o valor da maior base do seu trapézio."))
    altura = float(input("Qual a altura do trapézio?"))

    soma_bases = base_maior + base_menor
    area = soma_bases * altura / 2
    print("O seu trapézio tem uma área de " + str(area) + "cm")