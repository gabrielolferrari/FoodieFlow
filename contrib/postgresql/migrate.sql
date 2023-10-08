CREATE SCHEMA "FIAP";

-- Criação da tabela Produto
CREATE TABLE "FIAP".produto (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
);

