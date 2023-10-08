# language: pt

Funcionalidade: Gerenciamento de Pedidos

Cenário: Cliente lista seus pedidos
    Dado que o cliente está logado no sistema
    Quando ele acessa a seção "Meus Pedidos"
    Então o sistema deve listar todos os pedidos associados a esse cliente