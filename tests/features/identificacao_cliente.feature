# language: pt

Funcionalidade: Identificação de Cliente

Cenário: Cliente se identifica usando o CPF
    Dado que o cliente está na página de identificação
    Quando ele insere seu CPF
    E clica no botão "Identificar"
    Então o sistema deve buscar o cliente pelo CPF
    E mostrar as informações do cliente na tela