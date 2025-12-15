from dataclasses import dataclass

@dataclass
class Order:
    customer_name: str
    total_price:  float
    status: str = "open"


# ============================================================
# KODE BURUK (SEBELUM REFACTOR) - Melanggar SRP, OCP, DIP
# ============================================================
class OrderManager: 
    """
    Kelas ini melanggar: 
    - SRP:  Menangani pembayaran DAN notifikasi dalam satu class
    - OCP: Harus dimodifikasi jika ada metode pembayaran baru
    - DIP: Bergantung langsung pada implementasi konkrit (hardcoded if/else)
    """
    
    def process_checkout(self, order: Order, payment_method: str):
        print(f"\n{'='*50}")
        print(f"Memulai checkout untuk {order.customer_name}...")
        print(f"Total:  Rp {order.total_price: ,.0f}")
        print(f"{'='*50}")
        
        # LOGIKA PEMBAYARAN (Pelanggaran OCP/DIP - hardcoded if/else)
        if payment_method == "credit_card":
            print("[Payment] Processing Credit Card...")
            print("[Payment] Menghubungi gateway kartu kredit...")
            print("[Payment] Memverifikasi CVV...")
            payment_success = True
        elif payment_method == "bank_transfer":
            print("[Payment] Processing Bank Transfer...")
            print("[Payment] Mengecek rekening tujuan...")
            print("[Payment] Menunggu konfirmasi bank...")
            payment_success = True
        elif payment_method == "e_wallet":
            print("[Payment] Processing E-Wallet...")
            print("[Payment] Mengirim request ke provider...")
            payment_success = True
        else: 
            print(f"[ERROR] Metode pembayaran '{payment_method}' tidak valid.")
            return False
        
        if not payment_success:
            print("[✗] Pembayaran GAGAL")
            return False
        
        # LOGIKA NOTIFIKASI (Pelanggaran SRP - seharusnya terpisah)
        print(f"\n[Notif] Mengirim email konfirmasi ke {order.customer_name}...")
        print(f"[Notif] Mengirim SMS ke {order.customer_name}...")
        
        order.status = "paid"
        print(f"\n[✓] CHECKOUT BERHASIL - Status: {order.status}")
        return True

print("=" * 50)
print(" SISTEM CHECKOUT - SEBELUM REFACTORING")
print(" (Kode ini melanggar SRP, OCP, DIP)")
print("=" * 50)

manager = OrderManager()

# Test 1: Credit Card
order1 = Order("Andi", 500000)
manager.process_checkout(order1, "credit_card")

# Test 2: Bank Transfer
order2 = Order("Budi", 750000)
manager.process_checkout(order2, "bank_transfer")

# Test 3: Metode tidak valid
order3 = Order("Citra", 200000)
manager.process_checkout(order3, "bitcoin")  # Tidak valid
