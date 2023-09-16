#Elaborar um algoritmo que calcule a área e o perímetro de um quadrado

lado_valor = float(input('Qual o valor do lado do quadrado? (em centímetros)\n'))

def perimetro(a):
    return(4*a)

def area(a):
    return(a*a)
    

while True:
    print("Qual dessas opções você gostaria de calcular?")
    operação = int(input('1 para perímetro\n2 para área\n3 ambas operações\n'))
    
    if operação == 1:
        print('O valor do perímetro é' +' ' +str(perimetro(lado_valor)) +'cm')
        break
    elif operação == 2:
        print('O valor da área é '+ str(area(lado_valor)) + 'cm^2')
        break
    elif operação ==3:
        print('O perímetro é '+str(perimetro(lado_valor))+'cm' + ' e a área é ' +str(area(lado_valor)) + 'cm^2')
        break
    else:
        print("Operação não válida")






