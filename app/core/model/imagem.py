from typing import Optional
from pydantic import BaseModel

class ImagemBase(BaseModel):
    caminho: str
    id_produto: int

class Imagem(ImagemBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True
