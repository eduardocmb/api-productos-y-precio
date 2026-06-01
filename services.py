from models import Producto
from schemas import ProductoCreate
from sqlalchemy.orm import Session

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(nombre=producto.nombre, precio=producto.precio, url=producto.url)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def update_producto(db: Session, producto_id: int, producto: ProductoCreate):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        return None
    db_producto.nombre = producto.nombre
    db_producto.precio = producto.precio
    db_producto.url = producto.url
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if db_producto is None:
        return None
    db.delete(db_producto)
    db.commit()
    return db_producto

def search_productos(db: Session, query: str):
    return db.query(Producto).filter(Producto.nombre.contains(query)).all()