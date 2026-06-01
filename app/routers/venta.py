from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter()

class Venta(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    fecha: date

ventas = [
    Venta(id=1, producto_id=1, cantidad=2, fecha=date(2023, 10, 1)),
    Venta(id=2, producto_id=2, cantidad=1, fecha=date(2023, 10, 2))
]

@router.get("/venta", response_model=List[Venta])
async def get_ventas():
    return ventas

@router.get("/venta/{venta_id}", response_model=Venta)
async def get_venta(venta_id: int):
    for venta in ventas:
        if venta.id == venta_id:
            return venta
    raise HTTPException(status_code=404, detail="Venta no encontrada")

@router.post("/venta", response_model=Venta)
async def create_venta(venta: Venta):
    ventas.append(venta)
    return venta

@router.put("/venta/{venta_id}", response_model=Venta)
async def update_venta(venta_id: int, updated_venta: Venta):
    for index, venta in enumerate(ventas):
        if venta.id == venta_id:
            ventas[index] = updated_venta
            return updated_venta
    raise HTTPException(status_code=404, detail="Venta no encontrada")

@router.delete("/venta/{venta_id}", response_model=Venta)
async def delete_venta(venta_id: int):
    for index, venta in enumerate(ventas):
        if venta.id == venta_id:
            deleted_venta = ventas.pop(index)
            return deleted_venta
    raise HTTPException(status_code=404, detail="Venta no encontrada")