from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    foto: str
    precio: float

productos = [
    Producto(id=1, nombre="Camiseta", foto="/images/camiseta.jpg", precio=19.99),
    Producto(id=2, nombre="Pantalón", foto="/images/pantalon.jpg", precio=39.99)
]

@router.get("/producto", response_model=List[Producto])
async def get_productos():
    return productos

@router.get("/producto/{producto_id}", response_model=Producto)
async def get_producto(producto_id: int):
    for producto in productos:
        if producto.id == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.post("/producto", response_model=Producto)
async def create_producto(producto: Producto):
    productos.append(producto)
    return producto

@router.put("/producto/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, updated_producto: Producto):
    for index, producto in enumerate(productos):
        if producto.id == producto_id:
            productos[index] = updated_producto
            return updated_producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.delete("/producto/{producto_id}", response_model=Producto)
async def delete_producto(producto_id: int):
    for index, producto in enumerate(productos):
        if producto.id == producto_id:
            deleted_producto = productos.pop(index)
            return deleted_producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")