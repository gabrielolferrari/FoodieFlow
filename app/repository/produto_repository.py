import daiquiri
import pytz
import uuid
from sqlalchemy.exc import SQLAlchemyError

log = daiquiri.getLogger(__name__)
tz_sp = pytz.timezone('America/Sao_Paulo')


def create_fund(
    produto
):
    try:
        log.info('create_produto -> Salvando produto')
        with sync_session() as db:

            existing_fund = db.query(produto).filter_by().first()

            if existing_fund:
                print("produto ja existe")
                existing_produto.nome = produto.nome
                ...
            else:
                novo_produto = produto(
                    nome=nome,
                )
                db.add(novo_produto)
            db.commit()
    except SQLAlchemyError as e:
        log.error(f'Erro ao salvar produto no banco: {e}')

        if db.is_active:
            db.rollback()
