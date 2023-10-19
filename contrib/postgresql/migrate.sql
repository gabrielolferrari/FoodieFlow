-- CREATE TABLE Cliente (
--     id SERIAL PRIMARY KEY,
--     cpf VARCHAR(11) NOT NULL,
--     nome VARCHAR(255),
--     email VARCHAR(255)
-- );

-- CREATE TABLE Categoria (
--     id SERIAL PRIMARY KEY,
--     nome VARCHAR(255)
-- );

-- CREATE TABLE Produto (
--     id SERIAL PRIMARY KEY,
--     idCategoria INT REFERENCES Categoria (id),
--     nome VARCHAR(255),
--     descricao TEXT,
--     preco DECIMAL
-- );

-- CREATE TABLE Imagem (
--     id SERIAL PRIMARY KEY,
--     idProduto INT REFERENCES Produto (id),
--     url VARCHAR(255)
-- );

-- CREATE TABLE Ingrediente (
--     id SERIAL PRIMARY KEY,
--     nome VARCHAR(255)
-- );

-- CREATE TABLE Produto_Ingrediente (
--     idProduto INT REFERENCES Produto (id),
--     idIngrediente INT REFERENCES Ingrediente (id),
--     quantidade INT
-- );

-- CREATE TABLE StatusPedido (
--     id SERIAL PRIMARY KEY,
--     estado VARCHAR(255)
-- );

-- CREATE TABLE Pedido (
--     id SERIAL PRIMARY KEY,
--     idCliente INT REFERENCES Cliente (id),
--     idStatusPedido INT REFERENCES StatusPedido (id),
--     codigo INT
-- );

-- CREATE TABLE Item (
--     id SERIAL PRIMARY KEY,
--     idPedido INT REFERENCES Pedido (id),
--     idProduto INT REFERENCES Produto (id),
--     quantidade INT,
--     preco DECIMAL
-- );

-- CREATE TABLE Item_Ingrediente (
--     idItem INT REFERENCES Item (id),
--     idIngrediente INT REFERENCES Ingrediente (id),
--     quantidade INT
-- );

-- ALTER TABLE Cliente ADD FOREIGN KEY (id) REFERENCES Pedido (idCliente);
-- ALTER TABLE Produto ADD FOREIGN KEY (id) REFERENCES Item (idProduto);
-- ALTER TABLE Produto ADD FOREIGN KEY (id) REFERENCES Imagem (idProduto);
-- ALTER TABLE Produto ADD FOREIGN KEY (id) REFERENCES Produto_Ingrediente (idProduto);
-- ALTER TABLE Produto_Ingrediente ADD FOREIGN KEY (idIngrediente) REFERENCES Ingrediente (id);
-- ALTER TABLE Pedido ADD FOREIGN KEY (idStatusPedido) REFERENCES StatusPedido (id);
-- ALTER TABLE Item ADD FOREIGN KEY (idPedido) REFERENCES Pedido (id);
-- ALTER TABLE Item ADD FOREIGN KEY (idProduto) REFERENCES Produto (id);
-- ALTER TABLE Item_Ingrediente ADD FOREIGN KEY (idItem) REFERENCES Item (id);
-- ALTER TABLE Item_Ingrediente ADD FOREIGN KEY (idIngrediente) REFERENCES Ingrediente (id);

-- COMMIT;