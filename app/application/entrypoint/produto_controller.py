import daiquiri
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.usecases.produto_service_impl import ProdutoServiceImpl
from core.ports.produto_repository import ProdutoRepository
from infrastructure.dataprovider.produto_database_adapter import ProdutoDatabaseAdapter
from core.model.produto import Produto as ProdutoModel
from infrastructure.database import get_db

router = APIRouter()
log = daiquiri.getLogger(__name__)

produto_repository: ProdutoRepository = ProdutoDatabaseAdapter()
produto_service = ProdutoServiceImpl(produto_repository)

@router.post("/", response_model=ProdutoModel, description="Cria um novo produto")
def create_produto(produto: ProdutoModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Produto para criação: {produto}")
        return produto_service.create_produto(db, produto)
    except Exception as ex:
        log.error(f"Erro ao criar produto. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao criar produto")

@router.get("/{produto_id}", response_model=ProdutoModel, description="Busca um produto pelo ID")
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando produto com ID {produto_id}")
        produto = produto_service.get_produto(db, produto_id)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return produto
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar produto. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar produto")
    
@router.get("/categoria/{id_categoria}", response_model=list[ProdutoModel], description="Busca um produtos pelo ID da categoria")
def read_produtos_by_categoria(id_categoria: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando produtos com ID da categoria {id_categoria}")
        produto = produto_service.get_produtos_by_categoria(db, id_categoria)
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produtos não encontrado para a categoria {id_categoria}")
        return produto
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao buscar produto. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar produtos")

@router.get("/", response_model=list[ProdutoModel], description="Busca todos os produtos")
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        log.info(f"Buscando produtos")
        return produto_service.get_produtos(db, skip, limit)
    except Exception as ex:
        log.error(f"Erro ao buscar produtos. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao buscar produtos")

@router.put("/{produto_id}", response_model=ProdutoModel, description="Atualiza um produto")
def update_produto(produto_id: int, updated_produto: ProdutoModel, db: Session = Depends(get_db)):
    try:
        log.info(f"Produto recebido para atualização: {updated_produto}")
        produto = produto_service.update_produto(db, produto_id, updated_produto)
        if not produto:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return produto
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao atualizar produto. {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao atualizar produto")

@router.delete("/{produto_id}", description="Deleta um produto")
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    try:
        log.info(f"Deletando produto com ID {produto_id}")
        success = produto_service.delete_produto(db, produto_id)
        if not success:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return {"message": "Produto deletado com sucesso!"}
    except HTTPException:
        raise
    except Exception as ex:
        log.error(f"Erro ao deletar produto: {str(ex)}")
        raise HTTPException(status_code=400, detail="Erro ao deletar produto")
