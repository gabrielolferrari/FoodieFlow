from typing import Optional, List
from pydantic import BaseModel as ScBaseModel


class ProductSchema(ScBaseModel):
    id: Optional[int]
    name: str
    price: float
    img: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True
