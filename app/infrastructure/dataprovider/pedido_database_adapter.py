from sqlalchemy.orm import Session
from core.model.pedido import Pedido as PedidoModel, PedidoCompleto
from core.model.produto import Produto as ProdutoModel
from core.model.status import Status as StatusModel
from core.model.cliente import Cliente as ClienteModel
from core.model.orm.pedido import Pedido as PedidoORM
from core.model.orm.cliente import Cliente as ClienteORM
from core.model.orm.produto import Produto as ProdutoORM
from core.ports.pedido_repository import PedidoRepository
from application.commons.enums.status import StatusEnum
import datetime
import string

class PedidoDatabaseAdapter(PedidoRepository):
    # Definindo os caracteres para a base 62
    BASE62 = string.ascii_uppercase + string.ascii_lowercase + string.digits

    def from_base10_to_base62(self, num):
        """Converte um número da base 10 para base 62."""
        if num == 0:
            return self.BASE62[0]
        arr = []
        while num:
            num, rem = divmod(num, 62)
            arr.append(self.BASE62[rem])
        arr.reverse()
        return ''.join(arr)

    def generate_order_code(self, prefix='PED'):
        now = datetime.datetime.now()
        # Convertendo hora, minuto e segundo para um único número na base 10
        base10_num = now.hour * 3600 + now.minute * 60 + now.second
        # Convertendo esse número para base 62 para compactação
        base62_num = self.from_base10_to_base62(base10_num)
        # Garantindo que a saída tenha 4 caracteres, preenchendo com zeros à esquerda se necessário
        unique_code = base62_num.rjust(4, '0')
        return prefix + unique_code

    def _to_pedido_completo(self, pedido: PedidoORM) -> PedidoCompleto:
        # Convertendo os dados do ORM Cliente para o modelo Cliente
        cliente_model = ClienteModel(
            id=pedido.cliente.id,
            cpf=pedido.cliente.cpf,
            nome=pedido.cliente.nome,
            email=pedido.cliente.email
        )

        # Convertendo os dados do ORM Status para o modelo Status
        status_model = StatusModel(
            id=pedido.status.id,
            nome=pedido.status.nome
        )

        pedido_completo =  PedidoCompleto(
            id=pedido.id,
            codigo=pedido.codigo,
            id_cliente=pedido.id_cliente,
            id_status=pedido.id_status,
            cliente=cliente_model,
            status=status_model,
            produtos=[
                ProdutoModel(
                    id=produto.id,
                    nome=produto.nome,
                    descricao=produto.descricao,
                    preco=produto.preco,
                    id_categoria=produto.id_categoria
                ) for produto in pedido.produtos
            ]
        )
        
        return pedido_completo


    def create_pedido(self, db: Session, pedido: PedidoModel) -> PedidoCompleto:
        # Obter os dados do pedido excluindo "produtos"
        pedido_data = pedido.dict(exclude={"produtos"})

        if 'id_cliente' not in pedido_data:
            raise ValueError("id_cliente é obrigatório para criar um pedido.")
        
        pedido_data['id_status'] = StatusEnum.RECEBIDO.value  # Por padrão, o status é "Recebido"
        
        # Gerar o código do pedido
        pedido_data['codigo'] = self.generate_order_code()
        
        # Criar o pedido ORM
        db_pedido = PedidoORM(**pedido_data)

        # Adicionar produtos ao pedido
        produtos = pedido.dict().get('produtos')
        if produtos:
            produtos_orm = db.query(ProdutoORM).filter(ProdutoORM.id.in_(produtos)).all()
            db_pedido.produtos = produtos_orm

        # Adicionar o pedido ao banco de dados e commitar
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido)

        return self._to_pedido_completo(db_pedido)

    def get_pedidos(self, db: Session, skip: int = 0, limit: int = 100):
        pedidos = db.query(PedidoORM).filter(PedidoORM.id_status != 4).order_by(PedidoORM.id_status, PedidoORM.id).offset(skip).limit(limit).all()
        return [self._to_pedido_completo(pedido) for pedido in pedidos]

    def get_pedidos_by_status(self, db: Session, status: int, skip: int = 0, limit: int = 100):
        pedidos = db.query(PedidoORM).filter(PedidoORM.id_status == status).offset(skip).limit(limit).all()
        return [self._to_pedido_completo(pedido) for pedido in pedidos]

    def atualizar_status_para_preparacao(self, db: Session, pedido_id: int):
        db_pedido = db.query(PedidoORM).filter(PedidoORM.id == pedido_id).first()
        if not db_pedido:
            return False

        db_pedido.id_status = StatusEnum.EM_PREPARACAO.value
        db.commit()
        db.refresh(db_pedido)

        return self._to_pedido_completo(db_pedido)
