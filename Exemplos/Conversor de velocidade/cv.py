velocidade_hora = input("Insira a velocidade a ser convertida\n")
velocidade_segundo = float(velocidade_hora) / 3.6
tempo = 435 / float(velocidade_hora)

print("Você estará viajando a %.2f M/s" % velocidade_segundo)
print("e chegará em seu destino em aproximadamente %.2f Horas" % tempo)