import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("checkout")

@dataclass
class Order: 
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    @property
    @abstractmethod
    def payment_name(self) -> str:
        pass
    
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass

class INotificationService(ABC):
    @property
    @abstractmethod
    def service_name(self) -> str:
        pass
    
    @abstractmethod
    def send(self, order: Order) -> bool:
        pass

class CreditCardProcessor(IPaymentProcessor):
    @property
    def payment_name(self) -> str:
        return "Credit Card"
    
    def process(self, order: Order) -> bool:
        logger.info("Memproses Kartu Kredit (gateway, CVV, verifikasi)")
        return True

class BankTransferProcessor(IPaymentProcessor):
    @property
    def payment_name(self) -> str:
        return "Bank Transfer"
    
    def process(self, order:  Order) -> bool:
        logger.info("Memproses Transfer Bank (cek rekening, konfirmasi)")
        return True

class EWalletProcessor(IPaymentProcessor):
    @property
    def payment_name(self) -> str:
        return "E-Wallet"
    
    def process(self, order: Order) -> bool:
        logger.info("Memproses E-Wallet (request ke provider)")
        return True

class EmailNotifier(INotificationService):
    @property
    def service_name(self) -> str:
        return "Email"
    
    def send(self, order: Order) -> bool:
        logger.info("Mengirim email konfirmasi ke %s", order.customer_name)
        return True

class SmsNotifier(INotificationService):
    @property
    def service_name(self) -> str:
        return "SMS"
    
    def send(self, order:  Order) -> bool:
        logger.info("Mengirim SMS ke %s", order.customer_name)
        return True

class CheckoutService:
    def __init__(self, payment_processor: IPaymentProcessor, 
        notifiers: List[INotificationService] = None):
        self._payment_processor = payment_processor
        self._notifiers = notifiers or []
    
    def run_checkout(self, order: Order) -> bool:
        logger.info("PROSES CHECKOUT: %s | Total: Rp %s | Metode: %s",
                    order.customer_name, f"{order.total_price:,.0f}", self._payment_processor.payment_name)
        
        logger.info("Memproses Pembayaran (%s)", self._payment_processor.payment_name)
        payment_success = self._payment_processor.process(order)
        
        if not payment_success:
            logger.warning("CHECKOUT GAGAL - Pembayaran ditolak untuk %s", order.customer_name)
            return False
        
        order.status = "paid"
        
        if self._notifiers:
            logger.info("Mengirim Notifikasi (%d notifier)", len(self._notifiers))
            for notifier in self._notifiers:
                ok = notifier.send(order)
                if not ok:
                    logger.warning("Notifikasi %s gagal untuk %s", notifier.service_name, order.customer_name)
        
        logger.info("CHECKOUT BERHASIL! Status Order: %s", order.status)
        return True

if __name__ == "__main__":
    logger.info("SISTEM CHECKOUT - SETELAH REFACTORING (SRP, OCP, DIP + Logging)")
    email_notifier = EmailNotifier()
    sms_notifier = SmsNotifier()

    order1 = Order("Andi Pratama", 500000)
    checkout_cc = CheckoutService(CreditCardProcessor(), [email_notifier])
    checkout_cc.run_checkout(order1)

    order2 = Order("Budi Santoso", 750000)
    checkout_bank = CheckoutService(BankTransferProcessor(), [email_notifier, sms_notifier])
    checkout_bank.run_checkout(order2)

    order3 = Order("Citra Dewi", 250000)
    checkout_ewallet = CheckoutService(EWalletProcessor(), [sms_notifier])
    checkout_ewallet.run_checkout(order3)

    class QrisProcessor(IPaymentProcessor):
        @property
        def payment_name(self) -> str:
            return "QRIS"
        def process(self, order:  Order) -> bool:
            logger.info("Memproses QRIS (QR Code, scan, verifikasi)")
            return True

    order4 = Order("Dani Wijaya", 100000)
    checkout_qris = CheckoutService(QrisProcessor(), [email_notifier, sms_notifier])
    checkout_qris.run_checkout(order4)

    class WhatsAppNotifier(INotificationService):
        @property
        def service_name(self) -> str:
            return "WhatsApp"
        def send(self, order: Order) -> bool:
            logger.info("Mengirim WhatsApp ke %s", order.customer_name)
            return True

    order5 = Order("Eva Marlina", 350000)
    wa_notifier = WhatsAppNotifier()
    checkout_full = CheckoutService(CreditCardProcessor(), [email_notifier, sms_notifier, wa_notifier])
    checkout_full.run_checkout(order5)
