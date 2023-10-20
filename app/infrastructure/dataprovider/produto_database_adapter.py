from sqlalchemy.orm import Session
from core.model.produto import Produto as ProdutoModel
from core.model.orm.produto import Produto as ProdutoORM
from core.model.orm.ingrediente import Ingrediente as IngredienteORM

class ProdutoDatabaseAdapter:
    def create_produto(self, db: Session, produto: ProdutoModel):
        db_produto = ProdutoORM(**produto.dict(exclude={"ingredientes"}))
        if "ingredientes" in produto.dict():
            db_produto.ingredientes = [db.query(IngredienteORM).get(ingrediente_id) for ingrediente_id in produto.ingredientes]
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto

    def get_produto(self, db: Session, produto_id: int):
        return db.query(ProdutoORM).filter(ProdutoORM.id == produto_id).first()

    def get_produtos(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(ProdutoORM).offset(skip).limit(limit).all()

    def update_produto(self, db: Session, produto_id: int, updated_produto: ProdutoModel):
        db_produto = db.query(ProdutoORM).filter(ProdutoORM.id == produto_id).first()
        for field, value in updated_produto.dict(exclude_unset=True, exclude={"ingredientes"}).items():
            setattr(db_produto, field, value)
        if "ingredientes" in updated_produto.dict():
            db_produto.ingredientes = [db.query(IngredienteORM).get(ingrediente_id) for ingrediente_id in updated_produto.ingredientes]
        db.commit()
        db.refresh(db_produto)
        return db_produto

    def delete_produto(self, db: Session, produto_id: int):
        db_produto = db.query(ProdutoORM).filter(ProdutoORM.id == produto_id).first()
        if not db_produto:
            return False
        db.delete(db_produto)
        db.commit()
        return True
