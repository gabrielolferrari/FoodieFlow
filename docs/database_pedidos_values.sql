-- Adicionando Clientes
INSERT INTO cliente
(id, cpf, nome, email)
VALUES(1, '4564575632', 'Teste Rodrigues', 'rodrigues@gmail.com');
INSERT INTO cliente
(id, cpf, nome, email)
VALUES(2, '6545778674', 'Josias Silva Carneiro', 'carneiro@gmail.com');
INSERT INTO cliente
(id, cpf, nome, email)
VALUES(3, '5467548979', 'Tulio Fabio Martins', 'fabio@gmail.com');
INSERT INTO cliente
(id, cpf, nome, email)
VALUES(4, '4325678346', 'Fernando Suares', 'fersoares@gmail.com');

-- Pedidos produto
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(1, '000124112023', 3, 1);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(2, '000224112023', 4, 4);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(3, '000324112023', 2, 1);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(4, '000424112023', 2, 1);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(5, '000524112023', 1, 3);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(6, '000624112023', 3, 1);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(7, '000724112023', 3, 4);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(8, '000824112023', 2, 2);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(9, '000924112023', 3, 2);
INSERT INTO pedido
(id, codigo, id_cliente, id_status)
VALUES(10, '001024112023', 2, 3);


-- Produtos
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(1, 'Hambúrguer', 'Completo', 33, 1);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(2, 'Hambúrguer', 'Ausente um dos ingredientes', 30, 1);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(3, 'Batata Frita', '200g', 15, 2);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(4,'Batata Frita', '400g', 30, 2);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(5,'Onion Rings', '12 peças', 16, 2);
INSERT into produto
(id, nome, descricao, preco, id_categoria)
VALUES(6, 'Onion Rings', '20 peças', 28, 2);
INSERT into produto
(id, nome, descricao, preco, id_categoria)
VALUES(7, 'Agua Mineral', '300ml', 3, 3);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(8, 'Refrigerante', 'Lata', 4, 3);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(9, 'Refrigerante', 'Litro', 10, 3);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(10, 'Suco de Laranja', 'Copo', 8, 3);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(11, 'Suco de Laranja', 'Jarra 1 litro', 18, 3);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(12, 'Sorvete', 'Copo de 300 ml', 8, 4);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(13, 'Sorvete com calda', 'Copo de 300ml com cobertura', 10, 4);
INSERT INTO produto
(id, nome, descricao, preco, id_categoria)
VALUES(14, 'Sorvete com Chantilly', 'Copo de 300ml com cobertura e Chantilly', 13, 4);

--Produto Ingredientes
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(1, 2);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(1, 1);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(1, 3);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(1, 4);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(1, 5);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(2, 1);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(2, 2);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(2, 3);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(2, 4);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(2, 5);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(3, 6);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(4, 6);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(5, 7);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(6, 7);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(7, 8);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(8, 9);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(9, 9);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(10, 10);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(11, 10);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(12, 11);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(13, 11);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(13, 12);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(14, 11);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(14, 12);
INSERT INTO produto_ingrediente
(id_produto, id_ingrediente)
VALUES(14, 13);

-- Pedido Produto
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(1, 1);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(1, 3);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(1, 10);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(2, 12);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(3, 1);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(3, 8);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(4, 2);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(4, 5);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(4, 11);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(4, 14);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(5, 1);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(5, 7);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(5, 4);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(6, 1);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(7, 13);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(8, 5);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(8, 1);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(8, 11);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(9, 2);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(9, 14);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(10, 11);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(10, 3);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(10, 6);
INSERT INTO pedido_produto
(id_pedido, id_produto)
VALUES(10, 7);







