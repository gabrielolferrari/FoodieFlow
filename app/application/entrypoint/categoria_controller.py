import daiquiri
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.usecases.categoria_service_impl import CategoriaServiceImpl
from core.ports.categoria_repository import CategoriaRepository
from infrastructure.dataprovider.categoria_database_adapter import CategoriaDatabaseAdapter
from core.model.categoria import Categoria as CategoriaModel
from infrastructure.database import get_db

router = APIRouter()
log = daiquiri.getLogger(__name__)

categoria_repository: CategoriaRepository = CategoriaDatabaseAdapter()
categoria_service = CategoriaServiceImpl(categoria_repository)

@router.post("/", response_model=CategoriaModel, description="Cria uma nova categoria")
def create_categoria(categoria: CategoriaModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Categoria para criação: {categoria}")
        return categoria_service.create_categoria(db, categoria)
    except Exception as ex:
        log.error(f"Erro ao criar categoria. {str(ex)}")
        if "Categoria já cadastrada" in str(ex):
            raise HTTPException(status_code=400, detail="Categoria já cadastrada")
        raise HTTPException(status_code=400, detail="Erro ao criar categoria")

@router.get("/{categoria_id}", response_model=CategoriaModel, description="Busca uma categoria pelo ID")
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando categoria com ID {categoria_id}")
        categoria = categoria_service.get_categoria(db, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        return categoria
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar categoria. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar categoria")

@router.get("/", response_model=list[CategoriaModel], description="Busca todas as categorias")
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando categorias")
        return categoria_service.get_categorias(db, skip, limit)
    except Exception as ex:
        log.error(f"Erro ao buscar categorias. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar categorias")

@router.put("/{categoria_id}", response_model=CategoriaModel, description="Atualiza uma categoria")
def update_categoria(categoria_id: int, updated_categoria: CategoriaModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Categoria recebida para atualização: {updated_categoria}")
        categoria = categoria_service.update_categoria(db, categoria_id, updated_categoria)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        return categoria
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao atualizar categoria. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao atualizar categoria")

@router.delete("/{categoria_id}", description="Deleta uma categoria")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Deletando categoria com ID {categoria_id}")
        categoria = categoria_service.delete_categoria(db, categoria_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        return categoria
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao deletar categoria. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao deletar categoria")