import daiquiri
from typing import List
from fastapi import APIRouter, Request, status
from starlette.responses import JSONResponse

from schemas.produto_schema import ProductSchema
from repository.produto_repository import create_product, get_product, get_all_products, delete_product

router = APIRouter()
log = daiquiri.getLogger(__name__)


@router.get("/produtos/{id}", response_model=ProductSchema, description='Retorna um produto especificado pelo id')
async def product_get(request: Request, id: int):
    try:
        log.info(f'Produto solicitado com ID: {id}')
        product = get_product(id)
        return product
    except Exception as ex:
        log.error(f'[ADM] Erro ao retornar o produto. {ex}')


@router.get("/produtos", response_model=List[ProductSchema], description='Retorna todos os produto')
async def products_get(request: Request):
    try:
        log.info(f'Todos os produtos solicitados')
        products = get_all_products()

        return products

    except Exception as ex:
        log.error(f'[ADM] Erro ao retornar a listagem de produtos. {ex}')


@router.post("/produtos", status_code=status.HTTP_201_CREATED,
             description='Cria um novo produto')
async def products_post(prod: ProductSchema):
    try:
        product = create_product(
            name=prod.name,
            price=prod.price,
            img=prod.img if hasattr(prod, 'img') else None,
            description=prod.description if hasattr(prod, 'description') else None
        )
        return product

    except Exception as ex:
        log.error(f'[ADM] Erro ao criar/atualizar produto. {ex}')


@router.delete("/produtos/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(request: Request, id: int):
    try:
        if delete_product(id):
            return None  # Retorna uma resposta vazia com status 204 se o produto foi excluído com sucesso
        else:
            return JSONResponse(content={"message": f"Produto com o ID {id} não encontrado"}, status_code=status.HTTP_404_NOT_FOUND)

    except Exception as ex:
        log.error(f'Erro ao excluir produto. {ex}')