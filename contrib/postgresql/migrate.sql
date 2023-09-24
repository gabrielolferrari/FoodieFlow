CREATE SCHEMA "FIAP";

CREATE TABLE "FIAP".PRODUTO (
    id UUID PRIMARY KEY,
    created_at TIMESTAMP,
    nome VARCHAR(255),
    preco FLOAT,
);
