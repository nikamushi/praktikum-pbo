from produk import Produk
from pelanggan import Pelanggan, PelangganVIP

class Transaksi:
    def __init__(self, pelanggan):
        self.__pelanggan = pelanggan
        self.__daftar_item = []
        self.__total = 0

    def tambah_item(self, produk, jumlah):
        if produk.get_stok() >= jumlah:
            self.__daftar_item.append((produk, jumlah))
            self.__total += produk.get_harga() * jumlah
            print(f"{jumlah}x {produk.get_nama()} ditambahkan ke keranjang.")
        else:
            print(f"Stok {produk.get_nama()} tidak mencukupi!")

    def proses_transaksi(self):
        total_bayar = self.__total
        if isinstance(self.__pelanggan, PelangganVIP):
            diskon = self.__pelanggan.get_diskon()
            total_bayar -= (self.__total * diskon / 100)
            print(f"Diskon {diskon}% diterapkan. Total bayar: Rp{total_bayar}")

        if self.__pelanggan.get_saldo() >= total_bayar:
            self.__pelanggan.kurangi_saldo(self.__total)
            for produk, jumlah in self.__daftar_item:
                produk.kurangi_stok(jumlah)
            print(f"Transaksi berhasil! Total: Rp{total_bayar}")
        else:
            print("Transaksi gagal, saldo pelanggan tidak cukup.")

    def ringkasan(self):
        print("\n=== Ringkasan Transaksi ===")
        print(f"Pelanggan: {self.__pelanggan.get_nama()}")
        for produk, jumlah in self.__daftar_item:
            print(f"- {produk.get_nama()} x{jumlah} = Rp{produk.get_harga() * jumlah}")
        print(f"Total: Rp{self.__total}")
