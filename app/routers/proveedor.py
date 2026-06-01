from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Proveedor(BaseModel):
    id: int
    nombre: str

proveedores = [
    Proveedor(id=1, nombre="Proveedor A"),
    Proveedor(id=2, nombre="Proveedor B")
]

@router.get("/proveedor", response_model=List[Proveedor])
async def get_proveedores():
    return proveedores

@router.get("/proveedor/{proveedor_id}", response_model=Proveedor)
async def get_proveedor(proveedor_id: int):
    for proveedor in proveedores:
        if proveedor.id == proveedor_id:
            return proveedor
    raise HTTPException(status_code=404, detail="Proveedor no encontrado")

@router.post("/proveedor", response_model=Proveedor)
async def create_proveedor(proveedor: Proveedor):
    proveedores.append(proveedor)
    return proveedor

@router.put("/proveedor/{proveedor_id}", response_model=Proveedor)
async def update_proveedor(proveedor_id: int, updated_proveedor: Proveedor):
    for index, proveedor in enumerate(proveedores):
        if proveedor.id == proveedor_id:
            proveedores[index] = updated_proveedor
            return updated_proveedor
    raise HTTPException(status_code=404, detail="Proveedor no encontrado")

@router.delete("/proveedor/{proveedor_id}", response_model=Proveedor)
async def delete_proveedor(proveedor_id: int):
    for index, proveedor in enumerate(proveedores):
        if proveedor.id == proveedor_id:
            deleted_proveedor = proveedores.pop(index)
            return deleted_proveedor
    raise HTTPException(status_code=404, detail="Proveedor no encontrado")