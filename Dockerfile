# Dockerfile para empacotamento da aplicação Processador de Arquivos (Poetry/Python)
FROM python:3.11-slim

# 2. DIRETÓRIO DE TRABALHO
WORKDIR /app

# 3. INSTALAÇÃO DE DEPENDÊNCIAS DO POETRY:
# Copia os arquivos de configuração do Poetry.
COPY pyproject.toml poetry.lock ./

# Instala o poetry, as dependências, e limpa o cache.
RUN pip install poetry && poetry install --no-root --no-dev && poetry cache clear --all pypi -n

# 4. CÓDIGO DA APLICAÇÃO
# Copia o restante do código da aplicação.
COPY . .

# 5. EXPOSIÇÃO DA ENTRADA DO USUÁRIO
VOLUME /app/data

# 6. PONTO DE ENTRADA (Como o programa será executado)
# ATENÇÃO: Substitua 'conversor_cli.py' pelo nome exato do arquivo/módulo principal
ENTRYPOINT ["poetry", "run", "python", "conversor_cli.py"]