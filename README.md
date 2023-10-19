# FoodieFlow

Um projeto para gerenciamento de produtos.

### Swagger: COLOCAR AQUI

### Collection e documentação disponivel: COLOCAR ONDE

## Configuração de Ambiente

### Rodando projeto local

1. Crie uma cópia do arquivo `env-example` e renomeie para `.env`. Preencha as variáveis de ambiente conforme necessário para configurar o ambiente.

```bash
cp env-example .env
```

2. Tenha instalado o `docker` e `docker-compose` na sua máquina e rode o comando abaixo para subir a aplicação

```bash
docker-compose up -d
```

OBS: O parâmetro `-d` é para rodar em background, caso queira ver os logs, remova o parâmetro.

3. Acesse a aplicação `http://localhost:8000/healthcheck`

## Configuração de Ambiente (antigo)

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd app
cp env-example .env
cd ..

// 1° Terminal
make infra-start

// 2° Terminal
make dev-run
```

Renomeie o arquivo `env-example` para `.env` e preencha as variáveis de ambiente conforme necessário para configurar o ambiente.

## Inicialização do Banco de Dados

O script `init-db.sh` e o arquivo `migrate.sql` são usados para inicializar o banco de dados PostgreSQL. Certifique-se de que todas as migrações estejam atualizadas antes de iniciar a aplicação.

## Logging

O logging foi configurado usando a biblioteca `daiquiri`. Nos ambientes `HML` e `PRD`, os logs são integrados ao Datadog. Certifique-se de configurar corretamente suas variáveis de ambiente para permitir a integração adequada.

## Roteamento

A aplicação possui várias rotas, incluindo:

- Rota de verificação de saúde: `/healthcheck`
- Rota de exemplo: `/v1/webhook` (definida em `EXEMPLOROTA.py`)

Consulte os arquivos de rota para obter mais detalhes sobre as rotas disponíveis e suas funcionalidades.

## Desenvolvimento Local

Para iniciar a aplicação e a infraestrutura associada localmente:

1. Use o `Makefile` para executar comandos comuns, como construir e iniciar a aplicação.
2. Use o `docker-compose.yml` para iniciar serviços dependentes, como o banco de dados PostgreSQL.

## Dependências

A aplicação utiliza várias bibliotecas e ferramentas, incluindo:

- **FastAPI**: Framework web utilizado para criar a API.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interação com o banco de dados.
- **uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **daiquiri**: Utilizado para configurar o logging da aplicação.
- **decouple**: Gerenciador de configurações para separar configurações do código.
- **pytz**: Utilizado para manipulação de fusos horários.
- **psycopg2-binary**: Driver PostgreSQL para SQLAlchemy, usado para conectar-se ao banco de dados PostgreSQL.
- **simplejson**: Uma biblioteca para trabalhar com JSON em Python.
- **pydantic**: Biblioteca para análise de dados e validação de dados Python.
- **uvloop**: Uma implementação baseada em Cython do asyncio event loop.
- **python-decouple**: Uma biblioteca para separar configurações do código Python.
- **pipreqs**: Uma ferramenta que ajuda a gerar um arquivo `requirements.txt` com as dependências do projeto.

Consulte o arquivo `requirements.txt` para uma lista completa das dependências.

---

Se você tiver dúvidas ou precisar de ajuda com a configuração, entre em contato com a equipe de desenvolvimento.
