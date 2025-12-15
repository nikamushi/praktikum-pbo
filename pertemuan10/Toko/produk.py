class Produk:
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            print(f"Stok {self.__nama} berkurang {jumlah} unit.")
        else:
            print(f"Stok {self.__nama} tidak cukup!")

    def __str__(self):
        return f"Produk: {self.__nama}, Harga: Rp{self.__harga}, Stok: {self.__stok}"
