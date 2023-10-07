# Algoritmo 4) Crie um algoritmo que leia dois números inteiros e que depois mostre:
# O primeiro valor elevado ao segundo valor (ok)
# O primeiro valor vezes o segundo valor (ok)
# O número inverso do primeiro valor (se não souber o que é o valor inverso, pesquise) (ok)?
# A soma do segundo número com a metade do primeiro número (ok)
# A diferença do primeiro número com o segundo (ok)
# O valor oposto do segundo número

num1 = float(input('Insira dois números \n' + '1°num(x): '))
num2 = float(input('2°num(y): '))

n1_elevado_n2 = num1 ** num2
print('x^y = ' + str(n1_elevado_n2))
n1_vezes_n2 = num1 * num2
print('x*y = ' + str(n1_vezes_n2))
inverso_n1 = '1/' + str(num1)
print('1/x = ' + inverso_n1)
soma_n2_metade_n1 = num2 + (num1 / 2)
print('y+x/2 = ' + str(soma_n2_metade_n1))
diferenca_n2_n1 = num2 - num1
print('y-x = ' + str(diferenca_n2_n1))
oposto_n2 = num2 * -1
print('O oposto de y é: ' + str(oposto_n2))