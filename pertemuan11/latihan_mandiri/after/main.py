from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Order: 
    customer_name: str
    total_price: float
    status: str = "open"

class IPaymentProcessor(ABC):
    @property
    @abstractmethod
    def payment_name(self) -> str:
        """Nama metode pembayaran untuk ditampilkan"""
        pass
    
    @abstractmethod
    def process(self, order: Order) -> bool:
        """
        Memproses pembayaran untuk order. 
        Return True jika berhasil, False jika gagal.
        """
        pass


class INotificationService(ABC):
    @property
    @abstractmethod
    def service_name(self) -> str:
        """Nama layanan notifikasi"""
        pass
    
    @abstractmethod
    def send(self, order: Order) -> bool:
        """Mengirim notifikasi untuk order."""
        pass

class CreditCardProcessor(IPaymentProcessor):
    @property
    def payment_name(self) -> str:
        return "Credit Card"
    
    def process(self, order: Order) -> bool:
        print(f"    [Payment] Memproses Kartu Kredit...")
        print(f"    [Payment] Menghubungi gateway kartu kredit...")
        print(f"    [Payment] Memverifikasi CVV...")
        print(f"    [✓] Pembayaran Credit Card berhasil!")
        return True


class BankTransferProcessor(IPaymentProcessor):
    @property
    def payment_name(self) -> str:
        return "Bank Transfer"
    
    def process(self, order:  Order) -> bool:
        print(f"    [Payment] Memproses Transfer Bank...")
        print(f"    [Payment] Mengecek rekening tujuan...")
        print(f"    [Payment] Menunggu konfirmasi bank...")
        print(f"    [✓] Pembayaran Bank Transfer berhasil!")
        return True


class EWalletProcessor(IPaymentProcessor):    
    @property
    def payment_name(self) -> str:
        return "E-Wallet"
    
    def process(self, order: Order) -> bool:
        print(f"    [Payment] Memproses E-Wallet...")
        print(f"    [Payment] Mengirim request ke provider...")
        print(f"    [✓] Pembayaran E-Wallet berhasil!")
        return True

class EmailNotifier(INotificationService):
    @property
    def service_name(self) -> str:
        return "Email"
    
    def send(self, order: Order) -> bool:
        print(f"    [Notif] Mengirim email konfirmasi ke {order.customer_name}...")
        print(f"    [✓] Email terkirim!")
        return True


class SmsNotifier(INotificationService):    
    @property
    def service_name(self) -> str:
        return "SMS"
    
    def send(self, order:  Order) -> bool:
        print(f"    [Notif] Mengirim SMS ke {order.customer_name}...")
        print(f"    [✓] SMS terkirim!")
        return True

class CheckoutService:
    def __init__(self, payment_processor: IPaymentProcessor, 
         notifiers: List[INotificationService] = None):
        """
        Dependency Injection (DIP): Bergantung pada Abstraksi,
        bukan implementasi konkrit.
        """
        self._payment_processor = payment_processor
        self._notifiers = notifiers or []
    
    def run_checkout(self, order: Order) -> bool:
        """Menjalankan proses checkout."""
        
        print(f"\n{'='*60}")
        print(f"PROSES CHECKOUT: {order.customer_name}")
        print(f"{'='*60}")
        print(f"Total Pembayaran: Rp {order.total_price:,.0f}")
        print(f"Metode Pembayaran: {self._payment_processor.payment_name}")
        print(f"\n{'-'*40}")
        
        # Delegasi 1: Proses Pembayaran
        print(f"\n>> Memproses Pembayaran ({self._payment_processor.payment_name})")
        payment_success = self._payment_processor.process(order)
        
        if not payment_success:
            print(f"\n{'-'*40}")
            print(f"[✗] CHECKOUT GAGAL - Pembayaran ditolak")
            return False
        
        # Update status
        order.status = "paid"
        
        # Delegasi 2: Kirim Notifikasi
        if self._notifiers:
            print(f"\n>> Mengirim Notifikasi")
            for notifier in self._notifiers:
                notifier. send(order)
        
        print(f"\n{'-'*40}")
        print(f"[✓] CHECKOUT BERHASIL!")
        print(f"    Status Order: {order.status}")
        return True


if __name__ == "__main__":
    print("=" * 60)
    print(" SISTEM CHECKOUT - SETELAH REFACTORING")
    print(" Implementasi:  SRP, OCP, DIP dengan Dependency Injection")
    print("=" * 60)
    email_notifier = EmailNotifier()
    sms_notifier = SmsNotifier()
    print("\n" + "=" * 60)
    print(" SKENARIO 1: Checkout dengan Credit Card")
    print("=" * 60)
    
    order1 = Order("Andi Pratama", 500000)
    cc_processor = CreditCardProcessor()
    
    checkout_cc = CheckoutService(
        payment_processor=cc_processor,
        notifiers=[email_notifier]
    )
    checkout_cc.run_checkout(order1)
    print("\n" + "=" * 60)
    print(" SKENARIO 2: Checkout dengan Bank Transfer")
    print("=" * 60)
    
    order2 = Order("Budi Santoso", 750000)
    bank_processor = BankTransferProcessor()
    
    checkout_bank = CheckoutService(
        payment_processor=bank_processor,
        notifiers=[email_notifier, sms_notifier]  # Multiple notifiers
    )
    checkout_bank.run_checkout(order2)
    
    print("\n" + "=" * 60)
    print(" SKENARIO 3: Checkout dengan E-Wallet")
    print("=" * 60)
    
    order3 = Order("Citra Dewi", 250000)
    ewallet_processor = EWalletProcessor()
    
    checkout_ewallet = CheckoutService(
        payment_processor=ewallet_processor,
        notifiers=[sms_notifier]
    )
    checkout_ewallet.run_checkout(order3)
    
    print("\n" + "=" * 60)
    print(" SKENARIO 4 (CHALLENGE): Pembuktian OCP")
    print(" >> Menambahkan QrisProcessor tanpa mengubah CheckoutService")
    print("=" * 60)
    
    class QrisProcessor(IPaymentProcessor):
        @property
        def payment_name(self) -> str:
            return "QRIS"
        
        def process(self, order:  Order) -> bool:
            print(f"    [Payment] Memproses QRIS...")
            print(f"    [Payment] Menampilkan QR Code...")
            print(f"    [Payment] Menunggu scan dari customer...")
            print(f"    [Payment] Verifikasi pembayaran...")
            print(f"    [✓] Pembayaran QRIS berhasil!")
            return True
    
    order4 = Order("Dani Wijaya", 100000)
    qris_processor = QrisProcessor()
    
    checkout_qris = CheckoutService(
        payment_processor=qris_processor,
        notifiers=[email_notifier, sms_notifier]
    )
    checkout_qris.run_checkout(order4)
    
    print("\n" + "=" * 60)
    print(" SKENARIO 5 (CHALLENGE): Pembuktian OCP")
    print(" >> Menambahkan WhatsAppNotifier tanpa mengubah CheckoutService")
    print("=" * 60)
    
    class WhatsAppNotifier(INotificationService):
        @property
        def service_name(self) -> str:
            return "WhatsApp"
        
        def send(self, order: Order) -> bool:
            print(f"    [Notif] Mengirim WhatsApp ke {order.customer_name}...")
            print(f"    [✓] WhatsApp terkirim!")
            return True
    
    order5 = Order("Eva Marlina", 350000)
    wa_notifier = WhatsAppNotifier()
    
    checkout_full = CheckoutService(
        payment_processor=cc_processor,
        notifiers=[email_notifier, sms_notifier, wa_notifier]  # 3 notifiers! 
    )
    checkout_full.run_checkout(order5)
    
    print("\n" + "=" * 60)
    print(" SELESAI - Semua skenario telah dijalankan")
    print("=" * 60)
