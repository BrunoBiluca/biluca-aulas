import os
#os.rename("Teste/Jedi.png","Output/Jedi.png")
# os.rename('Output/Jedi.png', 'Teste/Jedi.png')

#caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
# arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

#print(os.listdir('Teste'))

origem = "Teste"
destino = "Output"
imagem = "Output/Imagens"
documento = "Output/Documentos"

def transferencia_de_imagens(origem,imagem):
    if not os.path.isdir(imagem):
        os.mkdir(imagem)
        print("A pasta não existe!")

    for nome in os.listdir(origem):
        print('arquivo encontrado: ' + nome)
        if nome.endswith(tuple([".png", ".jpg"])):
            os.rename(origem +'/' + nome , imagem + '/' + nome)
            print('Foi movido o aquivo: ' + nome + ' para a pasta ' + imagem + '.')
        print('')

def transferencia_de_documentos(origem,documento):
    if not os.path.isdir(documento):
        os.mkdir(documento)
        print("A pasta não existe!")

    for nome in os.listdir(origem):
        print('arquivo encontrado: ' + nome)
        if nome.endswith(tuple([".txt", ".rtf"])):
            os.rename(origem +'/' + nome , documento + '/' + nome)
            print('Foi movido o aquivo: ' + nome + ' para a pasta ' + documento + '.')
        print('')

transferencia_de_imagens(origem,imagem)
transferencia_de_documentos(origem,documento)