import daiquiri
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.usecases.cliente_service_impl import ClienteServiceImpl
from core.ports.cliente_repository import ClienteRepository
from infrastructure.dataprovider.cliente_database_adapter import ClienteDatabaseAdapter
from core.model.cliente import Cliente as ClienteModel
from infrastructure.database import get_db

router = APIRouter()
log = daiquiri.getLogger(__name__)

cliente_repository: ClienteRepository = ClienteDatabaseAdapter()
cliente_service = ClienteServiceImpl(cliente_repository)

@router.post("/", response_model=ClienteModel, description="Cria um novo cliente")
def create_cliente(cliente: ClienteModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Cliente para criação: {cliente}")
        return cliente_service.create_cliente(db, cliente)
    except Exception as ex:
        log.error(f"Erro ao criar cliente. {str(ex)}")
        if "Cliente já cadastrado" in str(ex):
            raise HTTPException(status_code=400, detail="Cliente já cadastrado")
        raise HTTPException(status_code=400, detail="Erro ao criar cliente")

@router.get("/{cliente_id}", response_model=ClienteModel, description="Busca um cliente pelo ID")
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando cliente com ID {cliente_id}")
        cliente = cliente_service.get_cliente(db, cliente_id)
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return cliente
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar cliente. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar cliente")

@router.get("/", response_model=list[ClienteModel], description="Busca todos os clientes")
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando clientes")
        return cliente_service.get_clientes(db, skip, limit)
    except Exception as ex:
        log.error(f"Erro ao buscar clientes. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar clientes")

@router.put("/{cliente_id}", response_model=ClienteModel, description="Atualiza um cliente")
def update_cliente(cliente_id: int, updated_cliente: ClienteModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Cliente recebido para atualização: {updated_cliente}")
        cliente = cliente_service.update_cliente(db, cliente_id, updated_cliente)
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return cliente
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao atualizar cliente. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao atualizar cliente")

@router.delete("/{cliente_id}", description="Deleta um cliente")
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Deletando cliente com ID {cliente_id}")
        success = cliente_service.delete_cliente(db, cliente_id)
        if not success:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return {"message": "Cliente deletado com sucesso!"}
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao deletar cliente: {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao deletar cliente")