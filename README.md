# Processador de Arquivos

Software que processa arquivos usando Python + Poetry.

## 🚀 Funcionalidade atual

- Conversão de imagens entre formatos (ex.: JPG → PNG)
- Detecção automática do tipo de arquivo usando python-magic
- Interface de linha de comando construída com Typer

## 📦 Como instalar

Instale as dependências:

poetry install


## ▶️ Como usar

Execute o conversor passando o arquivo de entrada e o arquivo de saída:



poetry run python src/conversor/main.py "caminho/entrada.jpg" "caminho/saida.png"


## 🛠 Tecnologias usadas

- Python
- Poetry
- Pillow
- python-magic
- Typer 

## 🐳 Como Rodar a Aplicação com Docker

Após a instalação do Docker Desktop, você pode usar nossa aplicação em qualquer sistema sem instalar Python ou dependências.

### 1. Puxar a Imagem (Download)

A imagem final do nosso conversor está hospedada no GitHub Container Registry (`ghcr.io`). Usaremos a tag final da versão, que será a `v1.0.0`.

```bash
docker pull ghcr.io/pedrohensc/processador-arquivos:v1.0.0

### 2. Executar o Conversor

Para que o container consiga ler o arquivo de imagem do seu computador e salvar a saída, é obrigatório mapear a sua pasta local para o container usando o parâmetro `-v` (Volume).

O container está configurado para ler e escrever na pasta `/app/data` interna.

**Exemplo de Uso (Assumindo que você está na pasta com a imagem):**

```bash
docker run --rm \
    -v $(pwd):/app/data \
    ghcr.io/pedrohensc/processador-arquivos:v1.0.0 \
    convert /app/data/entrada.jpg --to png