CREATE SCHEMA "FIAP";

-- Criação da tabela Produto
CREATE TABLE "FIAP".produto (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    img VARCHAR(255),
    description VARCHAR(255)
);

