# Organização de arquivos

Escrever um programa em python que dada uma pasta ele deve conseguir organizar em novas pasta os arquivos existentes na pasta original.

- O programa deve receber um arquivo json como parâmetro para definir a configuração dos caminhos.

Formato do arquivo de entrada:

```json
{
	"original_folder": "",
	"output_path": {
		"imagens": "",
		"documentos": "",
		"videos": "",
		"outros": "",
	}
}
```

- O programa irá separar os arquivos em relação ao tipo de cada arquivo
    - pasta de imagens: arquivos de imagens como: png, jpeg, gif
    - pasta de vídeos: arquivos de vídeos como: mp4
    - pasta de documentos: arquivos de documentos como: pdf, epub, word
    - pasta de outros: um tipo de arquivo não identificado

- Quando o programa rodar é importante exibir algumas informações para o usuário
    - Quantos arquivos contém na pasta original
    - Exibição das etapas do programa
        - movendo arquivos de imagens
        - movendo arquivos de documentos
    - Quantos arquivos foram movidos para cada pasta
    - Conclusão do processo

### Desenvolvimento

Etapas para a conclusão do programa:

- (ok) Mover um arquivo específico de uma pasta para outra
- (ok) Listar os arquivos de uma pasta 
- (ok) Mover um arquivo pelo tipo para uma pasta
- (ok) Identificar os arquivos pelos tipos
- Mover arquivos do tipo de imagem
- Mover arquivos do tipo de documento
- Mover arquivos do tipo de vídeos
- Mover arquivos não identificados
- Ler o arquivo de entrada
- Configurar de acordo com o arquivo de entrada as pastas específicas
- Adicionar mensagens para o usuário

### Exemplo

Seja uma pasta com vários tipos de arquivos armazenados, queremos separar os arquivos pelos seus tipos.

```
📂 pasta
 ┣ 🖼️ player
 ┣ 🧊 player
 ┣ 🧊 enemy_1
 ┣ 📜 player_movement
 ┣ 📜 player_attack
 ┣ 📜 enemy
 ┣ 📜 enemy_attack_1
 ┣ 📦 player
 ┣ 📦 enemy_1
 ┣ 📦 enemy_2
 ┣ 🖼️ hud
 ┣ 🖼️ enemy_1
 ┗ 🖼️ enemy_2
```

Rodando o script com a configuração:

```json
{
	"original_folder": "pasta",
	"output_path": {
		"imagens": "pasta/imagens",
		"documentos": "pasta/documentos",
		"videos": "pasta/videos",
		"outros": "pasta/outros"
	}
}
```

Resultado final

```
📂 pasta
 ┣ 📂 imagens
 ┃ ┣ 🖼️ player
 ┃ ┣ 🖼️ hud
 ┃ ┣ 🖼️ enemy_1
 ┃ ┗ 🖼️ enemy_2
 ┣ 📂 outros
 ┃ ┣ 🧊 player
 ┃ ┣ 🧊 enemy_1
 ┃ ┗ 🧊 enemy_2
 ┣ 📂 documentos
 ┃ ┣ 📜 player_movement
 ┃ ┣ 📜 player_attack
 ┃ ┣ 📜 enemy
 ┃ ┣ 📜 enemy_attack_1
 ┃ ┣ 📜 enemy_attack_2
 ┃ ┗ 📜 player_hud
 ┗ 📂 videos
   ┣ 📦 player
   ┣ 📦 enemy_1
   ┣ 📦 enemy_2
   ┗ 📦 hud

```