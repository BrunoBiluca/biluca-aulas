import os
#os.rename("Teste/Jedi.png","Output/Jedi.png")
# os.rename('Output/Jedi.png', 'Teste/Jedi.png')

#caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
# arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

#print(os.listdir('Teste'))

origem = "Teste"
destino = "Output"

for nome in os.listdir(origem):
    print(nome)
    if nome == 'Jedi.png':
        os.rename( origem +'/' + nome , destino+ '/' + nome)