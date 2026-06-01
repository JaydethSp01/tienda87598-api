from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Stock(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    cantidad: int

stocks = [
    Stock(id=1, producto_id=1, talla_id=1, cantidad=10),
    Stock(id=2, producto_id=2, talla_id=2, cantidad=5)
]

@router.get("/stock", response_model=List[Stock])
async def get_stocks():
    return stocks

@router.get("/stock/{stock_id}", response_model=Stock)
async def get_stock(stock_id: int):
    for stock in stocks:
        if stock.id == stock_id:
            return stock
    raise HTTPException(status_code=404, detail="Stock no encontrado")

@router.post("/stock", response_model=Stock)
async def create_stock(stock: Stock):
    stocks.append(stock)
    return stock

@router.put("/stock/{stock_id}", response_model=Stock)
async def update_stock(stock_id: int, updated_stock: Stock):
    for index, stock in enumerate(stocks):
        if stock.id == stock_id:
            stocks[index] = updated_stock
            return updated_stock
    raise HTTPException(status_code=404, detail="Stock no encontrado")

@router.delete("/stock/{stock_id}", response_model=Stock)
async def delete_stock(stock_id: int):
    for index, stock in enumerate(stocks):
        if stock.id == stock_id:
            deleted_stock = stocks.pop(index)
            return deleted_stock
    raise HTTPException(status_code=404, detail="Stock no encontrado")