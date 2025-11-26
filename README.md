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