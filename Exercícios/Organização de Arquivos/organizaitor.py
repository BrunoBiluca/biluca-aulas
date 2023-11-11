import os
#os.rename("Teste/Jedi.png","Output/Jedi.png")
# os.rename('Output/Jedi.png', 'Teste/Jedi.png')

#caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
# arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

#print(os.listdir('Teste'))

origem = "Teste"
destino = "Output"
imagem = "Output/Imagem"

if not os.path.isdir(imagem):
    os.mkdir(destino + '/Imagem')
    print("A pasta não existe!")

for nome in os.listdir(destino):
    print('arquivo encontrado: ' + nome)
    if nome.endswith(tuple([".png", ".jpg"])):
        os.rename( destino +'/' + nome , imagem + '/' + nome)
        print('Foi movido o aquivo: ' + nome + ' para a pasta ' + imagem + '.')
    print('')

