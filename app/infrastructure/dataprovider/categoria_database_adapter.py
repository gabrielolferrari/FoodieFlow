from sqlalchemy.orm import Session
from infrastructure import database
from core.model.categoria import Categoria as CategoriaModel
from core.model.orm.categoria import Categoria as CategoriaORM
from core.ports.categoria_repository import CategoriaRepository

class CategoriaDatabaseAdapter(CategoriaRepository):
    def create_categoria(self, db: Session, categoria: CategoriaModel):
        db_categoria = CategoriaORM(**categoria.dict())
        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria

    def get_categoria(self, db: Session, categoria_id: int):
        return db.query(CategoriaORM).filter(CategoriaORM.id == categoria_id).first()

    def get_categorias(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(CategoriaORM).offset(skip).limit(limit).all()

    def get_categoria_by_nome(self, db: Session, nome: str):
        return db.query(CategoriaORM).filter(CategoriaORM.nome == nome).first()

    def update_categoria(self, db: Session, categoria_id: int, updated_categoria: CategoriaModel):
        db_categoria = db.query(CategoriaORM).filter(CategoriaORM.id == categoria_id).first()
        for field, value in updated_categoria.dict(exclude_unset=True).items():
            setattr(db_categoria, field, value)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria

    def delete_categoria(self, db: Session, categoria_id: int):
        db_categoria = db.query(CategoriaORM).filter(CategoriaORM.id == categoria_id).first()
        if not db_categoria:
            return False
        db.delete(db_categoria)
        db.commit()
        return True 