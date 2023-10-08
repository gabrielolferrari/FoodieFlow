from behave import *

# Passos para o Cenário de Cadastro do Cliente
@given('que o cliente não está registrado')
def step_impl(context):
    pass

@when('ele fornece seu CPF, nome e e-mail')
def step_impl(context):
    pass

@when('clica no botão "Registrar"')
def step_impl(context):
    pass

@then('o sistema deve criar um novo registro de cliente')
def step_impl(context):
    assert False, "Ainda não implementado"

@then('informar ao cliente que o registro foi bem-sucedido')
def step_impl(context):
    assert False, "Ainda não implementado"


# Passos para o Cenário de Identificação do Cliente via CPF
@given('que o cliente está na página de identificação')
def step_impl(context):
    pass

@when('ele insere seu CPF')
def step_impl(context):
    pass

@when('clica no botão "Identificar"')
def step_impl(context):
    pass

@then('o sistema deve buscar o cliente pelo CPF')
def step_impl(context):
    assert False, "Ainda não implementado"

@then('mostrar as informações do cliente na tela')
def step_impl(context):
    assert False, "Ainda não implementado"


# Passos para os Cenários de Produto
@given('que o administrador está na página de gerenciamento de produtos')
def step_impl(context):
    pass

@when('ele preenche as informações do produto')
def step_impl(context):
    pass

@when('ele clica no botão "Adicionar Produto"')
def step_impl(context):
    pass

@then('o sistema deve armazenar o novo produto')
def step_impl(context):
    assert False, "Ainda não implementado"

@then('informar ao administrador que o produto foi adicionado com sucesso')
def step_impl(context):
    assert False, "Ainda não implementado"

# ... E os passos para editar e remover o produto ...


# Passos para Buscar produtos por categoria
@given('que o cliente está na página de produtos')
def step_impl(context):
    pass

@when('ele seleciona uma categoria específica')
def step_impl(context):
    pass

@then('o sistema deve listar todos os produtos dessa categoria')
def step_impl(context):
    assert False, "Ainda não implementado"


# Passos para Fake checkout
@given('que o cliente selecionou produtos para comprar')
def step_impl(context):
    pass

@when('ele clica no botão "Enviar para Fila"')
def step_impl(context):
    pass

@then('o sistema deve adicionar os produtos escolhidos à fila de pedidos')
def step_impl(context):
    assert False, "Ainda não implementado"

@then('informar ao cliente que os produtos foram enviados para a fila com sucesso')
def step_impl(context):
    assert False, "Ainda não implementado"


# Passos para Listar os pedidos
@given('que o cliente está logado no sistema')
def step_impl(context):
    pass

@when('ele acessa a seção "Meus Pedidos"')
def step_impl(context):
    pass

@then('o sistema deve listar todos os pedidos associados a esse cliente')
def step_impl(context):
    assert False, "Ainda não implementado"
