import daiquiri
from typing import List
import pytz
from sqlalchemy.exc import SQLAlchemyError
from commons.postgres import sync_session
from models.produto_model import Product
from schemas.produto_schema import ProductSchema

log = daiquiri.getLogger(__name__)
tz_sp = pytz.timezone('America/Sao_Paulo')


def create_product(name: str, price: float, img: str = None, description: str = None) -> ProductSchema:
    try:
        log.info('create_produto')
        with sync_session() as db:
            existing_product = db.query(Product).filter_by(name=name).first()
            if existing_product:
                log.info(f'atualizando produto')
                existing_product.name = name
                existing_product.price = price

                if img:
                    existing_product.imgs = img
                if description:
                    existing_product.description = description
            else:
                log.info('criando novo produto')
                new_product = Product(
                    name=name,
                    price=price,
                    imgs=img,
                    description=description
                )
                db.add(new_product)
                existing_product = new_product
            db.commit()
            log.info(f'criado novo produto')

            product_schema = ProductSchema(
                id=existing_product.id,
                name=existing_product.name,
                price=existing_product.price,
                imgs=existing_product.imgs,
                description=existing_product.description
            )
            return product_schema

    except SQLAlchemyError as e:
        log.error(f'Erro ao salvar produto no banco: {e}')
        if db.is_active:
            db.rollback()


def get_product(id: int) -> ProductSchema:
    try:
        log.info('get_product -> Obtendo produto')
        with sync_session() as db:
            product = db.query(Product).filter_by(id=id).first()

            product_schema = ProductSchema(
                id=product.id,
                name=product.name,
                price=product.price,
                imgs=product.imgs,
                description=product.description
            )
            return product_schema


    except SQLAlchemyError as e:
        log.error(f'Erro ao obter produto no banco: {e}')
        if db.is_active:
            db.rollback()


def get_all_products() -> List[ProductSchema]:
    try:
        with sync_session() as db:
            products = db.query(Product).all()
            product_schemas = [ProductSchema(
                id=product.id,
                name=product.name,
                price=product.price,
                imgs=product.imgs,
                description=product.description
            ) for product in products]
            return product_schemas

    except SQLAlchemyError as e:
        log.error(f'Erro ao obter todos os produtos do banco: {e}')

def delete_product(id: int):
    try:
        with sync_session() as db:
            product = db.query(Product).filter_by(id=id).first()
            if product:
                db.delete(product)
                db.commit()
                return True  # Indica que o produto foi excluído com sucesso
            else:
                return False  # Indica que o produto com o ID especificado não foi encontrado

    except SQLAlchemyError as e:
        log.error(f'Erro ao excluir produto do banco: {e}')
        if db.is_active:
            db.rollback()
        return False