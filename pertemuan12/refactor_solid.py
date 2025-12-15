from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

# Konfigurasi dasar: Semua log level INFO ke atas akan ditampilkan
# Format: Waktu - Level - Nama Kelas/Fungsi - Pesan
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
) 
# Tambahkan logger untuk kelas yang akan kita gunakan
LOGGER = logging.getLogger('Checkout')

@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    """Kontrak: Semua prosesor pembayaran hrus punya method 'process'."""
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass
    
class INotificationService(ABC):
    """Kontrak: Semua layanan notifikasi harus punya method 'send'."""
    @abstractmethod
    def send(self, order: Order):
        pass
    
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Kartu Kredit.")
        return True
    
class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Notif: Mengirim email konfirmasi ke {order.customer_name}.")
        
class CheckoutService: # Tanggung jawab tunggal: Mengkoordinasikan Checkout
    """
    Kelas high-level untuk mengkoordinasi proses transaksi pembayaran.
    
    Kelas ini memisahkan logika pembayaran dan notifikasi (memenuhi SRP).
    """
    def __init__(self, payment_processor: IPaymentProcessor, notifier: INotificationService):
        """
        Menginisialisasi CheckOutService dengan depedensi yang diperlukan.
    
         Args:
            payment_processort (IPaymentProcessor): Implementasi interface pembayaran.
            notifier (INotificationService): Implementsi interface notifikasi.
         """
        self.payment_processor = payment_processor
        self.notifier = notifier
        
    def run_checkout(self, order: Order):
        """
        Menjalankan proses checkout dan memvalidasi pembayaran.
        
        Args:
            order (Order): Objek pesanan yang akan diproses.
            
        Returns:
            bool: True jika checkout sukses, False jika gagal.
        """
        # Logging alih-alih print()
        LOGGER.info(f"Memulai checkout untuk {order.customer_name}. Total: {order.total_price}")
        payment_success = self.payment_processor.process(order) # Delegasi 1
        
        if payment_success:
            order.status = "paid"
            self.notifier.send(order) # Delegasi 2
            LOGGER.info("Checkout Sukses. Status pesanan: PAID.")
            return True
        else:
            # Gunakan level ERROR/WARNING untuk masalah
            LOGGER.error("Pembayaran gagal. Transaksi dibatalkan.")
            return False

        pass
    
andi_order = Order("Andi", 500000)
email_service = EmailNotifier()

cc_processor = CreditCardProcessor()
checkout_cc = CheckoutService(payment_processor=cc_processor, notifier=email_service)
print("--- Skenario 1: Credit Card ---")
checkout_cc.run_checkout(andi_order)

class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses Qris.")
        return True
    
budi_order = Order("Budi", 100000)
qris_processor = QrisProcessor()

checkout_qris = CheckoutService(payment_processor=qris_processor, notifier=email_service)
print("\n--- Skenario 2: Pembuktian OCP (QRIS) ---")
checkout_qris.run_checkout(budi_order)
