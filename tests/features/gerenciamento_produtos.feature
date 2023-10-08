# language: pt

Funcionalidade: Gerenciamento de Produtos

Cenário: Administrador adiciona um novo produto
    Dado que o administrador está na página de gerenciamento de produtos
    Quando ele preenche as informações do produto
    E clica no botão "Adicionar Produto"
    Então o sistema deve armazenar o novo produto
    E informar ao administrador que o produto foi adicionado com sucesso

Cenário: Administrador edita um produto existente
    Dado que o administrador está na página de gerenciamento de produtos
    Quando ele seleciona um produto para editar
    E altera as informações desejadas
    E clica no botão "Salvar Alterações"
    Então o sistema deve atualizar as informações do produto
    E informar ao administrador que o produto foi atualizado com sucesso

Cenário: Administrador remove um produto
    Dado que o administrador está na página de gerenciamento de produtos
    Quando ele seleciona um produto para remover
    E clica no botão "Remover Produto"
    Então o sistema deve deletar o produto selecionado
    E informar ao administrador que o produto foi removido com sucesso