from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    foto_url: str

class Categoria(BaseModel):
    id: int
    nombre: str

class Talla(BaseModel):
    id: int
    nombre: str

class Proveedor(BaseModel):
    id: int
    nombre: str

class Stock(BaseModel):
    id: int
    producto_id: int
    talla_id: int
    cantidad: int

class Venta(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    fecha: str

class Alerta(BaseModel):
    id: int
    producto_id: int
    mensaje: str
