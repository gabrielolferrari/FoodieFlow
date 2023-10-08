from typing import Optional
from pydantic import BaseModel as ScBaseModel


class ProductSchema(ScBaseModel):
    id: Optional[int]
    nome: Optional[str]
    price: Optional[float]

    class Config:
        orm_mode = True
