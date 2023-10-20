from typing import Optional
from pydantic import BaseModel

class IngredienteBase(BaseModel):
    nome: str

class Ingrediente(IngredienteBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True
