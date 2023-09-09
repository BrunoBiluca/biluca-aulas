#Elaborar um algoritmo que calcule a área e o perímetro de um quadrado

lado_valor = float(input('Qual o valor do lado do quadrado?\n'))
print("Qual dessas opções você gostaria de calcular?")
operação = int(input('1 para perímetro\n2 para área\n'))

def perimetro(a):
    return(4*a)

def area(a):
    return(a*a)

if operação == 1:
    print(perimetro(lado_valor))
elif operação == 2:
    print(area(lado_valor))
else:
    print("Operação não válida")





