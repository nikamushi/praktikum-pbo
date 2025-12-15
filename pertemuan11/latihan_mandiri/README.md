## 📝 Deskripsi Project

Project ini merupakan refactoring sistem checkout order dari kode monolitik yang melanggar prinsip SOLID menjadi kode modular yang mengikuti prinsip **SRP**, **OCP**, dan **DIP** menggunakan **Dependency Injection**.

---

## 🔍 Analisis Pelanggaran SOLID

### Kode Sebelum Refactoring

```python
class OrderManager:
    def process_checkout(self, order: Order, payment_method: str):
        # LOGIKA PEMBAYARAN (hardcoded if/else)
        if payment_method == "credit_card":
            print("Processing Credit Card...")
        elif payment_method == "bank_transfer":
            print("Processing Bank Transfer...")
        elif payment_method == "e_wallet":
            print("Processing E-Wallet...")
        else:
            print("Metode tidak valid.")
            return False

        # LOGIKA NOTIFIKASI (dicampur dalam satu method)
        print(f"Mengirim notifikasi ke {order.customer_name}...")
```

---

### 1️ Pelanggaran Single Responsibility Principle (SRP)

| Aspek           | Penjelasan                                                                                                                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definisi**    | Sebuah class harus memiliki satu dan hanya satu alasan untuk berubah                                                                                                                                                 |
| **Pelanggaran** | `OrderManager` menangani: logika pembayaran (credit card, bank transfer, e-wallet), logika notifikasi (email, SMS), koordinasi checkout, dan update status order                                                     |
| **Dampak**      | Jika ada perubahan pada cara memproses credit card, class harus diubah. Jika ada perubahan pada cara mengirim notifikasi, class yang sama juga harus diubah. Class menjadi "God Class" yang tahu terlalu banyak hal. |

**Bukti Pelanggaran:**

```python
def process_checkout(self, order, payment_method):
    # Tanggung jawab 1: Logika pembayaran
    if payment_method == "credit_card":
        print("Processing Credit Card...")

    # Tanggung jawab 2: Logika notifikasi
    print(f"Mengirim email konfirmasi...")
    print(f"Mengirim SMS...")
```

---

### 2️ Pelanggaran Open/Closed Principle (OCP)

| Aspek           | Penjelasan                                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definisi**    | Class harus terbuka untuk ekstensi (extension), tertutup untuk modifikasi (modification)                                                      |
| **Pelanggaran** | Menambah metode pembayaran baru (QRIS, PayPal, Crypto) memerlukan modifikasi method `process_checkout()` dengan menambah `elif` baru          |
| **Dampak**      | Setiap penambahan fitur berisiko merusak fitur yang sudah ada. Kode semakin panjang dan kompleks. Sulit di-test karena semua logic tercampur. |

**Bukti Pelanggaran:**

```python
def process_checkout(self, order, payment_method):
    if payment_method == "credit_card":
        ...
    elif payment_method == "bank_transfer":
        ...
    elif payment_method == "e_wallet":
        ...
    # HARUS TAMBAH ELIF DI SINI UNTUK METODE BARU!
    # elif payment_method == "qris":
    #     ...
```

---

### 3️ Pelanggaran Dependency Inversion Principle (DIP)

| Aspek           | Penjelasan                                                                                                                                                                                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Definisi**    | High-level module tidak boleh bergantung pada low-level module; keduanya harus bergantung pada abstraksi                                                                                                                    |
| **Pelanggaran** | `OrderManager` (high-level) bergantung langsung pada implementasi konkrit pembayaran dan notifikasi yang di-hardcode dalam if/else                                                                                          |
| **Dampak**      | Tight coupling - tidak bisa mengganti implementasi tanpa mengubah class. Sulit melakukan unit testing (tidak bisa mock payment processor). Tidak fleksibel - tidak bisa menggunakan pembayaran berbeda untuk order berbeda. |

**Bukti Pelanggaran:**

```python
class OrderManager:
    def process_checkout(self, order, payment_method):
        # Bergantung langsung pada implementasi konkrit (string comparison)
        if payment_method == "credit_card":
            # Logic credit card di-hardcode di sini
            print("Processing Credit Card...")
```

---
