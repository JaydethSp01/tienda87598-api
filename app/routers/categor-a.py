from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Categoria(BaseModel):
    id: int
    nombre: str

categorias = [
    Categoria(id=1, nombre="Ropa de Mujer"),
    Categoria(id=2, nombre="Ropa de Hombre")
]

@router.get("/categoria", response_model=List[Categoria])
async def get_categorias():
    return categorias

@router.get("/categoria/{categoria_id}", response_model=Categoria)
async def get_categoria(categoria_id: int):
    for categoria in categorias:
        if categoria.id == categoria_id:
            return categoria
    raise HTTPException(status_code=404, detail="Categoría no encontrada")

@router.post("/categoria", response_model=Categoria)
async def create_categoria(categoria: Categoria):
    categorias.append(categoria)
    return categoria

@router.put("/categoria/{categoria_id}", response_model=Categoria)
async def update_categoria(categoria_id: int, updated_categoria: Categoria):
    for index, categoria in enumerate(categorias):
        if categoria.id == categoria_id:
            categorias[index] = updated_categoria
            return updated_categoria
    raise HTTPException(status_code=404, detail="Categoría no encontrada")

@router.delete("/categoria/{categoria_id}", response_model=Categoria)
async def delete_categoria(categoria_id: int):
    for index, categoria in enumerate(categorias):
        if categoria.id == categoria_id:
            deleted_categoria = categorias.pop(index)
            return deleted_categoria
    raise HTTPException(status_code=404, detail="Categoría no encontrada")