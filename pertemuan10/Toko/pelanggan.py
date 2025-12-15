class Pelanggan:
    def __init__(self, nama, saldo):
        self.__nama = nama
        self.__saldo = saldo

    def get_nama(self):
        return self.__nama

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo_baru):
        if saldo_baru >= 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo tidak boleh negatif!")

    def kurangi_saldo(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"{self.__nama} membayar sebesar Rp{jumlah}")
        else:
            print("Saldo tidak cukup!")

    def __str__(self):
        return f"Pelanggan: {self.__nama}, Saldo: Rp{self.__saldo}"
      
class PelangganVIP(Pelanggan):
  def __init__(self, nama, saldo, diskon):
      super().__init__(nama, saldo)
      self.__diskon = diskon
      
  def get_diskon(self):
        return self.__diskon
      
  def kurangi_saldo(self, jumlah):
        jumlah_diskon = jumlah - (jumlah * self.__diskon / 100)
        if jumlah_diskon <= self.get_saldo():
            self.set_saldo(self.get_saldo() - jumlah_diskon)
            print(f"{self.get_nama()} (VIP) membayar Rp{jumlah_diskon} dengan diskon {self.__diskon}%")
        else:
            print("Saldo tidak cukup!")
            
  def __str__(self):
        return f"Pelanggan VIP: {self.get_nama()}, Saldo: Rp{self.get_saldo()}, Diskon: {self.__diskon}%"
