from sqlalchemy.orm import Session, joinedload
from core.model.produto import Produto as ProdutoModel
from core.model.orm.produto import Produto as ProdutoORM
from core.model.orm.ingrediente import Ingrediente as IngredienteORM
from core.model.orm.imagem import Imagem as ImagemORM
from core.model.ingrediente import Ingrediente
from core.model.imagem import Imagem
from core.model.produto import ProdutoCompleto


class ProdutoDatabaseAdapter:

    def _to_produto_completo(self, produto: ProdutoORM) -> ProdutoCompleto:
        return ProdutoCompleto(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            id_categoria=produto.id_categoria,
            imagens=[Imagem(caminho=imagem.caminho, id_produto=imagem.id_produto, id=imagem.id) for imagem in produto.imagens],
            ingredientes=[Ingrediente(id=ingrediente.id, nome=ingrediente.nome) for ingrediente in produto.ingredientes]
        )

    def create_produto(self, db: Session, produto: ProdutoModel) -> ProdutoCompleto:
        produto_data = produto.dict(exclude={"ingredientes", "imagens"})
        db_produto = ProdutoORM(**produto_data)

        # Adicionando ingredientes
        ingredientes = produto.dict().get('ingredientes')
        if ingredientes:
            ingredientes_orm = db.query(IngredienteORM).filter(IngredienteORM.id.in_(ingredientes)).all()
            db_produto.ingredientes = ingredientes_orm

        db.add(db_produto)
        db.commit()

        # Lidar com imagens
        imagens = produto.dict().get('imagens')
        if imagens:
            for imagem_path in imagens:
                new_image = ImagemORM(caminho=imagem_path, id_produto=db_produto.id)
                db.add(new_image)
            db.commit()

        db.refresh(db_produto)

        return self._to_produto_completo(db_produto)

    def get_produto(self, db: Session, produto_id: int):
        produto = db.query(ProdutoORM).options(
            joinedload(ProdutoORM.ingredientes),
            joinedload(ProdutoORM.imagens)
        ).filter(ProdutoORM.id == produto_id).first()

        if not produto:
            return None

        return self._to_produto_completo(produto)

    def get_produtos(self, db: Session, skip: int = 0, limit: int = 100):
        produtos = db.query(ProdutoORM).options(
            joinedload(ProdutoORM.ingredientes),
            joinedload(ProdutoORM.imagens)
        ).offset(skip).limit(limit).all()

        return [self._to_produto_completo(produto) for produto in produtos]
    
    def get_produtos_by_categoria(self, db: Session, id_categoria: int, skip: int = 0, limit: int = 100):
        produtos = db.query(ProdutoORM).options(
            joinedload(ProdutoORM.ingredientes),
            joinedload(ProdutoORM.imagens)
        ).filter(ProdutoORM.id_categoria == id_categoria).offset(skip).limit(limit).all()

        return [self._to_produto_completo(produto) for produto in produtos]

    def update_produto(self, db: Session, produto_id: int, updated_produto: ProdutoModel) -> ProdutoCompleto:
        db_produto = db.query(ProdutoORM).filter(ProdutoORM.id == produto_id).first()

        if not db_produto:
            return None

        # Atualizando campos básicos
        updated_data = updated_produto.dict(exclude_unset=True, exclude={"ingredientes", "imagens"})
        for field, value in updated_data.items():
            setattr(db_produto, field, value)

        # Atualizando ingredientes
        ingredientes = updated_produto.dict().get('ingredientes')
        if ingredientes:
            ingredientes_orm = db.query(IngredienteORM).filter(IngredienteORM.id.in_(ingredientes)).all()
            db_produto.ingredientes = ingredientes_orm

        # Atualizando imagens
        imagens = updated_produto.dict().get('imagens')
        if imagens:
            # Removendo imagens existentes
            db.query(ImagemORM).filter(ImagemORM.id_produto == db_produto.id).delete()

            # Adicionando novas imagens
            for imagem_path in imagens:
                new_image = ImagemORM(caminho=imagem_path, id_produto=db_produto.id)
                db.add(new_image)

        db.commit()
        db.refresh(db_produto)

        return self._to_produto_completo(db_produto)

    def delete_produto(self, db: Session, produto_id: int):
        db_produto = db.query(ProdutoORM).filter(ProdutoORM.id == produto_id).first()

        if not db_produto:
            return False

        # Deletando imagens associadas ao produto
        db.query(ImagemORM).filter(ImagemORM.id_produto == produto_id).delete()

        # Deletando o produto
        db.delete(db_produto)
        db.commit()

        return True
