from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Talla(BaseModel):
    id: int
    nombre: str

# Simulate a database
tallas = [
    Talla(id=1, nombre="S"),
    Talla(id=2, nombre="M"),
    Talla(id=3, nombre="L")
]

@router.get("/talla", response_model=List[Talla])
async def get_tallas():
    return tallas

@router.get("/talla/{talla_id}", response_model=Talla)
async def get_talla(talla_id: int):
    for talla in tallas:
        if talla.id == talla_id:
            return talla
    raise HTTPException(status_code=404, detail="Talla no encontrada")

@router.post("/talla", response_model=Talla)
async def create_talla(talla: Talla):
    tallas.append(talla)
    return talla

@router.put("/talla/{talla_id}", response_model=Talla)
async def update_talla(talla_id: int, updated_talla: Talla):
    for index, talla in enumerate(tallas):
        if talla.id == talla_id:
            tallas[index] = updated_talla
            return updated_talla
    raise HTTPException(status_code=404, detail="Talla no encontrada")

@router.delete("/talla/{talla_id}", response_model=Talla)
async def delete_talla(talla_id: int):
    for index, talla in enumerate(tallas):
        if talla.id == talla_id:
            deleted_talla = tallas.pop(index)
            return deleted_talla
    raise HTTPException(status_code=404, detail="Talla no encontrada")