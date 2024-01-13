# Algoritmo para achar as raízes de uma função de segundo grau 

def delta(a,b,c):
    return(b*b - 4*a*c)

def delta_raiz(a):
    return(a**(1/2))

def raiz_1(a,b,c):
    return(-b+c)/2*a

def raiz_2(a,b,c):
    return(-b-c)/2*a

while True:
    a = float(input('Qual o valor de a?\n'))
    b = float(input('Qual o valor de b?\n'))
    c = float(input('Qual o valor de c?\n'))
    
    resultado_delta = delta(a,b,c)
    resultado_raiz_delta = delta_raiz(resultado_delta)
    raiz1 = raiz_1(a,b,resultado_raiz_delta)
    raiz2 = raiz_2(a,b,resultado_raiz_delta)
    
    if a != 0:
        if resultado_delta > 0: 
            print('As raízes da função são ' + str(raiz1) + ' e ' + str(raiz2))
        elif resultado_delta == 0:
            print('A raíz da função é '+ str(raiz1))
        else:
            print('Não existem raízes reais')

    else:
        print('Esta não é uma função de segundo grau')

    retornar = int(input('Deseja fazer outra operação? Se sim, digite 1\n'))
    if retornar != 1:
        break

