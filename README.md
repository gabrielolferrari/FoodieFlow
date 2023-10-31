# FoodieFlow

Um projeto para gerenciamento de produtos.

### Swagger: http://localhost:8000/docs

### Redoc: http://localhost:8000/redoc

### Documentação disponivel: docs/Tech Challenge - FoodieFlow.pdf

### Coleção do Postman: docs/postman_collection.json

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

4. Add informações iniciais no banco de dados

```sql
-- Adicionando categorias

INSERT INTO categoria (nome) VALUES 
('Lanche'),
('Acompanhamento'),
('Bebida'),
('Sobremesa');

-- Adicionando ingredientes de exemplo

-- Ingredientes para Lanches
INSERT INTO ingrediente (nome) VALUES
('Pão'),
('Hambúrguer de Carne'),
('Queijo'),
('Alface'),
('Tomate');

-- Ingredientes para Acompanhamentos
INSERT INTO ingrediente (nome) VALUES
('Batata Frita'),
('Onion Rings');

-- Ingredientes para Bebidas
INSERT INTO ingrediente (nome) VALUES
('Água'),
('Refrigerante'),
('Suco de Laranja');

-- Ingredientes para Sobremesas
INSERT INTO ingrediente (nome) VALUES
('Sorvete'),
('Calda de Chocolate'),
('Chantilly');

-- Adicionando status

INSERT INTO status (id, nome) VALUES
(1, 'Recebido'),
(2, 'Em preparação'),
(3, 'Pronto'),
(4, 'Finalizado');
```

## Logging

O logging foi configurado usando a biblioteca `daiquiri`. Nos ambientes `HML` e `PRD`, os logs são integrados ao Datadog. Certifique-se de configurar corretamente suas variáveis de ambiente para permitir a integração adequada.

## Desenvolvimento Local

Para iniciar a aplicação e a infraestrutura associada localmente:

1. Use o `Makefile` para executar comandos comuns, como construir e iniciar a aplicação.
2. Use o `docker-compose.yml` para iniciar serviços necessários para a aplicação.

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
