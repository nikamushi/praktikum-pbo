class Kendaraan:
    def __init__(self, merk, tahun_produksi, warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna
        
    def tampilkan_info(self):
        print("Informasi Kendaraan: ")
        print(f"Merk: {self.__merk}")
        print(f"Tahun Produksi: {self.__tahun_produksi}")
        print(f"Warna: {self.__warna}")
    
    def nyalakan_mesin(self):
        print("Mesin kendaraan menyala")
    
class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        super().__init__(merk, tahun_produksi, warna)
        self.__jumlah_pintu = jumlah_pintu
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah Pintu: {self.__jumlah_pintu}")

    def buka_pintu_bagasi(self):
        print("Pintu Bagasi Dibuka!")

class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        super().__init__(merk, tahun_produksi, warna)
        self.__kapasitas_tangki = kapasitas_tangki
    
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Kapasitas Tangki: {self.__kapasitas_tangki} L")
        
    def nyalakan_mesin(self):
        print("Brmm... Mesin motor dinyalakan dengan kick starter!")

# Membuat objek
mobil1 = Mobil("Civic", 2024, "Ungu", 4)
motor1 = Motor("Chopper", 2025, "Hitam", 4.2)

print("=== Mobil ===")
mobil1.tampilkan_info()
mobil1.nyalakan_mesin()
mobil1.buka_pintu_bagasi()

print("\n=== Motor ===")
motor1.tampilkan_info()
motor1.nyalakan_mesin()