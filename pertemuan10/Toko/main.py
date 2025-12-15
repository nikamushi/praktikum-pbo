from pelanggan import Pelanggan, PelangganVIP
from produk import Produk
from transaksi import Transaksi

pelanggan1 = Pelanggan("Bas", 200000)
pelanggan2 = PelangganVIP("Kara", 300000, 10)

produk1 = Produk("Laptop", 150000, 5)
produk2 = Produk("Mouse", 50000, 10)

print(pelanggan1)
print(pelanggan2)
print(produk1)
print(produk2)
print()

print("=== Transaksi Pelanggan Biasa ===")
transaksi1 = Transaksi(pelanggan1)
transaksi1.tambah_item(produk1, 1)
transaksi1.ringkasan()
transaksi1.proses_transaksi()

print("\n=== Transaksi Pelanggan VIP ===")
transaksi2 = Transaksi(pelanggan2)
transaksi2.tambah_item(produk2, 2)
transaksi2.ringkasan()
transaksi2.proses_transaksi()

print("\n=== Setelah Transaksi ===")
print(pelanggan1)
print(pelanggan2)
