from db import Base
from sqlalchemy import Column, Integer, String, Text

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False, index=True)
    precio = Column(Integer, nullable=False)
    url = Column(Text, nullable=True)