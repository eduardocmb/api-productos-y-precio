from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ProductoBase(BaseModel):
    nombre: str
    precio: int
    url: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        from_attribute = True