from fastapi import FastAPI, Depends, HTTPException
import services, schemas
from db import get_db
from sqlalchemy.orm import Session
from security import verify_api_key  # 🔐 IMPORTANTE

app = FastAPI()


@app.get("/productos/", response_model=list[schemas.Producto])
def get_all_productos(
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)  # 🔐 PROTEGIDO
):
    return services.get_productos(db)


@app.post("/productos/", response_model=schemas.Producto)
def create_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)
):
    return services.create_producto(db, producto)


@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def get_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)  # 🔐 PROTEGIDO
):
    db_producto = services.get_producto(db, producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto


@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(
    producto_id: int,
    producto: schemas.ProductoCreate,
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)  # 🔐 PROTEGIDO
):
    db_producto = services.update_producto(db, producto_id, producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto


@app.delete("/productos/{producto_id}", response_model=schemas.Producto)
def delete_producto(
    producto_id: int,
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)  # 🔐 PROTEGIDO
):
    db_producto = services.delete_producto(db, producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto


@app.get("/productos/search/", response_model=list[schemas.Producto])
def search_productos(
    query: str,
    db: Session = Depends(get_db),
    auth: str = Depends(verify_api_key)  # 🔐 PROTEGIDO
):
    return services.search_productos(db, query)