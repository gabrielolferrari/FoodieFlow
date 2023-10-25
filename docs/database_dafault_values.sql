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