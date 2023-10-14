# Algoritmo 5) Desenvolva um algoritmo para calcular as raízes de uma equação do 2º grau (Ax²+ Bx + C)
# sendo que os valores A, B e C são fornecidos pelo usuário.
print('Insira os valores de A, B e C para a equação de 2°grau')
valor_a = float(input('Valor A:'))
valor_b = float(input('Valor B:'))
valor_c = float(input('Valor C:'))

if valor_a == 0:
    print('Essa não é uma equação de 2°grau pois o valor A não pode ser igual a 0.') 
elif valor_a < 0:
    print('Esta equação não existe pois o denominador não pode ser negativo.')
elif valor_a > 0:
    delta = valor_b * valor_b - 4 * valor_a * valor_c
    raiz_de_delta = delta **(1/2)
    if delta < 0:
        print('A equação não possui raízes reais pois o delta é menor que 0.')
    elif delta == 0: 
        denominador = 2 * valor_a
        valor_final_x = -valor_b / denominador
        print('A equação possui ambas as raizas reais como ' + str(valor_final_x))
    elif delta > 0:
        denominador = 2 * valor_a
        baskara_positivo = -valor_b + raiz_de_delta
        baskara_negativo = -valor_b - raiz_de_delta
        valor_final_x1 = baskara_positivo / denominador
        valor_final_x2 = baskara_negativo / denominador
        print('Sua equação terá como resultado: \n''x1 = ' + str(valor_final_x1))
        print('x2 = ' + str(valor_final_x2))