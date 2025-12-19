from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: str
    name: str
    price: float
    
@dataclass
class CartItem:
    product: Product
    quantity: int
    
    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity
