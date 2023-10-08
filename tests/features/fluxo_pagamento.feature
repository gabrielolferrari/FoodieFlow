# language: pt

Funcionalidade: Fluxo de Pagamento

Cenário: Cliente realiza um fake checkout
    Dado que o cliente selecionou produtos para comprar
    Quando ele clica no botão "Enviar para Fila"
    Então o sistema deve adicionar os produtos escolhidos à fila de pedidos
    E informar ao cliente que os produtos foram enviados para a fila com sucesso