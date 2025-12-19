import logging
from abc import ABC, abstractmethod
from typing import List
from models import Product, CartItem

LOGGER = logging.getLogger('SERVICES')

# Abstraksi OCP/DIP
class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass

class CashPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        LOGGER.info("Menerima TUNAI sejumlah: Rp%s", f"{amount:,.0f}")
        return True

# Implementasi BARU (Challenge OCP/DIP): Debit Card
class DebitCardPayment(IPaymentProcessor):
    def process(self, amount: float) -> bool:
        LOGGER.info("Memproses pembayaran DEBIT CARD sejumlah: Rp%s", f"{amount:,.0f}")
        LOGGER.info("Verifikasi chip/PIN, otorisasi bank...")
        return True

class ShoppingCart:
    def __init__(self):
        self._items: dict[str, CartItem] = {}

    def add_item(self, product: Product, quantity: int = 1):
        if product.id in self._items:
            self._items[product.id].quantity += quantity
        else:
            self._items[product.id] = CartItem(product=product, quantity=quantity)
        LOGGER.info("Added %dx %s to cart.", quantity, product.name)

    def get_items(self) -> List[CartItem]:
        return list(self._items.values())

    @property
    def total_price(self) -> float:
        return sum(item.subtotal for item in self._items.values())
