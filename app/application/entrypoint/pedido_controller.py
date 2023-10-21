import daiquiri
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.usecases.pedido_service_impl import PedidoServiceImpl
from core.ports.pedido_repository import PedidoRepository
from infrastructure.dataprovider.pedido_database_adapter import PedidoDatabaseAdapter
from core.model.pedido import Pedido as PedidoModel
from infrastructure.database import get_db

router = APIRouter()
log = daiquiri.getLogger(__name__)

pedido_repository: PedidoRepository = PedidoDatabaseAdapter()
pedido_service = PedidoServiceImpl(pedido_repository)

@router.post("/", response_model=PedidoModel, description="Cria um novo pedido")
def create_pedido(pedido: PedidoModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Pedido para criação: {pedido}")
        return pedido_service.create_pedido(db, pedido)
    except Exception as ex:
        log.error(f"Erro ao criar pedido. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao criar pedido")
    
@router.get("/", response_model=list[PedidoModel], description="Busca todos os pedidos")
def read_pedidos_by_status(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando pedidos")
        pedidos = pedido_service.get_pedidos(db, skip, limit)
        if not pedidos:
            raise HTTPException(status_code=404, detail=f"Pedidos não encontrados")
        return pedidos
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar pedidos. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar pedidos")

@router.get("/status/{status}", response_model=list[PedidoModel], description="Busca pedidos por status")
def read_pedidos_by_status(status: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando pedidos com status {status}")
        pedidos = pedido_service.get_pedidos_by_status(db, status, skip, limit)
        if not pedidos:
            raise HTTPException(status_code=404, detail=f"Pedidos não encontrados com o status {status}")
        return pedidos
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar pedidos. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar pedidos")

@router.put("/pagamento/{pedido_id}", description="Atualiza o status do pedido para 'Em preparação'")
def update_pedido_to_preparation(pedido_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Atualizando status do pedido {pedido_id} para 'Em preparação'")
        success = pedido_service.atualizar_status_para_preparacao(db, pedido_id)
        if not success:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return {"message": "Pedido atualizado com sucesso!"}
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao atualizar status do pedido. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao atualizar status do pedido")
