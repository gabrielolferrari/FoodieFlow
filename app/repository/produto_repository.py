import daiquiri
import pytz
import uuid
from sqlalchemy.exc import SQLAlchemyError
from commons.postgres import sync_session
from models.produto_model import Product


log = daiquiri.getLogger(__name__)
tz_sp = pytz.timezone('America/Sao_Paulo')


def create_product(
    id: uuid,
    name: str,
    price: float
):
    try:
        log.info('create_produto -> Salvando produto')
        with sync_session() as db:

            existing_product = db.query(name).filter_by().first()
            if existing_product:
                existing_product.nome = name
                existing_product.price = price
                product = existing_product
            else:
                new_product = Product(
                    id=id,
                    name=name,
                    price=price
                )
                db.add(new_product)
                product = new_product
            db.commit()
            return product

    except SQLAlchemyError as e:
        log.error(f'Erro ao salvar produto no banco: {e}')
        if db.is_active:
            db.rollback()


def get_product(
    id: uuid
):
    try:
        log.info('get_product -> Obtendo produto')
        with sync_session() as db:
            product = db.query(Product).filter_by(id=id).first()
            if product:
                return product
            else:
                return None

    except SQLAlchemyError as e:
        log.error(f'Erro ao obter produto no banco: {e}')
        if db.is_active:
            db.rollback()