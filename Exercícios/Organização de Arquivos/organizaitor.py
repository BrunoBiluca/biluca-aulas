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
video = "Output/Vídeos"
outros = "Output/Outros"

def transferencia_de_arquivos(origem,arquivo,finais):
    if not os.path.isdir(arquivo):
        os.mkdir(arquivo)
        print("A pasta não existe!")

    for nome in os.listdir(origem):
        print('arquivo encontrado: ' + nome)
        if nome.endswith(finais):
            os.rename(origem +'/' + nome , arquivo + '/' + nome)
            print('Foi movido o aquivo: ' + nome + ' para a pasta ' + arquivo + '.')
        print('')


transferencia_de_arquivos(origem,imagem,tuple([".png", ".jpg"]))

transferencia_de_arquivos(origem,documento,tuple([".txt", ".rtf"]))

transferencia_de_arquivos(origem,video,tuple([".mp4", ".MOV"]))

transferencia_de_arquivos(origem,outros,tuple([".fbx"]))


