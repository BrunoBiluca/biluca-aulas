file = open("controle_financeiro.csv", "r")

line_number = 0
values_sum = 0
for line in file:
    line_number += 1
    if line_number == 1:
        continue

    entrada = line.replace("\n", "")
    valor = entrada.split(",")[1]
    values_sum += int(valor)

print(f'''Total gasto com firulagens: R$ {str(values_sum)},00''')