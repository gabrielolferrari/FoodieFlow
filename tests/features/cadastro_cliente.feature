# language: pt

Funcionalidade: Cadastro de Cliente no Sistema

Cenário: Cliente se registra no sistema
    Dado que o cliente não está registrado
    Quando ele fornece seu CPF, nome e e-mail
    E clica no botão "Registrar"
    Então o sistema deve criar um novo registro de cliente
    E informar ao cliente que o registro foi bem-sucedido