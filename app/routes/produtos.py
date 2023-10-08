import uuid

import daiquiri
from typing import List
from fastapi import APIRouter, Request, status
from commons.response import make_response

from schemas.produto_schema import ProductSchema
from repository.produto_repository import create_product, get_product
router = APIRouter()
log = daiquiri.getLogger(__name__)


@router.get("/produtos/{id}", response_model=ProductSchema)
async def product_get(request: Request, id):
    try:
        log.info(f'Todos os produtos solicitados')
        product = get_product(id)
        if product:
            return make_response(request=request, body=product, status_code=status.HTTP_200_OK)
        else:
            return make_response(request=request, body=f"Produto com o id: {id} não encontrado",
                             status_code=status.HTTP_200_OK)

    except Exception as ex:
        log.error(f'[ADM] Erro ao retornar a listagem de produtos. {ex}')


@router.get("/produtos", response_model=List[ProductSchema])
async def products_get(request: Request):
    try:
        log.info(f'Todos os produtos solicitados')
        product = get_product(id)

        return make_response(request=request, body=product, status_code=status.HTTP_200_OK)

    except Exception as ex:
        log.error(f'[ADM] Erro ao retornar a listagem de produtos. {ex}')


@router.post("/produtos", status_code=status.HTTP_200_OK, response_model=ProductSchema)
async def products_post(request: Request, prod: ProductSchema):
    try:
        product = create_product(str(uuid.uuid4()), prod.name, prod.price)
        return make_response(request=request, body=product, status_code=status.HTTP_200_OK)

    except Exception as ex:
        log.error(f'[ADM] Erro ao criar/atualizar produto. {ex}')
