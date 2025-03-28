FROM python:3.10-slim

# COMANDOS GLOBAIS: Instalação de dependências do sistema
RUN apt-get update && \
    apt-get install -y curl default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/* && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get update

# Definir o diretório de trabalho
WORKDIR /app_exemplo

# Copiar e instalar dependências Python

COPY requirements.txt .
COPY serverless.yaml .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o Serverless e o plugin serverless-offline
RUN npm install -g serverless@3
RUN serverless plugin install -n serverless-offline

# Copiar o restante do código da aplicação


# Definir o PYTHONPATH para o diretório correto
ENV PYTHONPATH=/app_exemplo

# Expor a porta 3000 onde o serverless-offline vai rodar
EXPOSE 3000

# Comando para rodar o serverless offline
CMD ["serverless", "offline", "--host", "0.0.0.0"]
