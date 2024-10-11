# Pipeline HuggingFace Hackernews

Projeto desenvolvido como desafio técnico para o papel de Data Engineer.

## Instruções de instalação (primeira utilização)

É necessário ter o Python versão 3.10 instalado. 

O gerenciador de pacotes utilizado neste projeto é o uv. Para instalá-lo, pode-se executar o seguinte comando:

```bash
pipx install uv
```

ou

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Após isso, pode-se instalar a versão necessária de Python com o comando:

```bash
uv install python 3.10
```

### Ingestão (dlt)

Para instalar o projeto de ingestão de dados, deve-se executar o comando uv sync no diretório ingestion.

```bash
cd ingestion 
uv sync
```

### Transformação (dbt) 

Para instalar o projeto de ingestão de dados, deve-se executar o comando uv sync no diretório ingestion.

```bash
cd transformation 
uv sync
```

-----

## Executar o projeto

### Variáveis de ambiente

Antes de executar as etapas de ingestão e transformação, é necessário definir as variáveis de ambiente para ambos os processos.

#### Ingestion

Crie um arquivo nomeado 'secrets.toml' no diretório '.dlt', dentro do diretório 'ingestion', com o seguinte conteúdo:

```toml
[destination.postgres.credentials]
database = "postgresDB"
username = "postgresUser"
password = "postgresPW"
host = "localhost"
port = 5455
connect_timeout = 15
```

Alternativamente, antes de executar o script de ingestão, pode-se definir as variáveis de ambiente.
Isto pode ser feito através de um script em bash como o seguinte:

```bash
export DESTINATION__POSTGRES__CREDENTIALS__DATABASE="postgresDB"
export DESTINATION__POSTGRES__CREDENTIALS__USERNAME="postgresUser"
export DESTINATION__POSTGRES__CREDENTIALS__PASSWORD="postgresPW"
export DESTINATION__POSTGRES__CREDENTIALS__HOST="localhost"
export DESTINATION__POSTGRES__CREDENTIALS__PORT="5455"
```

#### Transformation

Para executar o script de transformação, é necessário definir as seguintes variáveis de ambiente:

```bash
export PG_HOST='localhost'
export PG_PORT=5455
export PG_USERNAME='postgresUser'
export PG_PASSWORD='postgresPW'
export PG_DATABASE='postgresDB'
export PG_SCHEMA_RAW='raw'
export PG_SCHEMA_FINAL='marts'
```

## (Opcional) Preparação do banco de dados de destino

Caso não tenha instalado um banco de dados PostgreSQL, execute o comando abaixo para criar um container para executar testes. É necessário ter o Docker instalado no seu sistema.

```bash
docker run --name postgresDb -p 5455:5432 -e POSTGRES_USER=postgresUser -e POSTGRES_PASSWORD=postgresPW -e POSTGRES_DB=postgresDB -d postgres
```

## Instruções de execução

A partir do diretório raiz do projeto, execute os seguintes comandos:

### Executar apenas a ingestão

```bash
cd ingestion 
uv run ingest.py
```

### Executar apenas a tranformação

```bash
cd transformation 
bash run_dbt.sh
```
### Executar a pipeline completa

```bash
bash pipeline.sh
```

## Automação

A pipeline de dados é executada automaticamente através de uma Github Action, sempre que ocorre uma das condições:
 - um push no ramo main do repositório;
 - às 0h30 (BRT) uma vez por dia, de forma agendada;